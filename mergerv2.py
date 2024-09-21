import PyPDF2
import sys
import os

# * This version gives the option to merge the files in a different order than they are listed in the directory
# *! If the order is correct, use the other version


def do_validation(order):
    if len(order) == 0:
        print("No files selected. Exiting.")
        sys.exit()

    if len(order.split()) != len(files):
        print("You did not select the correct number of files. Exiting.")
        sys.exit()

    if len(set(order.split())) != len(order.split()):
        print("You have duplicate numbers. Exiting.")
        sys.exit()

    # if the order variable contains letters, then exit
    if not order.replace(" ", "").isnumeric():
        print("You have entered a non-numeric character. Exiting.")
        sys.exit()

    # if the order variable contains numbers that are not in the range of the files, then exit
    for number in order.split():
        if int(number) >= len(files):
            print("You have entered a number that is out of range. Exiting.")
            sys.exit()


def print_files_in_directory(directory, files):
    print("We see these files in the directory: ")
    for i, file in enumerate(os.listdir(directory)):
        if file.endswith(".pdf"):
            print(str(i)+") "+file)
            files.append(file)


def merge_in_new_order(merger, directory, files, newFileIndexOrder):
    for index in newFileIndexOrder.split():
        merger.append(directory+"\\"+files[int(index)])
    merger.write("combined.pdf")


if __name__ == "__main__":
    merger = PyPDF2.PdfMerger()
    directory = os.curdir+"\\pdfs_to_merge"
    files = []
    print_files_in_directory(directory, files)
    newFileIndexOrder = input(
        "Please enter the order of the files you want to merge (numbers separated by spaces): ")

    do_validation(newFileIndexOrder)
    merge_in_new_order(merger, directory, files, newFileIndexOrder)
    print("The files have been merged into combined.pdf")
    merger.close()
