from pdf2image import convert_from_path
import os
import pytesseract
import cv2 as cv
from os import remove  
from os import path

#PDF a imagen JPEG
poppler_path =  r"C:\Users\Octavio\Downloads\poppler-0.68.0\poppler-0.68.0\bin"
pdf_path = r"C:\OCR_Python\A0022.pdf"
saving_folder = r"C:\OCR_Python"

pages = convert_from_path(pdf_path = pdf_path, poppler_path = poppler_path) #size=(400, None)

            #Obtener el nombre del PDF
pdf_name = pdf_path[pdf_path.rfind("\\")+1:]

c = 1
for page in pages:
    img_name = f"{pdf_name[:-3]}jpeg"
    page.save(os.path.join(saving_folder,img_name),"JPEG") #Supported file formats are jpeg, png, tiff and ppm.
    c+=1


#Mejora de la nitidez de imagen

img_cv = cv.imread(img_name)

img_cv = cv.cvtColor(img_cv, cv.COLOR_RGB2GRAY)

adaptative = cv.adaptiveThreshold(img_cv,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,201,5)

cv.imwrite(f"{img_name}",adaptative)

#Eliminar
if path.exists(saving_folder+'\\'+img_name):
   remove(saving_folder+'\\'+img_name)
#Extracción del texto
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
texto = pytesseract.image_to_string(adaptative)
texto.remove("\n")

#Archivo txt de salida
salida_txt = open(f'{img_name[:-4]}'+'txt','w',)
salida_txt.write(texto)
salida_txt.close()

    #Buscar el folio en el txt
