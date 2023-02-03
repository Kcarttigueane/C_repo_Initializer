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

CLANG_TIDY_FILENAME = ".clang-tidy"
CLANG_FORMAT_FILENAME = ".clang-format"

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

CLANG_FORMAT_CONTENT = f"""\
Language: Cpp
BasedOnStyle: Google
AccessModifierOffset: -2
AlignAfterOpenBracket: Align
AlignConsecutiveAssignments: None
AlignOperands: Align
AllowAllArgumentsOnNextLine: true
AllowAllConstructorInitializersOnNextLine: true
AllowAllParametersOfDeclarationOnNextLine: false
AllowShortBlocksOnASingleLine: Empty
AllowShortCaseLabelsOnASingleLine: false
AllowShortFunctionsOnASingleLine: Inline
AllowShortIfStatementsOnASingleLine: Never # To avoid conflict, set this "Never" and each "if statement" should include brace when coding
AllowShortLambdasOnASingleLine: Inline
AllowShortLoopsOnASingleLine: false
AlwaysBreakAfterReturnType: None
AlwaysBreakTemplateDeclarations: Yes
BinPackArguments: true
BreakBeforeBraces: Custom
BraceWrapping:
  AfterFunction: true
  AfterCaseLabel: false
  AfterClass: false
  AfterStruct: false
  AfterControlStatement: Never
  AfterEnum: false
  AfterNamespace: false
  AfterUnion: false
  AfterExternBlock: false
  BeforeCatch: false
  BeforeElse: false
  BeforeLambdaBody: false
  IndentBraces: false
  SplitEmptyFunction: false
  SplitEmptyRecord: false
  SplitEmptyNamespace: false
BreakBeforeBinaryOperators: None
BreakBeforeTernaryOperators: true
BreakConstructorInitializers: BeforeColon
BreakInheritanceList: BeforeColon
ColumnLimit: 80
CompactNamespaces: false
ContinuationIndentWidth: 4
Cpp11BracedListStyle: true
DerivePointerAlignment: false # Make sure the * or & align on the left
EmptyLineBeforeAccessModifier: LogicalBlock
FixNamespaceComments: true
IncludeBlocks: Preserve
IndentCaseLabels: true
IndentWidth: 4
KeepEmptyLinesAtTheStartOfBlocks: true
MaxEmptyLinesToKeep: 1
NamespaceIndentation: None
ObjCSpaceAfterProperty: false
ObjCSpaceBeforeProtocolList: true
PointerAlignment: Left
ReflowComments: false
SeparateDefinitionBlocks: Always # Only support for clang-format 14
SpaceAfterCStyleCast: false
SpaceAfterLogicalNot: false
SpaceAfterTemplateKeyword: true
SpaceBeforeAssignmentOperators: true
SpaceBeforeCpp11BracedList: false
SpaceBeforeCtorInitializerColon: true
SpaceBeforeInheritanceColon: true
SpaceBeforeParens: ControlStatements
SpaceBeforeRangeBasedForLoopColon: true
SpaceBeforeSquareBrackets: false
SpaceInEmptyParentheses: false
SpacesBeforeTrailingComments: 2
SpacesInAngles: false
SpacesInCStyleCastParentheses: false
SpacesInContainerLiterals: false
SpacesInParentheses: false
SpacesInSquareBrackets: false
Standard: c++11
TabWidth: 4
UseTab: Never
IndentPPDirectives: AfterHash
"""

CLANG_TIDY_CONTENT = f"""\
# Generated from CLion Inspection settings
---
Checks: '-*,
bugprone-argument-comment,
bugprone-assert-side-effect,
bugprone-bad-signal-to-kill-thread,
bugprone-branch-clone,
bugprone-copy-constructor-init,
bugprone-dangling-handle,
bugprone-dynamic-static-initializers,
bugprone-fold-init-type,
bugprone-forward-declaration-namespace,
bugprone-forwarding-reference-overload,
bugprone-inaccurate-erase,
bugprone-incorrect-roundings,
bugprone-integer-division,
bugprone-lambda-function-name,
bugprone-macro-parentheses,
bugprone-macro-repeated-side-effects,
bugprone-misplaced-operator-in-strlen-in-alloc,
bugprone-misplaced-pointer-arithmetic-in-alloc,
bugprone-misplaced-widening-cast,
bugprone-move-forwarding-reference,
bugprone-multiple-statement-macro,
bugprone-no-escape,
bugprone-not-null-terminated-result,
bugprone-parent-virtual-call,
bugprone-posix-return,
bugprone-reserved-identifier,
bugprone-sizeof-container,
bugprone-sizeof-expression,
bugprone-spuriously-wake-up-functions,
bugprone-string-constructor,
bugprone-string-integer-assignment,
bugprone-string-literal-with-embedded-nul,
bugprone-suspicious-enum-usage,
bugprone-suspicious-include,
bugprone-suspicious-memory-comparison,
bugprone-suspicious-memset-usage,
bugprone-suspicious-missing-comma,
bugprone-suspicious-semicolon,
bugprone-suspicious-string-compare,
bugprone-swapped-arguments,
bugprone-terminating-continue,
bugprone-throw-keyword-missing,
bugprone-too-small-loop-variable,
bugprone-undefined-memory-manipulation,
bugprone-undelegated-constructor,
bugprone-unhandled-self-assignment,
bugprone-unused-raii,
bugprone-unused-return-value,
bugprone-use-after-move,
bugprone-virtual-near-miss,
cert-dcl21-cpp,
cert-dcl58-cpp,
cert-err34-c,
cert-err52-cpp,
cert-err60-cpp,
cert-flp30-c,
cert-msc50-cpp,
cert-msc51-cpp,
cert-str34-c,
cppcoreguidelines-interfaces-global-init,
cppcoreguidelines-narrowing-conversions,
cppcoreguidelines-pro-type-member-init,
cppcoreguidelines-pro-type-static-cast-downcast,
cppcoreguidelines-slicing,
google-default-arguments,
google-explicit-constructor,
google-runtime-operator,
hicpp-exception-baseclass,
hicpp-multiway-paths-covered,
misc-misplaced-const,
misc-new-delete-overloads,
misc-no-recursion,
misc-non-copyable-objects,
misc-throw-by-value-catch-by-reference,
misc-unconventional-assign-operator,
misc-uniqueptr-reset-release,
modernize-avoid-bind,
modernize-concat-nested-namespaces,
modernize-deprecated-headers,
modernize-deprecated-ios-base-aliases,
modernize-loop-convert,
modernize-make-shared,
modernize-make-unique,
modernize-pass-by-value,
modernize-raw-string-literal,
modernize-redundant-void-arg,
modernize-replace-auto-ptr,
modernize-replace-disallow-copy-and-assign-macro,
modernize-replace-random-shuffle,
modernize-return-braced-init-list,
modernize-shrink-to-fit,
modernize-unary-static-assert,
modernize-use-auto,
modernize-use-bool-literals,
modernize-use-emplace,
modernize-use-equals-default,
modernize-use-equals-delete,
modernize-use-nodiscard,
modernize-use-noexcept,
modernize-use-nullptr,
modernize-use-override,
modernize-use-transparent-functors,
modernize-use-uncaught-exceptions,
mpi-buffer-deref,
mpi-type-mismatch,
openmp-use-default-none,
performance-faster-string-find,
performance-for-range-copy,
performance-implicit-conversion-in-loop,
performance-inefficient-algorithm,
performance-inefficient-string-concatenation,
performance-inefficient-vector-operation,
performance-move-const-arg,
performance-move-constructor-init,
performance-no-automatic-move,
performance-noexcept-move-constructor,
performance-trivially-destructible,
performance-type-promotion-in-math-fn,
performance-unnecessary-copy-initialization,
performance-unnecessary-value-param,
portability-simd-intrinsics,
readability-avoid-const-params-in-decls,
readability-const-return-type,
readability-container-size-empty,
readability-convert-member-functions-to-static,
readability-delete-null-pointer,
readability-deleted-default,
readability-inconsistent-declaration-parameter-name,
readability-make-member-function-const,
readability-misleading-indentation,
readability-misplaced-array-index,
readability-non-const-parameter,
readability-redundant-control-flow,
readability-redundant-declaration,
readability-redundant-function-ptr-dereference,
readability-redundant-smartptr-get,
readability-redundant-string-cstr,
readability-redundant-string-init,
readability-simplify-subscript-expr,
readability-static-accessed-through-instance,
readability-static-definition-in-anonymous-namespace,
readability-string-compare,
readability-uniqueptr-delete-release,
readability-use-anyofallof'
"""

# ! LANGUAGES and TRANSLATIONS:


def get_language():
    try:
        return locale.getdefaultlocale()[0][:2]
    except (TypeError, IndexError):
        return "en"


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

NAME = {binary_name}
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
CC\t=\tgcc --coverage -g3 -I ../include

RM\t=\trm -f

TARGET\t=\tunit-tests

SRCS\t=\t$(wildcard *.c) \\
\t\t\t$(wildcard ../lib/*.c) \\
\t\t\t$(wildcard ../src/*.c) \\

SRCS\t:=\t$(filter-out ../main.c, $(SRCS))


OB\t=\t$(SRCS:.c=.o)


CFLAGS\t=\t-Wall -Wextra


all\t:\t$(TARGET)
\t\t./$(TARGET)


$(TARGET)\t:\t$(OBJ)
\t$(CC) $(CFLAGS) -o $(TARGET) $(OBJ) -lcriterion


clean\t:
\t\t$(RM) $(OBJ)


fclean\t:\tclean
\t\t\t$(RM) $(TARGET)
\t\t\t$(RM) $(wildcard ../lib/*.gcno)
\t\t\t$(RM) $(wildcard ../lib/*.gcda)
\t\t\t$(RM) $(wildcard ../src/*.gcno)
\t\t\t$(RM) $(wildcard ../src/*.gcda)
\t\t\t$(RM) $(wildcard *.gcno)
\t\t\t$(RM) $(wildcard *.gcda)

re\t:\tfclean all

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
    if os.path.exists(MAIN_FILENAME):
        return

    with open(MAIN_FILENAME, "w") as file:
        if is_epitech_header:
            file.write(BASIC_HEADER_CONTENT)
        file.write(MAIN_CONTENT)


def create_header_file(is_epitech_header, is_lib):
    with open(header_file, "w") as file:
        if is_epitech_header:
            file.write(BASIC_HEADER_CONTENT)
        file.write("\n#pragma once")

    if not is_lib:
        return

    with open(header_lib_file, "w") as lib_file:
        if is_epitech_header:
            lib_file.write(BASIC_HEADER_CONTENT)
        lib_file.write("\n#pragma once")


def create_formatter_files():
    with open(CLANG_TIDY_FILENAME, "w") as file:
        file.write(CLANG_TIDY_CONTENT)

    with open(CLANG_FORMAT_FILENAME, "w") as file:
        file.write(CLANG_FORMAT_CONTENT)


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
    create_formatter_files()

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
