from Bio import Entrez
Entrez.email = 'email@gmail.com'

#espell package
animals = ['Bos gaurus', 'Antelope cervicapra', 'Gazella bennettii', 'Boselaphus tragocamelus', 'Canis lupus', 'Panthera leo', 'Elephas maximus', 'Equus africanus', 'Panthera pardus', 'Cervus canadensis', 'Pavo cristatus', 'Grus leucogeranus', 'Vulpes vulpes', 'Rhinoceros unicornis', 'Panthera Tigris', 'Crocodylus palustris', 'Gavialis gangeticus', 'Equus caballus', 'Equus quagga', 'Babalus bubalis', 'Sus scrofa', 'Camelus dromedaries', 'Giraffa camelopardalis ', 'Hemidactylus flaviviridis', 'Hippopotamus amphibius', 'Macaca mulatta', 'Canis lupus', 'Felis domesticus', 'Acinonyx jubatus', 'Rattus rattus', 'Mus musculus', 'Oryctolagus cuniculus', 'Bubo virginianus', 'Passer domesticus', 'Corvus splendens', 'Acridotheres tristis', 'Psittacula eupatria', 'Molpastes cafer', 'Eudynamis scolopaccus', 'Columba livia', 'Naja naja', 'Ophiophagus hannah', 'Hydrophiinae ', 'Python molurus', 'Ptyas mucosa']

#clear all content in file
with open("correct-spell.txt", "w") as file:
  pass

with open("incorrect-spell.txt", "w") as file:
  pass

for animal in animals:
  recordTermSpells = Entrez.read(Entrez.espell(db='pmc', term=animal))
  recordTermId = Entrez.read(Entrez.esearch(db="Taxonomy", term=animal))

  lengthOfSpelledQuery = len(recordTermSpells["SpelledQuery"])
  lengthOfTermId = len(recordTermId["IdList"])

  if lengthOfTermId != 0: 
    recordCommonName = Entrez.read(Entrez.efetch(db="Taxonomy", id=recordTermId["IdList"][0], retmode="xml"))
    
    lengthOfName = len(recordCommonName)
    lengthOfCommonName = len(recordCommonName[0]['OtherNames']['CommonName'])

    if lengthOfName != 0 and lengthOfCommonName != 0:
      if lengthOfSpelledQuery == 0:
        with open("correct-spell.txt", "a") as file:
          file.write("Spell: " + recordTermSpells["Query"] + ", Common name: " + recordCommonName[0]['OtherNames']['CommonName'][0] + "\n")
      else:
        with open("incorrect-spell.txt", "a") as file:
          file.write("Spell: " + recordTermSpells["Query"] + ", Common name: " + recordCommonName[0]['OtherNames']['CommonName'][0] + "\n")
