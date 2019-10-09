#! usr/bin/python3.7
# -*- coding: utf-8 -*-

import csv # importation du module

csvFile = open('tournagesdefilmsparis2011.csv', 'r')
xmlData = open('donnees_xml.xml', 'w')

csvData = csv.reader(csvFile, delimiter=';')
xmlData.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")
xmlData.write('<!DOCTYPE tournage SYSTEM "devoir_1.dtd">' + "\n\n")
xmlData.write('<tournage>' + '\n')

data = []

for row in csvData:
    if row != 1:
        data.append(row)
csvFile.close

def convert_row(row):
    return """      <film>
        <Titre>%s</Titre>
        <Realisateur>%s</Realisateur>
        <Adresse arrondissement="%s">%s</Adresse>
        <Organisme_Demandeur>%s</Organisme_Demandeur>
        <Type_tournage>%s</Type_tournage>
        <Date_debut>%s</Date_debut>
        <Date_fin>%s</Date_fin>
        <xy>%s</xy>
      </film>"""% (row[0], row[1],row[5], row[2], row[3], row[4], row[6], row[7],row[8])
    
# print('\n'.join([convert_row(row) for row in data[1:]]))
xmlData.write('\n'.join([convert_row(row) for row in data[1:]]))

xmlData.write('\n</tournage>')

xmlData.close()    
