# specify the directory path
import os


def get_new_name(directory):
    full_name = directory.split("/")[-1]
    new_name = full_name[full_name.find("-") + 1 :]
    return new_name


def get_dirs(diriectory_path, counter):
    directories = []
    files_and_diriectories = os.listdir(diriectory_path)

    for item in files_and_diriectories:
        item_path = os.path.join(diriectory_path, item)
        if os.path.isdir(item_path):
            directories.append(item_path)

    if counter == 0:
        return directories
    else:
        return sum(
            [
                get_dirs(directory, counter - 1)
                for directory in directories
            ],
            [],
        )


def create_links(directory):
    old_directories = get_dirs(directory, 2)
    new_names = []
    for directory in old_directories:
        new_names.append(get_new_name(directory))

    for old_directory, new_name in zip(
        old_directories, new_names
    ):
        if os.path.exists(f"tasks/{new_name}"):
            print(f"Symlink {new_name} already exists!")
        else:
            os.symlink(old_directory, f"tasks/{new_name}")


create_links("checkers")
