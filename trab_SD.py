# -*- coding: utf-8 -*-
"""
Created on Mon Oct 08 13:24:14 2018

@author: Leonardo
"""

#contagem de palavras de um pdf
import PyPDF2
import time
import threading

cont = ""
arquivo = open('Leonardo Venancio Correia - monografia (TCIC II).pdf', 'rb')
pdf = PyPDF2.PdfFileReader(arquivo)

#numero de páginas
numPag = pdf.getNumPages()
print("Número de páginas:", numPag)

"""
#para extração de texto
texto_pdf = pdf.getPage(0).extractText()

# separa palavras pelo espaço
pg1 = texto_pdf.split(' ')

print (pg1)

print (len(pg1))
"""

inicio = time.time() #início do cálculo de tempo

#interação por páginas
for i in range(0, numPag):
    #concatenar palavras em uma lista de página em página
    cont += pdf.getPage(i).extractText()

cont = cont.split(' ')

contPalavras = 0
for i in range(0, len(cont)):
    contPalavras += 1    
print (contPalavras)

#print (cont)

fim = time.time()
tempo = fim - inicio #tempo calculado
t1 = tempo

print ("\ntempo de processamento sem threads = ",(t1) , "segundos\n")

arquivo.close()

###############################################################################
#agora usando threads
cont = ""
arquivo = open('Leonardo Venancio Correia - monografia (TCIC II).pdf', 'rb')
pdf = PyPDF2.PdfFileReader(arquivo)

#numero de páginas
numPag = pdf.getNumPages()
print("Número de páginas:", numPag)

inicio = time.time() #início do cálculo de tempo

#interação por páginas
for i in range(0, numPag):
    #concatenar palavras em uma lista de página em página
    cont += pdf.getPage(i).extractText()

cont = cont.split(' ')


def contPalav():
    contPalavras = 0
    for i in range(0, len(cont)):
        contPalavras += 1
    print (contPalavras)

t = threading.Thread(target = contPalav)
t.start()        

#bloco de calculo de tempo
fim = time.time()
tempo = fim - inicio
t2 = tempo

print ("\ntempo de processamento com threads = ",(t2), "segundos\n")

arquivo.close()

#comparando os valores
if(t1 < t2):
    print("Tempo de contagem sem a utilização de Threads foi menor")
elif(t2 < t1):
    print("Tempo de contagem com a utilização de Threads foi menor")

tempo_diferenca = abs(t1-t2)
print ("\nDiferença = ",(tempo_diferenca), "segundos")
