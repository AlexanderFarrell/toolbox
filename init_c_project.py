import sys
import os.path

# if len(sys.argv) < 2:
#     print("\033[91mError\033[0m: Please enter a project name")
#     exit(1)

# project_name = sys.argv[1]

files = [
    "src/main.c",
    "doc/srs.md",
    "doc/sdd.md"
]

folders = [
    'doc',
    'dev',
    'src',
    'build'
]

for file in files:
    if os.path.isfile(file):
        print("\033[91mError\033[0m: Project already initialized")
        exit(1)
    

def make_empty_file(file):
    open(file, "w").close()

for folder in folders:
    os.mkdir(folder)

make_empty_file('doc/srs.md')
make_empty_file('doc/sdd.md')
make_empty_file('readme.md')

c_main = f'''#include <stdio.h>
#include <stdlib.h>

int main() {{
    printf("Hello world!\\n");
}}

'''

c_file = open("src/main.c", "w")
c_file.write(c_main)
c_file.close()

c_run = f'''gcc src/main.c -o build/out;
./build/out;

'''

run_file = open("run.sh", "w")
run_file.write(c_run)
run_file.close()

os.system("chmod +x run.sh")