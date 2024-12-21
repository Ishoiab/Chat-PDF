import fitz  # type: ignore # PyMuPDF
doc = fitz.open("C:/Users/91738/Downloads/example.pdf")  # Provide the path to your PDF
page2_text = doc.load_page(1).get_text()  # Extract text from page 2
page6_text = doc.load_page(5).get_text()  # Extract text from page 6

import pdfplumber # type: ignore

# Open the PDF file using the 'with' statement to ensure it's properly managed
with pdfplumber.open("C:/Users/91738/Downloads/example.pdf") as pdf:
    # Extract text from Page 2
    page2 = pdf.pages[1]  # Page indexing starts from 0, so page 2 is index 1
    page6 = pdf.pages[5]  # Page 6 is index 5

    # Extract text from Page 6
    page2_text = page2.extract_text()
    page6_text = page6.extract_text()

# Print the extracted text
print("Page 2 Text:")
print(page2_text)

print("\nPage 6 Text:")
print(page6_text)
