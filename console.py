#!/usr/bin/python3
"""Entry point of the command interpreter."""

import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def default(self, line):
        """Handles commands in <class name>.command() format."""
        args = line.split('.')
        if len(args) == 2:
            class_name = args[0]
            command = args[1].split('(')[0]
            if class_name in self.classes:
                if command == "all":
                    self.do_all(class_name)
                elif command == "count":
                    self.do_count(class_name)
                elif command == "show":
                    instance_id = args[1].split('(')[1].strip('")')
                    self.do_show(f"{class_name} {instance_id}")
                elif command == "destroy":
                    instance_id = args[1].split('(')[1].strip('")')
                    self.do_destroy(f"{class_name} {instance_id}")
                elif command == "update":
                    update_args = args[1].split('(')[1].strip(')')
                    if '{' in update_args:
                        instance_id, dict_rep = update_args.split(', ', 1)
                        self.do_update(f"{class_name} {instance_id.strip('\"')} {dict_rep}")
                    else:
                        instance_id, attr_name, attr_value = update_args.split(', ')
                        self.do_update(f"{class_name} {instance_id.strip('\"')} {attr_name.strip('\"')} {attr_value.strip('\"')}")
            else:
                print("** class doesn't exist **")
        else:
            print(f"*** Unknown syntax: {line}")

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances, or based on class name."""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if not arg or arg == obj.__class__.__name__:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_count(self, class_name):
        """Counts the number of instances of a given class."""
        count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == class_name)
        print(count)

    def do_update(self, arg):
        """Updates an instance based on class name, id, attribute name, and value or dictionary."""
        args = arg.split(" ", 2)

        if len(args) < 2:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]

                # Handle dictionary update
                if args[2].startswith('{') and args[2].endswith('}'):
                    try:
                        attr_dict = json.loads(args[2])
                        for attr_name, attr_value in attr_dict.items():
                            setattr(obj, attr_name, attr_value)
                        obj.save()
                    except json.JSONDecodeError:
                        print("** invalid dictionary format **")
                else:
                    # Handle regular attribute update
                    attr_args = args[2].split(" ", 1)
                    if len(attr_args) < 2:
                        print("** attribute name or value missing **")
                    else:
                        attr_name = attr_args[0]
                        attr_value = attr_args[1].strip('"')

                        # Attempt to cast the attribute value to the appropriate type
                        if attr_value.isdigit():
                            attr_value = int(attr_value)
                        else:
                            try:
                                attr_value = float(attr_value)
                            except ValueError:
                                pass  # Leave it as a string if it's not a number

                        setattr(obj, attr_name, attr_value)
                        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
