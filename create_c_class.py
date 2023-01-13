import sys
import os.path

if len(sys.argv) < 2:
    print("\033[91mError\033[0m: Please enter a struct name")
    exit(1)

force = '-f' in sys.argv
struct_only = '-s' in sys.argv

if force:
    sys.argv.remove('-f')

if struct_only:
    sys.argv.remove("-s")

sys.argv.pop(0) # Removing the program argument

def create_file(struct_name):
    if ((os.path.isfile(f"{struct_name.lower()}.h") or os.path.isfile(f"{struct_name.lower()}.c")) and not force):
            print(f"\033[91mError\033[0m: File already exists for {struct_name.title()}")
            print("If this was intended, force the operation by adding -f")
            return
            # exit(1)

    c_head = f'''#ifndef {struct_name.upper()}_H
#define {struct_name.upper()}_H

#include <stdio.h>
#include <stdlib.h>

typedef struct {struct_name.title()} {struct_name.title()};
struct {struct_name.title()} {{
\t
}};

'''

    if not struct_only:
        c_head += f'''// Initializes a {struct_name.title()}
void init_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()});
        
// De-initializes a {struct_name.title()}
void deinit_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()});

// Allocates and initializes a new {struct_name.title()} on the heap
{struct_name.title()}* new_{struct_name.lower()}();

// Deletes the given {struct_name.title()}, calling deinit on it.
void delete_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()});

// Prompts the user via the terminal to initialize a {struct_name.title()}
void prompt_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()});

// Prints the given {struct_name.title()} to the terminal.
void print_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()});

// Loads a {struct_name.title()} given a filename
{struct_name.title()}* load_{struct_name.lower()}(char * filename);

// Save the given {struct_name.title()} to a file.
void save_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()}, char * filename);

'''

    c_head += "#endif"
    c_impl = f'#include "{struct_name.lower()}.h"'

    if not struct_only:
        c_impl += f'''

void init_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()}) {{
\t
}}

void deinit_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()}) {{
\t
}}
        
{struct_name.title()}* new_{struct_name.lower()}() {{
    {struct_name.title()}* {struct_name.lower()} = malloc(sizeof({struct_name.title()}));
    init_{struct_name.lower()}({struct_name.lower()});
    return {struct_name.lower()};
}}

void delete_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()}) {{
    deinit_{struct_name.lower()}({struct_name.lower()});
    free({struct_name.lower()});
}}

void prompt_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()}) {{
\t
}}

void print_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()}) {{
\t
}}

// Loads a {struct_name.title()} given a filename
{struct_name.title()}* load_{struct_name.lower()}(char * filename) {{
    {struct_name.title()}* {struct_name.lower()};
    FILE* fp;
    fp = fopen(filename, \"r\");
\t
    // Add logic to load a given struct;
\t
    fclose(fp);
    return {struct_name.lower()};
}}

// Save the given {struct_name.title()} to a file.
void save_{struct_name.lower()}({struct_name.title()}* {struct_name.lower()}, char * filename) {{
    FILE* fp;
    fp = fopen(filename, \"w\");
\t
    // Add logic to save a given struct;
\t
    fclose(fp);
}}
    '''

    head_file = open(f"{struct_name.lower()}.h", "w")
    impl_file = open(f"{struct_name.lower()}.c", "w")

    head_file.write(c_head)
    impl_file.write(c_impl)

    head_file.close()
    impl_file.close()

    print(f"  \033[96mCreated\033[0m new c 'class' named {struct_name.title()}")


for name in sys.argv:
    create_file(name)