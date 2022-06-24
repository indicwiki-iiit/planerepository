import pandas as pd
import math
import ast
from jinja2 import Environment, FileSystemLoader

class RenderInfo:
    def render(self,dictionary):
        file_loader = FileSystemLoader('./')
        env = Environment(loader=file_loader)
        template = env.get_template('./templates/info.j2')
        origin = dictionary['National origin']
        origin = self.get_literal(origin)
        if (origin == "nan"):
            origin = ""
        else:
            origin = dictionary['జాతీయ మూలం']

        designer = dictionary['Designer']
        #print(designer)
        #designer = self.get_eval(designer)
        print('designer',type(designer))

        if type(designer) == float:
            designer = ""
        else :
            designer = dictionary['డిజైనర్']

        introduction = dictionary['Introduction']
        print('introduction', type(introduction))

        if type(introduction) == float and math.isnan(introduction):
            introduction = ""
        else:
            introduction = int(introduction)

        print('introduction', introduction)
        print('introduction', type(introduction))

        retired = dictionary['Retired']
        if type(retired) == float and math.isnan(retired):
            retired = ""
        else:
            retired = int(retired)

        glob = {'name': dictionary["పేరు"], 'img': dictionary['img'],
        'role': dictionary['పాత్ర'], 'origin': origin, 'manufacturer' : dictionary['తయారీదారు'], 'designer':designer,
        'first_flight': dictionary['First flight'], 'built':dictionary['Number built'], 'introduction': introduction, 'retired':retired  }
        if 'type' in dictionary:
            glob['type']= dictionary['type']
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