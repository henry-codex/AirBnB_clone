#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models import base_model
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.stdin.isatty() else ''

    classes = {
        'BaseModel': base_model.BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int,
        'number_bathrooms': int,
        'max_guest': int,
        'price_by_night': int,
        'latitude': float,
        'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.stdin.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax"""
        parts = line.strip().split(' ')

        if len(parts) >= 2 and '.' in parts[1]:
            cmd_parts = parts[1].split('.')
            if cmd_parts[0] in self.classes and cmd_parts[1] in self.dot_cmds:
                parts[1] = cmd_parts[1] + ' ' + cmd_parts[0]
                line = ' '.join(parts)

        return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.stdin.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, arg):
        """Exit the HBNB console"""
        return True

    def help_quit(self):
        """Prints help documentation for quit"""
        print("Exit the program with formatting")

    def do_EOF(self, arg):
        """Handle EOF to exit program"""
        print()
        return True

    def help_EOF(self):
        """Prints help documentation for EOF"""
        print("Exit the program without formatting")

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def do_create(self, arg):
        """Create a new object of any class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """Help information for the create command"""
        print("Create a new object of any class")
        print("Usage: create <className>")

    def do_show(self, arg):
        """Show an individual object"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def help_show(self):
        """Help information for the show command"""
        print("Show an individual instance of a class")
        print("Usage: show <className> <objectId>")

    def do_destroy(self, arg):
        """Destroy a specified object"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def help_destroy(self):
        """Help information for the destroy command"""
        print("Destroy an individual instance of a class")
        print("Usage: destroy <className> <objectId>")

    def do_all(self, arg):
        """Show all objects or objects of a specific class"""
        objects = []
        if not arg:
            objects = list(storage.all().values())
        elif arg in self.classes:
            class_name = arg
            objects = self.classes[class_name].all()
        else:
            print("** class doesn't exist **")
            return

        print(objects)

    def help_all(self):
        """Help information for the all command"""
        print("Show all objects or objects of a specific class")
        print("Usage: all [<className>]")

    def do_count(self, arg):
        """Count the number of instances of a class"""
        if arg in self.classes:
            class_name = arg
            count = self.classes[class_name].count()
            print(count)
        else:
            print("** class doesn't exist **")

    def help_count(self):
        """Help information for the count command"""
        print("Count the number of instances of a class")
        print("Usage: count <className>")

    def do_update(self, arg):
        """Update an object with new information"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]

        obj = storage.all()[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

    def help_update(self):
        """Help information for the update command"""
        print("Update an object with new information")
        print("Usage: update <className> <objectId> <attribute> <value>")

    def do_batch_update(self, arg):
        """Update multiple objects with new information"""
        args = arg.split()
        if len(args) < 4:
            print("** missing arguments **")
            print("Usage: batch_update <className> <key=value> "
                  "<key=value> ...")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        class_attrs = self.classes[class_name].__dict__.keys()

        kwargs = {}
        for pair in args[1:]:
            if '=' not in pair:
                print("** invalid argument format **")
                print("Usage: batch_update <className> <key=value> "
                      "<key=value> ...")
                return
            attr, value = pair.split('=')
            if attr not in class_attrs:
                print(f"** {class_name} doesn't have attribute '{attr}' **")
                return
            kwargs[attr] = value

        objs = self.classes[class_name].all()
        for obj in objs:
            for attr, value in kwargs.items():
                setattr(obj, attr, value)
            obj.save()

    def help_batch_update(self):
        """Help information for the batch_update command"""
        print("Update multiple objects with new information")
        print("Usage: batch_update <className> <key=value> <key=value> ...")

    def do_batch_delete(self, arg):
        """Delete multiple objects of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        objs = self.classes[class_name].all()
        for obj in objs:
            key = class_name + '.' + obj.id
            del storage.all()[key]
            obj.save()

    def help_batch_delete(self):
        """Help information for the batch_delete command"""
        print("Delete multiple objects of a class")
        print("Usage: batch_delete <className>")

    def do_batch_count(self, arg):
        """Count the number of instances of multiple classes"""
        args = arg.split()
        if len(args) == 0:
            print("** class names missing **")
            return

        counts = {}
        for class_name in args:
            if class_name in self.classes:
                count = self.classes[class_name].count()
                counts[class_name] = count
            else:
                print(f"** {class_name} class doesn't exist **")

        for class_name, count in counts.items():
            print(f"{class_name}: {count}")

    def help_batch_count(self):
        """Help information for the batch_count command"""
        print("Count the number of instances of multiple classes")
        print("Usage: batch_count <className1> <className2> ...")

    def do_batch_show(self, arg):
        """Show multiple objects of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        objs = self.classes[class_name].all()
        print(objs)

    def help_batch_show(self):
        """Help information for the batch_show command"""
        print("Show multiple objects of a class")
        print("Usage: batch_show <className>")

    def do_search(self, arg):
        """Search for objects based on attribute values"""
        args = arg.split()
        if len(args) < 2:
            print("** missing arguments **")
            print("Usage: search <className> <attribute> <value>")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        attr_name = args[1]
        attr_value = ' '.join(args[2:])

        objs = [v for k, v in storage.all().items()
                if k.split('.')[0] == class_name and
                hasattr(v, attr_name) and
                getattr(v, attr_name) == attr_value]

        print(objs)

    def help_search(self):
        """Help information for the search command"""
        print("Search for objects based on attribute values")
        print("Usage: search <className> <attribute> <value>")

    def do_help(self, arg):
        """Override the default help command to display custom help messages"""
        if arg:
            if arg in self.classes:
                class_name = arg
                class_obj = self.classes[class_name]
                print(class_obj.__doc__)
            elif arg in self.dot_cmds:
                method_name = 'help_' + arg
                if hasattr(self, method_name):
                    getattr(self, method_name)()
                else:
                    print(f"No help available for {arg}")
            else:
                print(f"No help available for {arg}")
        else:
            super().do_help(arg)

    def help_help(self):
        """Help information for the help command"""
        print("Show help information for a specific command or class")
        print("Usage: help [<command> | <className>]")

    def do_EOF(self, arg):
        """Handle EOF to exit program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
