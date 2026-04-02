import os
from ast import List


def get_file_name(path:str) -> List[str]:
    full_file_name = []

    def get_current_file(path:str):
        all = os.listdir(path)
        for file in all:
            if os.path.isfile(os.path.join(path, file)):
                full_file_name.append(file)
            else:
                get_current_file(os.path.join(path, file))
    get_current_file(path)
    return full_file_name