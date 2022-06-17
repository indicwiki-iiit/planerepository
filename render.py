import pandas as pd
from genXML import tewiki, writePage
class Render:

    def create_xml_file(self):
        columns = ['name']
        df = pd.read_excel("output2.xlsx")
        print(df.head())
        for name in df.iterrows():
            print(name[1].to_dict())
        file_name = "plane.xml"
        with open(file_name, 'w') as fobj:
            fobj.write(tewiki + '\n')


if __name__ == "__main__":
    render = Render()
    render.create_xml_file()