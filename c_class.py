import sys


def generate(name):
    print(f"Created file {name}")
    snake = name
    pascal = name.replace("_", " ").title().replace(" ", "")
    screaming_snake = snake.upper()
    header = f'''#ifndef {screaming_snake}_H
#define {screaming_snake}_H

#include <stdio.h>
#include <stdlib.h>

typedef struct {pascal} {pascal};
struct {pascal} {{
    
}};

{pascal} * new_{snake}();
void delete_{snake}({pascal} * {snake});

#endif //{screaming_snake}_H'''

    impl = f'''#include "{snake}.h"

{pascal} * new_{snake}() {{
    {pascal} * {snake} = malloc(sizeof({pascal}));
    return {snake};
}}

void delete_{snake}({pascal} * {snake}) {{
    free({snake});
}}
'''

    h = open(f"{snake}.h", 'x')
    h.write(header)
    h.close()

    im = open(f"{snake}.c", 'x')
    im.write(impl)
    im.close()


if len(sys.argv) < 2:
    print("Please enter a name of the class to create")
    exit(1)

classes = []
for i in range(1, len(sys.argv)):
    print(i)
    classes.append(sys.argv[i])

for c in classes:
    generate(c)
