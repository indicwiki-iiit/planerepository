import pandas as pd
import math
from Words import Words
from jinja2 import Environment, FileSystemLoader
class RenderLast:

    def __init__(self):
        exclude_words = []
        exclude_words.append('పేరు')
        exclude_words.append('Role')
        exclude_words.append('Description')
        exclude_words.append('Guns')
        exclude_words.append('Bombs')
        exclude_words.append('First flight')
        exclude_words.append('Issued bylink')
        exclude_words.append('Developed intolink')
        exclude_words.append('Developed fromlink')
        exclude_words.append('Successor programslink')
        exclude_words.append('Primary userlink')
        exclude_words.append('పాత్ర')
        exclude_words.append('Rolelink')
        exclude_words.append('Manufacturer')
        exclude_words.append('తయారీదారు')
        exclude_words.append('Manufacturerlink')
        exclude_words.append('Variants')
        exclude_words.append('Length')
        exclude_words.append('Width')
        exclude_words.append('Wingspan')
        exclude_words.append('Height')
        exclude_words.append('Typelink')
        exclude_words.append('Closedlink')
        exclude_words.append('Fatelink')
        exclude_words.append('Owners and operatorslink')
        exclude_words.append('Type')
        exclude_words.append('Coordinateslink')
        exclude_words.append('Preserved atlink')
        exclude_words.append('Wing area')
        exclude_words.append('Empty weight')
        exclude_words.append('Gross weight')
        exclude_words.append('Wing loading')
        exclude_words.append('First flightlink')
        exclude_words.append('Introductionlink')
        exclude_words.append('Retiredlink')
        exclude_words.append('Primary userslink')
        exclude_words.append('Powerplant')
        exclude_words.append('Introduction')
        exclude_words.append('Maximum speed')
        exclude_words.append('Cruise speed')
        exclude_words.append('National origin')
        exclude_words.append('జాతీయ మూలం')
        exclude_words.append('National originlink')
        exclude_words.append('Designer')
        exclude_words.append('Designerlink')
        exclude_words.append('Retired')
        exclude_words.append('డిజైనర్')
        exclude_words.append('Number built')
        exclude_words.append('Variantslink')
        exclude_words.append('Propellers')
        exclude_words.append('Description')
        exclude_words.append('వివరణ')
        self.exclude_words = exclude_words


    def filterTheDict(self, dictObj,glob):
        newDict = {}
        words = Words()
        # Iterate over all the items in dictionary
        for key, value in dictObj.items():
            if key not in glob and key not in self.exclude_words:
                if type(value) == float and not math.isnan(value):
                    key =  words.getWord(key)
                    newDict[key] = value
                elif type(value) == str and value != 'nan':
                    key =  words.getWord(key)
                    newDict[key] = value
        return newDict

    def render(self,dictionary, glob):
        file_loader = FileSystemLoader('./')
        env = Environment(loader=file_loader)
        template = env.get_template('./templates/last.j2')
        newDictionary = self.filterTheDict(dictionary,glob)
        #print(newDictionary)
        return template.render({'glob' : newDictionary}), newDictionary


if __name__ == "__main__":
    renderLast = RenderLast()
    df = pd.read_excel("output2.xlsx")
    for row in df.iterrows():
        print("#########row+++++++++++")
        dictionary = row[1].to_dict()
        tempt, glob = renderLast.render(dictionary,{'name':'asdf', 'img': '324234'})
        print(tempt)