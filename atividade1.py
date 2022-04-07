# Eduardo Vieira Marques Pereira do Valle
# Para executar o codigo necessita do arquivo cf79.xml na mesma pasta

import xml.sax
import xml.dom.minidom

autores = []
titulos = []

# O handler do SAX para autores
#<------ Inicio ------>
class AuthorHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name

    def characters(self, content):
        if self.current == "AUTHOR":
            self.autor = content

    def endElement(self, name):
        if self.current == "AUTHOR":
            autores.append(self.autor)
        self.current = ""
#<------ Fim ------>

# Trecho que executa o parser SAX no documento cf79.xml para encontrar autores
#<------ Inicio ------>
handler = AuthorHandler()
parser = xml.sax.make_parser()
parser.setContentHandler( handler )
parser.parse("cf79.xml")
#<------ Fim ------>

# Trecho que executa o parser DOM no documento cf79.xml para encontrar titulos
#<------ Inicio ------>
domtree = xml.dom.minidom.parse("cf79.xml")

file = domtree.documentElement

titles = file.getElementsByTagName("TITLE")

for title in titles:
    titulos.append(title.childNodes[0].nodeValue)
#<------ Fim ------>

# Escrita do documento autores.xml, dos autores encontrados pelo SAX
#<------ Inicio ------>
raiz = xml.dom.minidom.Document()
  
documentoXML = raiz.createElement('titulos') 
raiz.appendChild(documentoXML)
  
for titulo in titulos:
    tagNode = raiz.createElement('titulo')
    textNode = raiz.createTextNode(titulo)
    tagNode.appendChild(textNode)  
    documentoXML.appendChild(tagNode)
  
xml_str = raiz.toprettyxml(indent ="\t") 
  
with open("titulo.xml", "w+") as f:
    f.write(xml_str) 
#<------ Fim ------>

# Escrita do documento titulo.xml, dos titulos encontrados pelo DOM
#<------ Inicio ------>
raiz = xml.dom.minidom.Document()
  
documentoXML = raiz.createElement('autores') 
raiz.appendChild(documentoXML)
  
for autor in autores:
    tagNode = raiz.createElement('autor')
    textNode = raiz.createTextNode(autor)
    tagNode.appendChild(textNode)  
    documentoXML.appendChild(tagNode)
  
xml_str = raiz.toprettyxml(indent ="\t") 
  
with open("autores.xml", "w+") as f:
    f.write(xml_str) 
#<------ Fim ------>