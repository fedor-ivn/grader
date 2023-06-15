# specify the directory path
import os


def get_names(old_dirs):
    new_names = []
    for dir in old_dirs:
        dir = dir.split('''\\''')
        list_splitted = dir[len(dir) - 1].split('-')
        del list_splitted[0]
        name = ''
        for i in range(len(list_splitted)):
            name += list_splitted[i]
            if i != len(list_splitted) - 1:
                 name += '-'
        new_names.append(name)
    return new_names


def get_dirs(dir_paths, counter):
    dirs = []
    for dir_path in dir_paths:
        files_and_dirs = os.listdir(dir_path)
        for item in files_and_dirs:
            item_path = os.path.join(dir_path, item)
            if os.path.isdir(item_path):
                dirs.append(item_path)
    if counter == 0:
        return dirs
    else:
        return get_dirs(dirs, counter-1)
    

def create_links(dir_paths):
    
    old_dirs = get_dirs(dir_paths, 1)
    
    new_names = get_names(old_dirs)
    print(new_names)

    for i in range(len(old_dirs)):
        os.symlink(old_dirs[i], './tasks/' + new_names[i])

dir_paths = ['./checkers/01-introduction', './checkers/02-bash-programming']
create_links(dir_paths)