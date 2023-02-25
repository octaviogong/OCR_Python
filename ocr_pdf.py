import ocrmypdf
#import fitz


if __name__ == '__main__':    
  


# documento_pdf = str(input())
# documento_abierto = fitz.open(documento_pdf)
    
# nombre_documento = documento_abierto.name

    def ocr(file_path,save_path):
        ocrmypdf.ocr(file_path,save_path)



    ocr('4.pdf', 'OCR_4.pdf')