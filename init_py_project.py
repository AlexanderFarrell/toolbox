import sys
import os.path

create_venv = '-venv' in sys.argv
if create_venv:
    sys.argv.remove("-venv")

files = [
    "src/main.c",
    "doc/srs.md",
    "doc/sdd.md"
]

folders = [
    'doc',
    'src'
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
make_empty_file('src/main.py')

run = 'python3 src/main.py;'

if create_venv:
    os.system('python -m venv ./venv')


a = open("run.sh", 'w')
a.write(run)
a.close()