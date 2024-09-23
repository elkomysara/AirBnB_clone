#!/usr/bin/python3
"""Entry point of the command interpreter."""

import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

classes = {
    "BaseModel": BaseModel, "User": User, "State": State, "City": City,
    "Amenity": Amenity, "Place": Place, "Review": Review
}

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console."""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
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
        elif args[0] not in classes:
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
        """Prints all string representation of all instances or based on class name."""
        if arg and arg not in classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if not arg or arg == obj.__class__.__name__:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id with a dictionary or attribute."""
        args = arg.split(" ", 2)
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        if len(args) == 3:
            if args[2].startswith("{") and args[2].endswith("}"):
                attr_dict = eval(args[2])
                for attr_name, attr_value in attr_dict.items():
                    if hasattr(obj, attr_name):
                        attr_type = type(getattr(obj, attr_name))
                        setattr(obj, attr_name, attr_type(attr_value))
                    else:
                        setattr(obj, attr_name, attr_value)
            else:
                attr_name, attr_value = args[2].split(" ", 1)
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value.strip('"')))
                else:
                    setattr(obj, attr_name, attr_value.strip('"'))
            obj.save()

    def default(self, line):
        """Handle special commands like <class name>.all() and <class name>.count()"""
        if "." in line:
            parts = line.split(".", 1)
            class_name = parts[0]
            if class_name in classes:
                if parts[1] == "all()":
                    self.do_all(class_name)
                elif parts[1] == "count()":
                    print(len([obj for obj in storage.all().values() if obj.__class__.__name__ == class_name]))
                elif parts[1].startswith("show("):
                    obj_id = parts[1][5:-1].strip('"')
                    self.do_show(f"{class_name} {obj_id}")
                elif parts[1].startswith("destroy("):
                    obj_id = parts[1][8:-1].strip('"')
                    self.do_destroy(f"{class_name} {obj_id}")
                elif parts[1].startswith("update("):
                    command = parts[1][7:-1]
                    if command.startswith("{"):
                        self.do_update(f"{class_name} {command}")
                    else:
                        command_parts = command.split(", ")
                        obj_id, attr_name, attr_value = command_parts[0].strip('"'), command_parts[1].strip('"'), command_parts[2].strip('"')
                        self.do_update(f"{class_name} {obj_id} {attr_name} {attr_value}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
