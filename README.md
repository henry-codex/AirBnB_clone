# Console Usage Guide

This guide provides instructions on how to use the console for the AirBnB clone project.

## Launch the Console

1. Clone the repository to your local machine:
git clone https://github.com/henry-codex/AirBnB_clone.git


2. Open your terminal or command prompt.

3. Navigate to the directory where your `console.py` file is located:


4. Run the command `console.py` to start the console.

## Available Commands

The console supports the following commands:

- `quit` or `EOF`: Exit the console.
- `create <className>`: Create a new object of the specified class.
- `show <className> <objectId>`: Show details of a specific object.
- `destroy <className> <objectId>`: Delete an object.
- `all` or `all <className>`: Show all objects or objects of a specific class.
- `count <className>`: Count the number of instances of a class.
- `update <className> <objectId> <attribute> <value>`: Update an object's attribute with a new value.
- `batch_update <className> <key=value> <key=value> ...`: Update multiple objects with new information.
- `batch_delete <className>`: Delete multiple objects of a class.
- `batch_count <className1> <className2> ...`: Count the number of instances of multiple classes.
- `batch_show <className>`: Show multiple objects of a class.
- `search <className> <attribute> <value>`: Search for objects based on attribute values.
- `help` or `help <command>` or `help <className>`: Display help information for a command or class.

## Usage Examples

Here are some usage examples for the commands:

- To create a new User object: `create User`
- To show details of a User object with id "abc123": `show User abc123`
- To delete a Place object with id "xyz789": `destroy Place xyz789`
- To show all objects: `all`
- To show all objects of a specific class, e.g., Review: `all Review`
- To count the number of User instances: `count User`
- To update the name attribute of a User object with id "abc123": `update User abc123 name "John Doe"`
- To update multiple User objects with the same attribute and value: `batch_update User name="John Doe" active=True`
- To delete all User objects: `batch_delete User`
- To count the number of instances of User and Place classes: `batch_count User Place`
- To show all User objects: `batch_show User`
- To search for Place objects with attribute `city` having the value "New York": `search Place city "New York"`

## Exiting the Console

You can exit the console by typing `quit` or pressing `Ctrl + D` (EOF) on your keyboard.


