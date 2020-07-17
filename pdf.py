import PyPDF2
import sys

input_file = sys.argv[1]
water_file = sys.argv[2]
output_file= sys.argv[3]


with open(input_file, "rb") as filehandle_input:
	pdf = PyPDF2.PdfFileReader(filehandle_input)
	pdf_writer = PyPDF2.PdfFileWriter()
	with open(water_file, "rb") as filehandle_watermark:
		watermark = PyPDF2.PdfFileReader(filehandle_watermark)
		for i in range(pdf.getNumPages()):
			first_page = pdf.getPage(i)
			first_page_watermark = watermark.getPage(0)
			first_page.mergePage(first_page_watermark)
			pdf_writer.addPage(first_page)
		
		with open(output_file, "wb") as filehandle_output:
			pdf_writer.write(filehandle_output)
