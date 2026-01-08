import docx2pdf

def config():
    return {
        "name": "Docx to PDF Converter",
        "version": "1.1",
        "description": "Convert DOCX files to PDF using docx2pdf.",
        "dependencies": ["docx2pdf"],
        "input_extension": [".docx"],
        "output_extension": [".pdf"],
        "category": "file"
    }

def convert(input_file, output_file):
    try:
        if not output_file.lower().endswith(".pdf"):
            output_file += ".pdf"
        docx2pdf.convert(input_file, output_file)
        print("Conversion successful ✔")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")