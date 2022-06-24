import pandas as pd
from render_info import RenderInfo
from render_description import RenderDescription
from infobox import InfoBox
from genXML import tewiki, writePage
class Render:

    def create_xml_file(self):
        columns = ['name']
        df = pd.read_excel("output2.xlsx")
        print(df.head())
        for row in df.iterrows():
            print("#########row+++++++++++")
            dictionary = row[1].to_dict()
            print(row[1].to_dict())
            infoBox = InfoBox()
            #file = infoBox.parse_image_filename(row[1]["name"])
            file = "abc"
            print(file)
            dictionary['img'] = file
            renderInfo = RenderInfo()
            template_info, glob = renderInfo.render(dictionary)
            print(glob)
            renderDescription = RenderDescription()
            template_description, glob =renderDescription.render_desc(dictionary, glob)
            print(template_description)
        file_name = "plane.xml"
        with open(file_name, 'w') as fobj:
            fobj.write(tewiki + '\n')


if __name__ == "__main__":
    render = Render()
    render.create_xml_file()
