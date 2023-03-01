from pdf2image import convert_from_path
import os
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

poppler_path = r"C:\Users\Octavio\Downloads\poppler-0.68.0\poppler-0.68.0\bin"
pdf_path = r"C:\OCR_Python\4.pdf"

pages = convert_from_path(pdf_path = pdf_path, poppler_path = poppler_path) #size=(900, None)

saving_folder = r"C:\OCR_Python"

c = 1
for page in pages:
    img_name = f"img{c}.jpeg"
    page.save(os.path.join(saving_folder,img_name),"jpeg")
    c+=1




im = Image.open(img_name)
im.show()

texto = pytesseract.image_to_string(im)

salida_txt = open('img1.txt','w')
salida_txt.write(texto)
salida_txt.close()



