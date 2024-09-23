#!/usr/bin/python3
"""Entry point of the command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
import json


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
        """Handle dot notation for 'all()', 'count()', 'show()', 'destroy()', and 'update()'."""
        match = re.match(r"(\w+)\.(\w+)\((.*)\)", line)
        if match:
            class_name, command, args = match.groups()
            args = args.split(", ", 1)
            if len(args) > 1:
                args[1] = args[1].strip()  # Strip any extra spaces
            if class_name in self.classes:
                if command == "all":
                    self.do_all(class_name)
                elif command == "count":
                    self.do_count(class_name)
                elif command == "show":
                    if len(args) > 0:
                        self.do_show(f"{class_name} {args[0].strip('\"')}")
                elif command == "destroy":
                    if len(args) > 0:
                        self.do_destroy(f"{class_name} {args[0].strip('\"')}")
                elif command == "update":
                    if len(args) > 0:
                        if args[1].startswith("{") and args[1].endswith("}"):
                            # Treat as dictionary update
                            try:
                                dictionary = json.loads(args[1])
                                self.do_update(f"{class_name} {args[0].strip('\"')} {json.dumps(dictionary)}")
                            except json.JSONDecodeError:
                                print("** invalid dictionary format **")
                        else:
                            # Treat as individual attribute update
                            other_args = args[1].split(", ")
                            self.do_update(f"{class_name} {args[0].strip('\"')} {other_args[0]} {other_args[1]}")
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
        """Updates an instance based on class name, id, attribute name, and attribute value."""
        args = arg.split(" ", 2)  # Split by spaces, keeping the rest as one part

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
                if args[2].startswith("{") and args[2].endswith("}"):
                    try:
                        attr_dict = json.loads(args[2])
                        for attr_name, attr_value in attr_dict.items():
                            if isinstance(attr_value, str):
                                setattr(obj, attr_name, attr_value)
                            elif isinstance(attr_value, (int, float)):
                                setattr(obj, attr_name, attr_value)
                        obj.save()
                    except json.JSONDecodeError:
                        print("** invalid dictionary format **")
                else:
                    # Handle regular attribute update
                    attr_args = args[2].split()
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
