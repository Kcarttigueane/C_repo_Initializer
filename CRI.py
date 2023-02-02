#!/usr/bin/env python3

import datetime
import json
import locale
import os

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

# ! DATA :

current_year = datetime.datetime.now().year
directory_name = os.path.basename(os.getcwd())
filename = os.path.basename(__file__)

TRANSLATION_DATA = {
    "english": {
        "questions": {
            "binary_name": "Enter your binary file name :",
            "custom_init": "Do you want to use a custom init ?",
            "epitech_header": "Do you want an Epitech Header for your files ?",
            "unit_tests": "Do you want a tests directory with a Makefile for unit tests ?",
            "lib": "Do you want a lib directory and a lib.h file ?"
        },
        "answers": {
            "yes": "Yes",
            "no": "No",
            "custom": "Custom",
            "classic": "Classic"
        },
        "errors": {
            "binary_name": "Please enter a valid binary file name, you can't leave it blank."
        }
    },
    "french": {
        "questions": {
            "binary_name": "Entrez le nom de votre fichier binaire :",
            "custom_init": "Voulez-vous utiliser un init personnalisé ?",
            "epitech_header": "Voulez-vous un epitech_header Epitech pour vos fichiers ?",
            "lib": "Voulez-vous un dossier lib and et un fichier lib.h ?"
        },
        "answers": {
            "yes": "Oui",
            "no": "Non",
            "custom": "Personnalisé",
            "classic": "Classique"
        },
        "errors": {
            "binary_name": "Veuillez entrer un nom de fichier binaire valide, vous ne pouvez pas le laisser vide."
        }
    }
}

# ! FILE / DIRECTORY NAME :

GITIGNORE_FILENAME = ".gitignore"
MAKEFILE_FILENAME = "Makefile"
MAIN_FILENAME = "main.c"

DIRECTORY_NAMES = ['include', 'src', 'lib', 'tests']


INCLUDE_PATH = "include/"

test_makefile = f"tests/{MAKEFILE_FILENAME}"

header_file = INCLUDE_PATH + directory_name + ".h"

header_lib_file = f"{INCLUDE_PATH}lib.h"

# ! CONTENT :

MAIN_CONTENT = "\n#include <stdio.h>\n\nint main(__attribute__((unused)) int argc, __attribute__((unused)) char const * argv[])\n{\n\tprintf(\"Hello, World!\\n\");\n\treturn 0;\n}"

GITIGNORE_CONTENT = """
# Prerequisites
*.d

# Object files
*.o
*.ko
*.obj
*.elf

# Linker output
*.ilk
*.map
*.exp

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe
*.out
*.app
*.i*86
*.x86_64
*.hex

# Debug files
*.dSYM/
*.su
*.idb
*.pdb

# Kernel Module Compile Results
*.mod*
*.cmd
.tmp_versions/
modules.order
Module.symvers
Mkfile.old
dkms.conf

# Binary files
"""

BASIC_HEADER_CONTENT = f"""\
/*
** EPITECH PROJECT, {current_year}
** {directory_name}
** File description:
** {MAIN_FILENAME}
*/
"""

TEST_RUN_CONTENT = f"""\
tests_run:\n\tmake -C tests all
"""

CLEAN_RULE_CONTENT = f"""\
\tmake -C tests fclean
"""

WILDCARD_LIB_CONTENT = f"""\
$(wildcard lib/*.c) \\"""

HEADER_MAKEFILE_CONTENT = f"""\
##
## EPITECH PROJECT, {current_year}
## {directory_name}
## File description:
## {MAKEFILE_FILENAME}
##
"""

# ! LANGUAGES and TRANSLATIONS:

def get_language():
    return locale.getdefaultlocale()[0][:2]


LANGUAGE = "french" if get_language() == "fr" else "english"

# ! PROMPT FUNCTIONS :


def ask_question(question_key, default="Yes"):
    return inquirer.select(
        message=TRANSLATION_DATA[LANGUAGE]['questions'][question_key],
        choices=[
            Choice(True, name=TRANSLATION_DATA[LANGUAGE]['answers']["yes"]),
            Choice(False, name=TRANSLATION_DATA[LANGUAGE]['answers']["no"]),
        ],
        default=default,
    ).execute()


def ask_for_epitech_header():
    return ask_question("epitech_header")


def ask_for_custom_init():
    is_custom_init = inquirer.select(
        message=TRANSLATION_DATA[LANGUAGE]['questions']["custom_init"],
        choices=[
            Choice("Classical",
                   name=TRANSLATION_DATA[LANGUAGE]['answers']["classic"]),
            Choice(
                "Custom", name=TRANSLATION_DATA[LANGUAGE]['answers']["custom"]),
        ],
        default="Classical",
    ).execute()
    return is_custom_init == "Custom"


def ask_for_unit_tests():
    return ask_question("unit_tests")


def ask_for_lib():
    return ask_question("lib")

# ! FILE CREATION FUNCTIONS :

def create_makefile(binary_name, is_epitech_header, is_unit_tests, is_lib):
    root_makefile_content = f"""{HEADER_MAKEFILE_CONTENT if is_epitech_header else ""}
CC ?=gcc
RM = rm -f

NAME =  {binary_name}
SRCS = $(wildcard *.c) \\
       {WILDCARD_LIB_CONTENT if is_lib else ""}
       $(wildcard src/*.c) \\

OBJS = $(SRCS:.c=.o)
DEPS = $(OBJS:.o=.d)

CFLAGS += -Wall -Wextra -I include -g3

all: $(NAME)

$(NAME): $(OBJS)
\t$(CC) $(CFLAGS) -o $(NAME) $(OBJS)

-include $(DEPS)

%.o: %.c
\t$(CC) $(CFLAGS) -MMD -c $< -o $@

clean:
\t$(RM) $(OBJS)
\t$(RM) $(DEPS)
{CLEAN_RULE_CONTENT if is_unit_tests else ""}

fclean: clean
\t$(RM) $(NAME)
\t$(RM) $(wildcard vgcore*)

re: fclean all

{TEST_RUN_CONTENT if is_unit_tests else ""}

.PHONY: all clean fclean re tests_run
"""

    with open(MAKEFILE_FILENAME, "w") as makefile:
        makefile.write(root_makefile_content)


def create_test_makefile(is_epitech_header):
    test_makefile_content = f"""{HEADER_MAKEFILE_CONTENT if is_epitech_header else ""}
CC			=	gcc --coverage -g3 -I ../include

RM			= 	rm -f

TARGET		=	unit-tests

SRCS		=	$(wildcard *.c)		\\
				$(wildcard ../lib/*.c)		\\
				$(wildcard ../src/*.c)		\\

SRCS := $(filter-out ../main.c $(SRCS))


OBJ			= 	$(SRCS:.c=.o)


CFLAGS		= 	-Wall -Wextra


all			:	$(TARGET)
			./$(TARGET)


$(TARGET)	:	$(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ) -lcriterion


clean		:
			$(RM) $(OBJ)


fclean		:	clean
            $(RM) $(TARGET)
			$(RM) $(wildcard ../lib/*.gcno)
            $(RM) $(wildcard ../lib/*.gcda)
			$(RM) $(wildcard ../src/*.gcno)
            $(RM) $(wildcard ../src/*.gcda)
            $(RM) $(wildcard *.gcno)
            $(RM) $(wildcard *.gcda)

re			:	fclean all

.PHONY: all clean fclean re
"""

    with open(test_makefile, "w") as makefile:
        makefile.write(test_makefile_content)


def create_gitignore(binary_name):
    with open(GITIGNORE_FILENAME, "w") as gitignore:
        gitignore.write(GITIGNORE_CONTENT + binary_name)


def create_directories(is_unit_tests, is_lib):
    for directory in DIRECTORY_NAMES:
        if not os.path.exists(directory):
            if directory == "tests" and not is_unit_tests:
                continue
            if directory == "lib" and not is_lib:
                continue
            os.mkdir(directory)


def create_main_filename(is_epitech_header):
    with open(MAIN_FILENAME, "w") as file:
        if is_epitech_header:
            file.write(BASIC_HEADER_CONTENT)
        file.write(MAIN_CONTENT)


def create_header_file(is_epitech_header, is_lib):
    with open(header_file, "w") as file:
        if is_epitech_header:
            file.write(BASIC_HEADER_CONTENT)
        file.write(
            f"\n#ifndef {directory_name.upper()}_H\n\t#define {directory_name.upper()}_H\n\n\n\n#endif")

    if not is_lib:
        return

    with open(header_lib_file, "w") as lib_file:
        if is_epitech_header:
            lib_file.write(BASIC_HEADER_CONTENT)
        lib_file.write(
            f"\n#ifndef _LIB_H\n\t#define _LIB_H\n\n\n\n#endif")

# ! INIT FUNCTIONS :

def custom_init(binary_name):
    is_epitech_header = ask_for_epitech_header()
    is_unit_tests = ask_for_unit_tests()
    is_lib = ask_for_lib()
    create_main_filename(is_epitech_header)
    create_directories(is_unit_tests, is_lib)
    create_makefile(binary_name, is_epitech_header, is_unit_tests, is_lib)
    if is_unit_tests:
        create_test_makefile(is_epitech_header)
    create_header_file(is_epitech_header, is_lib)


def classic_init(binary_name):
    create_directories(True, True)
    create_makefile(binary_name, True, True, True)
    create_test_makefile(True)
    create_header_file(True, True)
    create_main_filename(True)

# ! MAIN :

def main():
    binary_name = inquirer.text(
        message=TRANSLATION_DATA[LANGUAGE]['questions']["binary_name"],
        validate=lambda binary_name: len(binary_name) > 0,
        invalid_message=TRANSLATION_DATA[LANGUAGE]['errors']["binary_name"],
    ).execute()

    create_gitignore(binary_name)

    if ask_for_custom_init():
        custom_init(binary_name)
    else:
        classic_init(binary_name)


if __name__ == "__main__":
    main()
