#!/usr/bin/python3
""" Console Module for the AirBnB clone project """
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone"""
    prompt = "(hbnb) "  # Set the custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True  # Returning True exits the cmd loop

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a newline before exiting
        return True  # Returning True exits the cmd loop

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass  # Overrides the default behavior which repeats the last command

if __name__ == '__main__':
    HBNBCommand().cmdloop()  # Start the command loop
