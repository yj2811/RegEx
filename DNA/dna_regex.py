from re import *

dna = 'cgcgcATGcATGcgTGAcTAAcgTAGcgcgcgcgc'
dna = dna.lower()

#(?x) the very start of the regex to make the remainder of the regex free-spacing (spaces, tabs and newlines)

orfpat = r'(?x) (?= ( atg  (?: (?!tga|tag|taa) ... )*  (?:tga|tag|taa) ))'
s = findall(orfpat,dna)
if s:
     print (', '.join(s))