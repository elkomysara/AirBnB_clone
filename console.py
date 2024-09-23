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
import re  # To handle dot notation commands


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
        """Handle dot notation for 'all()', 'count()', and 'show()'"""
        match = re.match(r"(\w+)\.(\w+)\((.*)\)", line)
        if match:
            class_name, command, args = match.groups()
            args = args.strip('"')  # Remove any surrounding quotes
            if class_name in self.classes:
                if command == "all":
                    self.do_all(class_name)
                elif command == "count":
                    self.do_count(class_name)
                elif command == "show":
                    self.do_show(f"{class_name} {args}")
                else:
                    print("** unknown command **")
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
        """Updates an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')
                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
