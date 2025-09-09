from pyPDF import pdfWriter #type:ignore
import os

merger=pdfWriter()
files=[for file in file os.listdir() ,if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("Merged-pdf.pdf")    
merger.close()