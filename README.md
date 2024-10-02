# PDF Manipulation Toolkit using PyPDF2
This repository provides a powerful Python-based toolkit for manipulating PDF files using the PyPDF2 library. It includes functionalities for merging multiple PDFs, reading and writing PDF metadata, extracting images from PDF pages, encrypting/decrypting PDFs, and reading text from specific pages. The toolkit is designed to simplify and automate PDF-related tasks.

## Features
- Merge PDFs:
      <br/>&emsp;&emsp;Combine multiple PDF files into a single PDF document.<br/><br/>
- Read PDF Metadata:
      <br/>&emsp;&emsp;Retrieve important information such as the author, title, subject, and creator of a PDF.<br/><br/>
- Write PDF Metadata:
      <br/>&emsp;&emsp;Add or modify metadata fields like author, title, subject, etc., in a PDF file.<br/><br/>
- Extract Images:
      <br/>&emsp;&emsp;Extract images embedded in specific pages of a PDF document.<br/><br/>
- Encrypt/Decrypt PDFs:
      <br/>&emsp;&emsp;Secure PDFs by adding password protection or decrypt encrypted PDFs.<br/><br/>
- Read PDF Content:
      <br/>&emsp;&emsp;Extract and display text content from specified pages of a PDF.

## Prerequisites
- Python 3.x
- Install PyPDF2 library:
      "pip install pypdf2"

## Usage
1- Clone the repository to your local machine:
    "git clone https://github.com/Bilal-khan-1604/Python-PDF-Manipulaton-Toolkit-PyPDF2.git"
<br/><br/>
2- Import the MyPdfHandler class and use its methods for your PDF operations:
    <br/>&emsp;&emsp;"""from MyPdfHandler import MyPdfHandler
       <br/>&emsp;&emsp;&emsp;# Initialize with a PDF path
       <br/>&emsp;&emsp;&emsp;pdf = MyPdfHandler(r"path\to\file.pdf")
       <br/>&emsp;&emsp;&emsp;# Merge multiple PDFs into one
       <br/>&emsp;&emsp;&emsp;pdf.MergePdf(r"path\to\file2.pdf", r"path\to\file3.pdf")
       <br/>&emsp;&emsp;&emsp;# Read metadata from the PDF
       <br/>&emsp;&emsp;&emsp;pdf.ReadPdfMetadata()
       <br/>&emsp;&emsp;&emsp;# Encrypt the PDF
       <br/>&emsp;&emsp;&emsp;pdf.EncryptPdf("password")"""

## Examples
### 1-Merging PDFs:
pdf = MyPdfHandler(r"path\to\file1.pdf")
<br/>pdf.MergePdf(r"path\to\file2.pdf", r"path\to\file3.pdf")
### 2-Reading PDF Metadata:
pdf = MyPdfHandler(r"path\to\file.pdf")
<br/>pdf.ReadPdfMetadata()
### 3-Encrypting a PDF:
pdf = MyPdfHandler(r"path\to\file.pdf")
<br/>pdf.EncryptPdf("securepassword")

## Future Enhancements
- Split PDFs into smaller files.
- Add watermarks to PDF pages.
- Rotate and crop pages.
- More robust image extraction
