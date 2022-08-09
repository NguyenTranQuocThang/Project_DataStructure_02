## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
# print(os.listdir("./Project_DataStructure_02/problem2/testdir"))

# Let us check if this file is indeed a file!
# print(os.path.isfile("./ex.py"))

# Does the file end with .py?
# print("./ex.py".endswith(".py"))

directory = './Project_DataStructure_02/problem2/testdir'


def find_files(suffix, path):
    data = []
    list = os.listdir(path)
    data = loop_recursive(suffix, path, list)
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return data


def loop_recursive(suffix, path, list):
    if len(list) == 0:
        return []
    first_element = list[0]
    data = loop_recursive(suffix, path, list[1:])
    path_file = path + '/' + first_element
    if os.path.isfile(path_file):
        if path_file.endswith(suffix):
            data.append(path_file)
    else:
        new_data = find_files(suffix, path_file)
        data = data + new_data
    return data


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
# Test Case 1
print(find_files('c', directory))

# output conjecture
# ./Project_DataStructure_02/problem2/testdir/t1.c
# ./Project_DataStructure_02/problem2/testdir/subdir5/a.c
# ./Project_DataStructure_02/problem2/testdir/subdir3/subsubdir1/b.c
# ./Project_DataStructure_02/problem2/testdir/subdir1/a.c

# Test Case 2
print(find_files('h', directory))

# output conjecture
# ./Project_DataStructure_02/problem2/testdir/t1.h
# ./Project_DataStructure_02/problem2/testdir/subdir5/a.h
# ./Project_DataStructure_02/problem2/testdir/subdir3/subsubdir1/b.h
# ./Project_DataStructure_02/problem2/testdir/subdir1/a.h

# Test Case 3
print(find_files('', directory))

# output conjecture is all file
# ./testdir/subdir1/a.c
# ./testdir/subdir1/a.h
# ./testdir/subdir2/.gitkeep
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/subdir3/subsubdir1/b.h
# ./testdir/subdir4/.gitkeep
# ./testdir/subdir5/a.c
# ./testdir/subdir5/a.h
# ./testdir/t1.c
# ./testdir/t1.h
