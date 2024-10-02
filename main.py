import PyPDF2
from pathlib import Path
from typing import Optional, Union
import logging

# Configure logging
logging.basicConfig(
    filename='logfile.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class MyPdfHandler:
    def __init__(self, path: Union[str, Path]):
        self.path = Path(path)
        if not self.path.exists():
            raise FileNotFoundError(f"The file {self.path} does not exist.")
        if not self.path.is_file():
            raise ValueError(f"The path {self.path} is not a file.")
        self.rpath = self.path.parent
        logging.info(f"Initialized MyPdfHandler with path: {self.path}")

    def __str__(self):
        return f"MyPdfHandler managing the file: {self.path}"

    def __repr__(self):
        return f"MyPdfHandler(path={self.path})"

    def __len__(self):
        return len(self.path.name)

    def __call__(self):
        return (
            "MyPdfHandler is ready to manipulate PDF files. "
            "Available methods: read_metadata(), write_metadata(), merge_pdfs(), "
            "encrypt_pdf(), decrypt_pdf(), extract_text(), split_pdf(), "
            "add_password(), remove_password()"
        )

    def __hash__(self):
        return hash(self.path)

    def read_metadata(self) -> Optional[dict]:
        """Reads and prints the PDF metadata."""
        try:
            reader = PyPDF2.PdfReader(self.path)
            meta = reader.metadata
            metadata = {
                "Pages": len(reader.pages),
                "Author": meta.author,
                "Creator": meta.creator,
                "Producer": meta.producer,
                "Subject": meta.subject,
                "Title": meta.title
            }
            logging.info("PDF Metadata:")
            for key, value in metadata.items():
                logging.info(f"{key}: {value}")
            return metadata
        except Exception as e:
            logging.error(f"Failed to read metadata: {e}")
            return None

    def write_metadata(self, output_filename: str, **metadata) -> None:
        """Writes custom metadata to a new PDF file."""
        try:
            reader = PyPDF2.PdfReader(self.path)
            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.add_metadata(metadata)
            output_path = self.rpath / output_filename
            with open(output_path, "wb") as f:
                writer.write(f)
            logging.info(f"Metadata written to {output_path}")
        except Exception as e:
            logging.error(f"Failed to write metadata: {e}")

    def merge_pdfs(self, *other_pdfs: Union[str, Path], output_filename: str = "merged.pdf") -> None:
        """Merges multiple PDF files into a single PDF."""
        try:
            merger = PyPDF2.PdfMerger()
            merger.append(str(self.path))
            logging.info(f"Added {self.path} to merger.")
            for pdf in other_pdfs:
                pdf_path = Path(pdf)
                if not pdf_path.exists():
                    logging.warning(f"File {pdf_path} does not exist and will be skipped.")
                    continue
                merger.append(str(pdf_path))
                logging.info(f"Added {pdf_path} to merger.")
            output_path = self.rpath / output_filename
            merger.write(str(output_path))
            merger.close()
            logging.info(f"Merged PDF saved as {output_path}")
        except Exception as e:
            logging.error(f"Failed to merge PDFs: {e}")

    def extract_text(self, *page_numbers: int) -> None:
        """Extracts and prints text from specified pages."""
        try:
            reader = PyPDF2.PdfReader(self.path)
            for page_num in page_numbers:
                if page_num < 0 or page_num >= len(reader.pages):
                    logging.warning(f"Page number {page_num} is out of range.")
                    continue
                page = reader.pages[page_num]
                text = page.extract_text()
                logging.info(f"--- Text from page {page_num + 1} ---")
                print(text if text else "[No text found]")
        except Exception as e:
            logging.error(f"Failed to extract text: {e}")

    def encrypt_pdf(self, password: str, output_filename: str = "encrypted.pdf") -> None:
        """Encrypts the PDF with a password."""
        try:
            reader = PyPDF2.PdfReader(self.path)
            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.encrypt(password)
            output_path = self.rpath / output_filename
            with open(output_path, "wb") as f:
                writer.write(f)
            logging.info(f"Encrypted PDF saved as {output_path}")
        except Exception as e:
            logging.error(f"Failed to encrypt PDF: {e}")

    def decrypt_pdf(self, password: str, output_filename: str = "decrypted.pdf") -> None:
        """Decrypts the PDF using the provided password."""
        try:
            reader = PyPDF2.PdfReader(self.path)
            if not reader.is_encrypted:
                logging.info("The PDF is not encrypted.")
                return
            if not reader.decrypt(password):
                logging.error("Failed to decrypt PDF. Incorrect password.")
                return
            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            output_path = self.rpath / output_filename
            with open(output_path, "wb") as f:
                writer.write(f)
            logging.info(f"Decrypted PDF saved as {output_path}")
        except Exception as e:
            logging.error(f"Failed to decrypt PDF: {e}")

    def split_pdf(self, output_prefix: str = "split_page") -> None:
        """Splits the PDF into individual pages."""
        try:
            reader = PyPDF2.PdfReader(self.path)
            for i, page in enumerate(reader.pages):
                writer = PyPDF2.PdfWriter()
                writer.add_page(page)
                output_path = self.rpath / f"{output_prefix}_{i + 1}.pdf"
                with open(output_path, "wb") as f:
                    writer.write(f)
                logging.info(f"Saved page {i + 1} as {output_path}")
        except Exception as e:
            logging.error(f"Failed to split PDF: {e}")

    def add_password(self, password: str, output_filename: str = "protected.pdf") -> None:
        """Adds a password to the PDF."""
        self.encrypt_pdf(password, output_filename)

    def remove_password(self, password: str, output_filename: str = "unprotected.pdf") -> None:
        """Removes the password from the PDF."""
        self.decrypt_pdf(password, output_filename)


if __name__ == "__main__":
    try:
        pdf_handler = MyPdfHandler(r"D:/drylab.pdf")

        # This sample is to read metadata
        # pdf_metadata = pdf_handler.read_metadata()
        # print(pdf_metadata)

        # This sample is to write metadata
        # pdf_handler.write_metadata(title="mypdf2004", author="MBK")

        # This sample is to extract text from a PDF
        # pdf_handler.extract_text(1)

        # Add password to a PDF
        # pdf_handler.add_password("123456")

        # Remove password from a PDF if you know it
        # pdf_handler.remove_password("123456")

        # Split every page into a different PDF
        # pdf_handler.split_pdf()

        # this sample merges any given number of PDFs passed as a list
        # pdfs_to_merge = [r"D:/invoicesample.pdf", r"D:/somatosensory.pdf"]
        # pdf_handler.merge_pdfs(*pdfs_to_merge, output_filename="samples_merged.pdf")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
