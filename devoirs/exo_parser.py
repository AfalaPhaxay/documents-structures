#! usr/bin/python2
# -*- coding: utf-8 -*-

from lxml import etree


xmlfile = "../exo-parser/valery_ame-et-danse_1921.xml"

# Initialiser la lecture du fichier
tree = etree.parse(xmlfile)

# Le contenu en tant que string
# print(etree.tostring(tree))

# La racine
root = tree.getroot()
# print(root.tag)

TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
TEI = "{%s}" % TEI_NAMESPACE

# for element in root.iter(TEI + 'editionStmt'):
#     for child in element:
#         print(child.text)
#         edition = child.find('edition').text
#         print(edition)
        
for element in root.iter(TEI + 'edition'):
    print(element.text)
   
for element in root.iter(TEI + 'licence'): 
    print(element.get("tag"))

d= {}
for element in root.iter(TEI + 'label'):
    d[element.text] = d.get(element.text,0) + 1
    

max_speaker = sorted(d.items(), key=lambda x:x[1])
print(max_speaker)
print(max(d, key = d.get)

# # Ajouter un enfant
for element in root.iter(TEI + 'editionStmt'):
    child = etree.SubElement(element, "respStmt")
    sub_child1 = etree.SubElement(child, "name")
    sub_child1.text = "un texte"
    
for element in root.iter(TEI + 'signed'):
    for child in element:
        print(child.text.upper())
    

# # Ajouter un enfant
# text = etree.SubElement(root, "")
#text.text = "un texte"
#text.set("un-attribut", 'une-valeur')
