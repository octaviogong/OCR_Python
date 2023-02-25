from pdf2image import convert_from_path
import os
import pytesseract
import cv2 as cv


#PDF a imagen JPEG
poppler_path = r"C:\Users\Octavio\Downloads\Release-23.01.0-0\poppler-23.01.0\Library\bin"
pdf_path = r"C:\OCR_Python\HC JARAL\HC JARAL\A0207.pdf"
saving_folder = r"C:\OCR_Python"

pages = convert_from_path(pdf_path = pdf_path, poppler_path = poppler_path)

c = 1
for page in pages:
    img_name = f"img{c}.jpeg"
    page.save(os.path.join(saving_folder,img_name),"JPEG")
    c+=1


#Mejora de la nitidez de imagen

img_cv = cv.imread(img_name)
img_cv = cv.cvtColor(img_cv, cv.COLOR_RGB2GRAY)

adaptative = cv.adaptiveThreshold(img_cv,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,201,5)

cv.imwrite("Adapt.jpeg",adaptative)

#Extracción del texto
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
texto = pytesseract.image_to_string(adaptative)

#Archivo txt de salida
salida_txt = open('img1.txt','w')
salida_txt.write(texto)
salida_txt.close()






