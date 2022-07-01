import pandas as pd
from render_info import RenderInfo
from render_description import RenderDescription
from render_data import RenderData
from render_last import RenderLast
from infobox import InfoBox
from genXML import tewiki, writePage
class Render:

    def generate_template(self, dictionary):
        infoBox = InfoBox()
        file = infoBox.parse_image_filename(dictionary["name"])
        #file = "abc"
        #print(file)
        dictionary['img'] = file
        renderInfo = RenderInfo()
        template_info, glob = renderInfo.render(dictionary)
        #print(template_info)
        renderDescription = RenderDescription()
        template_description, glob =renderDescription.render_desc(dictionary, glob)
        #print(template_description)
        renderData = RenderData()
        template_descriptionInfo, glob = renderData.render(dictionary, glob)
        #print(template_descriptionInfo)
        renderLast = RenderLast()
        template_last, glob = renderLast.render(dictionary, glob)
        #print(template_last)
        template = template_info + "\n" + template_description + "\n" + template_descriptionInfo + "\n" + template_last + "\n"
        print(template)
        return template

    def create_xml_file(self):
        df = pd.read_excel("output2.xlsx")
        print(df.head())
        for row in df.iterrows():
            print("#########row+++++++++++")
            dictionary = row[1].to_dict()
            template = generate_template(dictionary)
        file_name = "plane.xml"
        with open(file_name, 'w') as fobj:
            fobj.write(tewiki + '\n')


if __name__ == "__main__":
    render = Render()
    render.create_xml_file()
