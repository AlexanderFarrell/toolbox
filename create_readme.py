# Generates a readme file template
import os


def create_link_file(file):
    return f"[{file}](./{file})"



def generate_folder_table():
    files = [file for file in os.listdir('.')]
    files = list(filter(lambda file: not file.find("readme") != -1 and not file[0]== '.', files))

    length = max([len(create_link_file(number)) for number in files])
    descriptions = []
    for file in files:
        description = ""
        if file == "external":
            description = "External dependencies"
        if file == "CMakeLists.txt":
            description = "Compilation instructions"
        descriptions.append(description)

    length_d = max([len(number) for number in descriptions])
    # print(files)
    table =  "| " + "Item".center(length) +" | " + "Description".center(length_d) +  " |\n"
    table += "|-" + "".center(length, "-") +"-|-"+"".center(length_d, "-")+"-|\n"
    for index in range(len(files)):
        file = files[index]
        description = descriptions[index]
        table += "| " + create_link_file(file).ljust(length) + " | " + description.center(length_d) +" |\n"
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


def common_titles(name):
    if name.lower() == "src":
        return "Source Folder"
    return name

def main():
    print("Creating readme file...")
    text = "# " + common_titles(snake_case_to_title(os.getcwd().split("/")[-1]))
    text += "\n\n"
    text += "Add introduction here"
    text += "\n\n"
    text += "## Navigation"
    text += "\n\n"
    text += generate_folder_table()
    text += "\n\n"

    save_safe(text)


main()