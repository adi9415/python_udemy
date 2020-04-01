import PyPDF2
import sys

inputs = sys.argv[1:]

# Merging PDFs

def pdfCombiner(pdf_list):
	merger  = PyPDF2.PdfFileMerger()			# merges the pages one by one
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')

 pdfCombiner(inputs)

# Rotating the pages for PDF

with open('dummy.pdf', 'rb') as pdf:			# pdf has to be open in binary mode as to read it correctly
	#print(pdf)
	reader = PyPDF2.PdfFileReader(pdf)
	#print(reader.getPage(0))
	page = reader.getPage(0)
	#print(page.rotateClockwise(180))			 # not save till now
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page.rotateClockwise(180))
	with open('rotated.pdf','wb') as new_file:
		writer.write(new_file)

# Adding watermark to pdf

input_pdf = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(input_pdf.getNumPages()):
	page = input_pdf.getPage(i)
	page.mergePage(watermark.getPage(0))			# merges the page
	output.addPage(page)

	with open('watermark.pdf','wb') as wtr:
		output.write(wtr)