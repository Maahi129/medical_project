from pdf2image import  convert_from_path
import  pytesseract
import  util
from PIL import Image
from parser_prescription import  PrescriptionParser
from parser_patient_details import  PatientDetailsParser

POPPLER_PATH = r'C:\poppler-22.04.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(filepath, file_format):
    # extracting text from pdf file
    pages = convert_from_path(filepath,poppler_path = POPPLER_PATH)
    document_text = ''

    if len(pages)>0:
        page = pages[0]
        processed_image = util.preprocessing_image(page)
        text = pytesseract.image_to_string(processed_image, lang = 'eng')
        document_text = '\n' + text

    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid document format: {file_format}")
    return  extracted_data


if __name__ == '__main__':
    data = extract('../resources/patient_details/pd_1.pdf','patient_details')
    print(data)