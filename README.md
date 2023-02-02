<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<h1>C_repo_Initializer : A Python script for creating a basic C project structure</h1>

# Description :
This script sets up a basic project structure with optional components such as Epitech header, custom initialization, unit tests, and a library. The script prompts the user for their desired options and creates the corresponding files and directories based on their choices.

# Requirements : 
Python 3 and inquirerPy library

# Usage :

* Clone or download the repository:<br /> 
* Follow the prompt to choose your desired options
* The script will generate the necessary files and directories based on your choices.

## File Structure :

The generated file structure includes:
- A main file (main.c) program
- A header file for the project (include/projectname.h)
- A Makefile for the project
- A .gitignore file to ignore specific files when using Git
- Optionally, a tests/ directory with a Makefile for unit tests
- Optionally, a lib/ directory for a library

__Note__: The script uses the default locale language of the system to determine the language used in the prompts. If the default locale language is French, the prompts will be in French, otherwise, they will be in English. The script assumes the presence of a `translation.json` file for the language used in the prompts.

# Run it from anywhere in your shell :

In order to run the script from anywhere in your shell, you need to place the file in a location that is part of your PATH. The most common location for this is `/usr/local/bin`. You can move the file to this location by using the following command:
