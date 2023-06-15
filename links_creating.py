# specify the directory path
import os

dir_paths = ["./checkers/01-introduction", "./checkers/02-bash-programming"]


class TasksDirectory:
    def __init__(checkers_path="checkers", target_path="tasks"):
        pass


names = []
for dir_path in dir_paths:
    files_and_dirs = os.listdir(dir_path)

    for item in files_and_dirs:
        item_path = os.path.join(dir_path, item)

        if os.path.isdir(item_path):
            sub_files_and_dirs = os.listdir(item_path)

            for sub_item in sub_files_and_dirs:
                sub_item_path = os.path.join(item_path, sub_item)

                if os.path.isdir(sub_item_path):
                    splitted = str(sub_item).split("-")
                    name = ""
                    for i in range(len(splitted)):
                        if i != 0:
                            name += splitted[i]
                            if i != len(splitted) - 1:
                                name += "-"
                    names.append(name)


print(names)

# for folder_name in names:
#     if not os.path.exists('./tasks/' + folder_name):
#         os.makedirs('./tasks/' + folder_name)
#         print(f"Folder {folder_name} has been created successfully!")
#     else:
#         print(f"Folder {folder_name} already exists!")

counter = 0

for dir_path in dir_paths:
    files_and_dirs = os.listdir(dir_path)

    for item in files_and_dirs:
        item_path = os.path.join(dir_path, item)

        if os.path.isdir(item_path):
            sub_files_and_dirs = os.listdir(item_path)

            for sub_item in sub_files_and_dirs:
                sub_item_path = os.path.join(item_path, sub_item)

                if os.path.isdir(sub_item_path):
                    print(sub_item_path)
                    print(names[counter])
                    os.symlink(sub_item_path, "./tasks/" + names[counter])
                    counter += 1
