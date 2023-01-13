# Generates a readme file template
import os


def generate_folder_table():
    files = [f"[{file}](./{file})" for file in os.listdir('.')]
    files = list(filter(lambda file: not file.find("readme") != -1, files))
    length = max([len(number) for number in files])
    # print(files)
    table =  "| " + "Item".center(length) +" |  Description  |\n"
    table += "|-" + "".center(length, "-") +"-|---------------|\n"
    for file in files:
        table += "| " + file.ljust(length) + " |               |\n"
    return table


def snake_case_to_title(snake):
    return snake.replace("_", " ").title()


def save_safe(text):
    if os.path.exists("readme.md"):
        count = 1
        filename = f"readme_revision_{count}.md"
        while os.path.exists(filename):
            count += 1
            filename = f"readme_revision_{count}.md"
        file = open(filename, "x")
        file.write(text)
        file.close()
        print(f"Readme revision created: \"{filename}\"")
    else:
        file = open("readme.md", "x")
        file.write(text)
        file.close()
        print("Created readme.md file")


def main():
    print("Creating readme file...")
    text = "# " + snake_case_to_title(os.getcwd().split("/")[-1])
    text += "\n\n"
    text += "Add introduction here"
    text += "\n\n"
    text += "## Navigation"
    text += "\n\n"
    text += generate_folder_table()
    text += "\n\n"

    save_safe(text)


main()