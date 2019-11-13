#! usr/bin/python3.7
# -*- coding: utf-8 -*-

from lxml import etree

xmlfile = "../seance_03/Duchn-etiquetage.txt.xml"

# Initialiser la lecture du fichier
tree = etree.parse(xmlfile)

# Le contenu en tant que string
# print(etree.tostring(tree))

# La racine
root = tree.getroot()



# Extraire tous les déterminants
list_det =[]
for element in root.iter('element'):
    for child in element:
        if "DET" in child.text:
            list_det.append(element[2].text)
print(list_det)            
print('\n')

# Afficher les patrons DET - NOM
patron = []
i = 0
for element in root.iter('article'):
    for data in element:
        if element[i][0].text[0:3] == 'DET':
            if element[i+1][0].text == 'NOM':
                patron.append((element[i][2].text, element[i+1][2].text))
        i += 1

print(patron)
 
# Reconstruire les phrases
list = []
list2 = []
for element in root.iter('element'):
    if element[0].text != 'SENT':
         list.append(element[2].text)
    else:
        list.append(element[2].text)
        list2.append(list)
        list = []
        
for ph in list2:
    print(" ".join(ph))
 
# Transformer l'affichage en : token/lemme/pos
aff = []
for element in root.iter('element'):
    aff.append((element[2].text, element[1].text, element[0].text))
        
print('\n'.join(['{}/{}/{}'.format(elt[0], elt[1], elt[2]) for elt in aff]))




