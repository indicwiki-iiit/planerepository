import pandas as pd
from render import Render
from datetime import datetime
from hashlib import sha1
import string
import os
import math
import xml.etree.ElementTree as ET

class GenerateXML:
    def __init__(self):
        self.user_id ="Kmeeraj"
        self.username ="Meeraj Kanaparthi"
        self.article = ''
        self.tewiki = '''<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="te">
            <siteinfo>
                <sitename>tewiki</sitename>
                <dbname>indicwiki</dbname>
                <base>https://tewiki.iiit.ac.in/index.php/%E0%B0%AE%E0%B1%8A%E0%B0%A6%E0%B0%9F%E0%B0%BF_%E0%B0%AA%E0%B1%87%E0%B0%9C%E0%B1%80</base>
                <generator>MediaWiki 1.34.0</generator>
                <case>first-letter</case>
                <namespaces>
                    <namespace key="-2" case="first-letter">మీడియా</namespace>
                    <namespace key="-1" case="first-letter">ప్రత్యేక</namespace>
                    <namespace key="0" case="first-letter" />
                    <namespace key="1" case="first-letter">చర్చ</namespace>
                    <namespace key="2" case="first-letter">వాడుకరి</namespace>
                    <namespace key="3" case="first-letter">వాడుకరి చర్చ</namespace>
                    <namespace key="4" case="first-letter">Project</namespace>
                    <namespace key="5" case="first-letter">Project చర్చ</namespace>
                    <namespace key="6" case="first-letter">దస్త్రం</namespace>
                    <namespace key="7" case="first-letter">దస్త్రంపై చర్చ</namespace>
                    <namespace key="8" case="first-letter">మీడియావికీ</namespace>
                    <namespace key="9" case="first-letter">మీడియావికీ చర్చ</namespace>
                    <namespace key="10" case="first-letter">మూస</namespace>
                    <namespace key="11" case="first-letter">మూస చర్చ</namespace>
                    <namespace key="12" case="first-letter">సహాయం</namespace>
                    <namespace key="13" case="first-letter">సహాయం చర్చ</namespace>
                    <namespace key="14" case="first-letter">వర్గం</namespace>
                    <namespace key="15" case="first-letter">వర్గం చర్చ</namespace>
                    <namespace key="828" case="first-letter">మాడ్యూల్</namespace>
                    <namespace key="829" case="first-letter">మాడ్యూల్ చర్చ</namespace>
                    <namespace key="2300" case="first-letter">Gadget</namespace>
                    <namespace key="2301" case="first-letter">Gadget talk</namespace>
                    <namespace key="2302" case="case-sensitive">Gadget definition</namespace>
                    <namespace key="2303" case="case-sensitive">Gadget definition talk</namespace>
                    <namespace key="2600" case="first-letter">Topic</namespace>
                </namespaces>
            </siteinfo>\n'''

            # Global Variables

    def filterNan(self, dictObj):
        newDict = {}
        # Iterate over all the items in dictionary
        for key, value in dictObj.items():
            if type(value) == float and not math.isnan(value):
                newDict[key] = value
            elif type(value) == str and value != 'nan':
                newDict[key] = value
        return newDict

    def mergeFiles(self):
        dir_name = "result/planes/all/"
        out_xml =""
        for filename in os.listdir(dir_name):
            fullname = os.path.join(dir_name, filename)
            with open(fullname, 'r') as file:
                if ".xml" in fullname:
                    print(fullname)
                    data = file.read()
                    out_xml += data
        file_name = "result/planes/out/out.xml"
        with open(file_name, 'w') as fobj:
            fobj.write(self.tewiki + '\n')
            fobj.write(out_xml)
            fobj.write('</mediawiki>')

    def genFile(self):
        planeNo =3200
        current_page_id = (1000000 + planeNo * 10)
        df = pd.read_excel("output"+str(planeNo)+".xlsx")
        for row in df.iterrows():
            print("#########row+++++++++++")
            dictionary = self.filterNan(row[1].to_dict())
            rendering = Render()
            template = rendering.generate_template(dictionary)
            #file_name = "result/planes/"+str(planeNo)+"/"+dictionary['name']+".xml"
            file_name = "result/planes/all/"+dictionary['name']+".xml"
            file_exists = os.path.exists(file_name)
            if not file_exists:
                os.makedirs(os.path.dirname(file_name), exist_ok=True)
                with open(file_name, 'w') as fobj:
                    fobj.write(self.article + '\n')
                    self.writePage(current_page_id, dictionary['పేరు'], template, fobj)
                    #self.writeArticle(current_page_id, dictionary['పేరు'], template, fobj)
                    current_page_id += 1
                    #fobj.write('</mediawiki>')

    # Funtions to write page to file object
    def sha36(self, page_id):
        page_id = str(page_id).encode('utf-8')
        sha16 =sha1(page_id).hexdigest()
        sha10 =int(sha16, 16)

        chars =[]
        alphabets = string.digits +string.ascii_lowercase
        while sha10>0:
            sha10, r = divmod(sha10, 36)
            chars.append(alphabets[r])

        return ''.join(reversed(chars))

    def writeArticle(self, page_id, title, wikiText, fobj):
        fobj.write(wikiText)
        return

    def writePage(self, page_id, title, wikiText, fobj):
        pglen = len(wikiText)
        time =datetime.now().strftime("%Y-%m-%dT%H-%M-%SZ")
        curPage ='''\n\n
        <page>
            <title>''' +title +'''</title>
            <ns>0</ns>
            <id>''' +str(page_id) +'''</id>
            <revision>
                <id>''' +str(page_id) +'''</id>
                <timestamp>'''+time+'''</timestamp>
                <contributor>
                    <username>''' +self.username +'''</username>
                    <id>''' +self.user_id +'''</id>
                </contributor>
                <comment>xmlpage created</comment>
                <model>wikitext</model>
                <format>text/x-wiki</format>
                <text xml:space="preserve" bytes="''' +str(pglen) +'''">
                \n''' + wikiText+'''
                </text>
                <sha1>''' +self.sha36(page_id) +'''</sha1>
            </revision>
        </page>
        \n\n'''

        fobj.write(curPage)
        return

if __name__ == "__main__":
    generateXML = GenerateXML()
    #generateXML.genFile()
    generateXML.mergeFiles()