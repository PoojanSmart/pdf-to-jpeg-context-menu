""" SINGLE FILE PROCESSING """

# IMPORTS
import os
import tempfile
import sys

from tqdm import tqdm
from pdf2image import convert_from_path

abs_pdf_path = sys.argv[1]

# OPENING THE GUI FILE PICKER
file_name = abs_pdf_path.split("\\")[-1]
dir_path = "\\".join(abs_pdf_path.split("\\")[:-1])
print(abs_pdf_path)
print(file_name)

# PRINTING SELECTED FILE NAME
if not file_name:
    print("\nError in opening the file")
    exit()
else:
    print("\nSelected file:", file_name)
    print("\nProcessing . . .")

# PROVIDING THE ABSOLUTE PATH FOR POPPLER
abs_poppler_path = "C:\\Tools\\_internal\\poppler\\bin"
print(abs_poppler_path)

# EXTRACTING THE IMAGES
page_number = 1

with tempfile.TemporaryDirectory() as path:
    pdf_images = convert_from_path(pdf_path=abs_pdf_path, poppler_path=abs_poppler_path, output_folder=path)
    print("\nTotal number of pages =", len(pdf_images),"\n")
    for page in tqdm(pdf_images):
        image_name = dir_path + "\\" + str(page_number) + '.jpg'
        page.save(image_name, 'JPEG')
        page_number += 1

"""
REQUIREMENTS:
    1. pdf2image -> pip install pdf2image
    2. tqdm -> pip install tqdm
"""
