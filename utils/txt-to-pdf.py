import os
from fpdf import FPDF

# Prompt the user to select the TXT file
txt_file = input("Enter the path to the TXT file: ")

# Open the TXT file and read its contents
with open(txt_file, "r") as f:
    text = f.read()

# Create a PDF object
pdf = FPDF()

# Add a new page to the PDF
pdf.add_page()

# Set the font and font size
pdf.set_font("Arial", size=12)

# Write the text from the TXT file to the PDF
pdf.cell(0, 10, txt=text, ln=1, align="L")

# Prompt the user to enter the path to save the PDF file
save_path = input("Enter the path to save the PDF file: ")

# Save the PDF to the specified path
pdf.output(name=save_path, dest='F').encode('latin1')

print("PDF file saved successfully at", save_path)
