import json
import yaml
with open('covid_cases.json', 'r') as json_file:
    ourjson = json.load(json_file)
print(ourjson)
print("dateRep {}".format(ourjson['dateRep']))
print("countriesandTerritories {}".format(ourjson['countriesandTerritories']))
print("cases {}".format(ourjson['cases']))
print("deaths {}".format(ourjson['deaths']))
print("\n\n---")
print(yaml.dump)(ourjson)
