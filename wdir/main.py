import os
import sys

def validate_args(args):
    if len(args) <= 1:
        raise '当前输入参数无效，请重新输入'
    origin_path = args[1]
    if not os.path.isdir(origin_path):
        raise '当前输入参数不是文件夹，请重新输入'


def get_files(args):
    files = os.listdir(args)
    return files

def get_all_file(files):
    res_files = []
    for file in files:
        if os.path.isdir(file):
            file_list = get_files(file)
            print(file_list)
            get_all_file(file_list)
        else:
            res_files.append(file)
    return res_files



if __name__ == "__main__":
    args = sys.argv
    validate_args(args)
    files = get_files(args[1])
    res = get_all_file(files)