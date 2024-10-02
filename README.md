# PDF Manipulation Toolkit using PyPDF2
This repository provides a powerful Python-based toolkit for manipulating PDF files using the PyPDF2 library. It includes functionalities for merging multiple PDFs, reading and writing PDF metadata, extracting images from PDF pages, encrypting/decrypting PDFs, and reading text from specific pages. The toolkit is designed to simplify and automate PDF-related tasks.

## Features
- Merge PDFs:
      Combine multiple PDF files into a single PDF document.
- Read PDF Metadata:
      Retrieve important information such as the author, title, subject, and creator of a PDF.
- Write PDF Metadata:
      Add or modify metadata fields like author, title, subject, etc., in a PDF file.
- Extract Images:
      Extract images embedded in specific pages of a PDF document.
- Encrypt/Decrypt PDFs:
      Secure PDFs by adding password protection or decrypt encrypted PDFs.
- Read PDF Content:
      Extract and display text content from specified pages of a PDF.

## Prerequisites
- Python 3.x
- Install PyPDF2 library:
      "pip install pypdf2"

## Usage
1- Clone the repository to your local machine:
    "git clone https://github.com/Bilal-khan-1604/Python-PDF-Manipulaton-Toolkit-PyPDF2.git"
2- Import the MyPdfHandler class and use its methods for your PDF operations:
    """from MyPdfHandler import MyPdfHandler
       # Initialize with a PDF path
       pdf = MyPdfHandler(r"path\to\file.pdf")
       # Merge multiple PDFs into one
       pdf.MergePdf(r"path\to\file2.pdf", r"path\to\file3.pdf")
       # Read metadata from the PDF
       pdf.ReadPdfMetadata()
       # Encrypt the PDF
       pdf.EncryptPdf("password")"""

## Examples
### 1-Merging PDFs:
pdf = MyPdfHandler(r"path\to\file1.pdf")
pdf.MergePdf(r"path\to\file2.pdf", r"path\to\file3.pdf")
### 2-Reading PDF Metadata:
pdf = MyPdfHandler(r"path\to\file.pdf")
pdf.ReadPdfMetadata()
### 3-Encrypting a PDF:
pdf = MyPdfHandler(r"path\to\file.pdf")
pdf.EncryptPdf("securepassword")

## Future Enhancements
- Split PDFs into smaller files.
- Add watermarks to PDF pages.
- Rotate and crop pages.
- More robust image extraction
