import pandas as pd
from jinja2 import Environment, FileSystemLoader

class RenderInfo:
    def render(self,_id):
        file_loader = FileSystemLoader('./')
        env = Environment(loader=file_loader)
        template = env.get_template('./templates/info.j2')
        #glob = {'get_profile_ref': get_profile_ref, 'get_source': get_source, 'conv': conv, 'is_valid_string': is_valid_string}
        #template.globals.update(glob)
        plane_DF = pd.DataFrame()
        plane_DF.fillna(value="nan", inplace=True)
        row = plane_DF['plane_id'] = _id
        print("str",type(row))
        return template.render({'plane_id': _id})

if __name__ == "__main__":
    renderInfo = RenderInfo()
    template = renderInfo.render('Akaflieg München Mü13')
    print(template)