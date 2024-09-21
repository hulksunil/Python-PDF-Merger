import PyPDF2
import sys
import os

# * This version merges the files in the order they are listed in the directory
# *! If you want to merge the files in a different order, use the other version

merger = PyPDF2.PdfMerger()

directory = os.curdir+"\\pdfs_to_merge"


for file in os.listdir(directory):
    if file.endswith(".pdf"):
        print(file)
        merger.append(directory+"\\"+file)
merger.write("combined.pdf")
