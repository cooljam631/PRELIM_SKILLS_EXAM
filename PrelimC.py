import xml.etree.ElementTree as ET
import re

xml = ET.parse("covid_cases_xml.xml")
root = xml.getroot()
Daterep = []
Cases = []
Deaths = []
Countriesandterritories = []

for title in root.iter('dateRep'):
    Daterep.append(title.text)

for title in root.iter('countriesandterritories'):
    Countriesandterritories.append(title.text)

for title in root.iter('cases'):
    Cases.append(title.text)

for title in root.iter('deaths'):
    Deaths.append(title.text)

print(Daterep)
print(Countriesandterritories)
print(Cases)
print(Deaths)