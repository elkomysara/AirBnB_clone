
# AirBnB Clone - The Console

This project is part of the AirBnB clone, focusing on building a command-line interpreter to manage AirBnB objects.

## Table of Contents
- [Description](#description)
- [Command Interpreter](#command-interpreter)
  - [How to Start](#how-to-start)
  - [How to Use](#how-to-use)
  - [Examples](#examples)
- [Features](#features)
- [File Structure](#file-structure)
- [Authors](#authors)

## Description
The AirBnB clone project aims to recreate the backend of the popular AirBnB web application. This first part is a command-line interface (CLI) that manages various objects like users, places, cities, and more. The command interpreter allows for creating, updating, retrieving, and deleting instances of these objects, while also handling the storage of the objects in a JSON file.

This console will be the base for future web applications, connecting to the front-end, database, and more advanced features like APIs and user management.

## Command Interpreter
The command interpreter provides functionalities similar to the shell but limited to managing AirBnB objects.

### How to Start
1. Clone the repository:
    ```bash
    git clone https://github.com/elkomysara/AirBnB_clone.git
    ```
2. Navigate into the project directory:
    ```bash
    cd AirBnB_clone
    ```
3. Start the console:
    ```bash
    ./console.py
    ```

### How to Use
The console supports the following commands:
- `create <class_name>`: Creates a new instance of a class.
- `show <class_name> <id>`: Retrieves an instance based on the class name and id.
- `destroy <class_name> <id>`: Deletes an instance.
- `all <class_name>`: Shows all instances of a class.
- `update <class_name> <id> <attribute_name> "<attribute_value>"`: Updates an instance’s attributes.

### Examples
#### Interactive Mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create User
(hbnb) show User 1234-1234-1234
(hbnb) all User
(hbnb) destroy User 1234-1234-1234
(hbnb) quit
$
```

#### Non-Interactive Mode
```bash
$ echo "create User" | ./console.py
$ echo "show User 1234-1234-1234" | ./console.py
```

## Features
- **Object management**: Create, show, update, and delete objects.
- **Storage**: Persistent storage using JSON files.
- **Interactive & non-interactive modes**: Execute commands manually or pipe them.

## File Structure
```bash
AirBnB_clone/
├── console.py             # Entry point for the command interpreter
├── models/                # Directory containing all models
│   ├── base_model.py      # Base class with common methods and attributes
│   ├── user.py            # User class
│   └── engine/
│       └── file_storage.py # File storage engine for JSON serialization
├── tests/                 # Unit tests
│   ├── test_models/
│   └── test_console.py    # Unit tests for the console
└── README.md              # Project documentation
```

## Authors
This project was developed by:
- [Sara Elkomy](https://github.com/elkomysara)
```
