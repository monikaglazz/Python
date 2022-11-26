# Few ways to compare two files

import filecmp
import difflib
import csv


# Compare Line by Line
def compare_files_line_by_line(file_name_1, file_name_2):
    try:
        file1 = open(file_name_1, 'r')
        file2 = open(file_name_2, 'r')
    except FileNotFoundError:
        print("At least one of files is not existing.")
        return 0

    file1_read = file1.readlines()
    file2_read = file2.readlines()

    for i in range(len(file1_read)):
        if file1_read[i] == file2_read[i]:
            print("Matching line: ", file1_read[i])

    file1.close()
    file2.close()


# Compare using filecmp Module
def compare_files_filecmp_module(file_name_1, file_name_2):
    try:
        compare = filecmp.cmp(file_name_1, file_name_2)
    except FileNotFoundError:
        print("At least one of files is not existing.")
        return 0

    if compare == True:
        print("Files are the same")
    else:
        print("Files are not the same")


# Compare using difflib Module
def compare_files_difflib_module(file_name_1, file_name_2):
    try:
        with open(file_name_1, 'r') as file1, open(file_name_2, 'r') as file2:
            file1_read = file1.readlines()
            file2_read = file2.readlines()

            differ = difflib.Differ()
            for x in differ.compare(file1_read, file2_read):
                if x[0] == ' ':
                    print("Matching line: ", x)
    except FileNotFoundError:
        print("At least one of files is not existing.")
        return 0


# Compare .csv files Line by Line
def compare_csv_line_by_line(file_name_1, file_name_2):
    try:
        file_1 = open(file_name_1)
        file_2 = open(file_name_2)
    except FileNotFoundError:
        print("At least one of files is not existing.")
        return 0

    file_1_read = csv.reader(file_1)
    file_2_read = csv.reader(file_2)

    file_1_list = [data for data in file_1_read]
    file_2_list = [data for data in file_2_read]

    for x in range(len(file_1_list)):
        if file_1_list[x] == file_2_list[x] and x != 0:
            print("Matching data: ", file_1_list[x])

    file_1.close()
    file_2.close()


f1 = "emails_A.txt"
f2 = "emails_B.txt"
f3 = "emails_C.txt"
f4 = "students_gpa_A.txt"
f5 = "students_gpa_B.txt"
f6 = "employees_A.csv"
f7 = "employees_B.csv"

compare_files_line_by_line(f1, f2)

compare_files_filecmp_module(f1, f2)
compare_files_filecmp_module(f1, f3)

compare_files_difflib_module(f4, f5)

compare_csv_line_by_line(f6, f7)
