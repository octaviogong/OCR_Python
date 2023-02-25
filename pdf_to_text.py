import fitz

documento_pdf = str(input())
documento_abierto = fitz.open(documento_pdf)
    
nombre_documento = documento_abierto.name[:-4]
salida_txt = open(nombre_documento+'.txt','wb')

for paginas in documento_abierto:
    texto = paginas.get_text().encode('utf8')
    salida_txt.write(texto)

salida_txt.close()

