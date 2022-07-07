import pandas as pd
import math
import ast
from jinja2 import Environment, FileSystemLoader

class RenderInfo:
    def render(self,dictionary):
        file_loader = FileSystemLoader('./')
        env = Environment(loader=file_loader)
        template = env.get_template('./templates/info.j2')
        origin = ""
        if 'National origin' in dictionary:
            origin = dictionary['National origin']
            origin = self.get_literal(origin)
            if (origin == "nan"):
                origin = ""
            else:
                origin = dictionary['జాతీయ మూలం']

        designer = ""
        if 'Designer' in dictionary:
            designer = dictionary['Designer']
            if type(designer) == float:
                designer = ""
            else :
                designer = dictionary['డిజైనర్']

        manufacturer=""
        if 'Manufacturer' in dictionary:
            designer = dictionary['Manufacturer']
            if type(designer) == float:
                manufacturer = ""
            else :
                manufacturer = dictionary['తయారీదారు']

        introduction = ""

        if 'Introduction' in dictionary:
            introduction = dictionary['Introduction']
            if type(introduction) == float:
                introduction = int(introduction)

        retired =""
        if 'Retired' in dictionary:
            retired = dictionary['Retired']
            if type(retired) == float:
                retired = int(retired)


        first_flight = ""
        if 'First flight' in dictionary:
            first_flight = dictionary['First flight']
            if type(retired) == float:
                first_flight = int(first_flight)

        built = ""
        if 'Number built' in dictionary:
            built = dictionary['Number built']

        role =""
        if 'పాత్ర' in dictionary:
            role = dictionary['పాత్ర']
        glob = {'name': dictionary["పేరు"], 'img': dictionary['img'],
        'role': role, 'origin': origin, 'manufacturer' : manufacturer, 'designer':designer,
        'first_flight': first_flight, 'built':built, 'introduction': introduction, 'retired':retired  }
        if 'type' in dictionary:
            glob['type']= dictionary['type']
        else:
            if 'Type' in dictionary:
                glob['type']= dictionary['Type']
            else:
                glob['type']= ""

        return template.render(glob), glob

    def get_literal(self, q):
        try:
            return ast.literal_eval(q)
        except:
            return 'nan'

    def get_eval(self, q):
        try:
            return eval(q)
        except:
            return 'nan'

if __name__ == "__main__":
    renderInfo = RenderInfo()
    template = renderInfo.render({name : 'Akaflieg München Mü13'})
    print(template)