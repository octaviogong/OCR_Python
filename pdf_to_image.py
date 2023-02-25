from pdf2image import convert_from_path
import os
from PIL import Image
import pytesseract
from PIL import ImageEnhance

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

poppler_path = r"C:\Users\Octavio\Downloads\poppler-0.68.0\poppler-0.68.0\bin"
pdf_path = r"C:\OCR_Python\HC JARAL\HC JARAL\MC\A0059.pdf"

pages = convert_from_path(pdf_path = pdf_path, poppler_path = poppler_path)

saving_folder = r"C:\OCR_Python"

c = 1
for page in pages:
    img_name = f"img{c}.jpeg"
    page.save(os.path.join(saving_folder,img_name),"JPEG")
    c+=1




im = Image.open(img_name)
curr_sharp = ImageEnhance.Sharpness(im)
new_sharp = 8.3
  
# Sharpness enhanced by a factor of 8.3
img_sharped = curr_sharp.enhance(new_sharp)
img_sharped.show()

texto = pytesseract.image_to_string(img_sharped)

salida_txt = open('img1.txt','w')
salida_txt.write(texto)
salida_txt.close()



