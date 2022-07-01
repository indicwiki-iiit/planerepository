import wptools

class InfoBox:
    def parse_infobox(self):
        page = wptools.page('Akaflieg München Mü13').get_parse()
        print(page)
        infobox = page.data['infobox']
        ##print(infobox)
        parsetree = page.data['parsetree']
        print(parsetree)
        iwlinks = page.data['iwlinks']
        ##print(iwlinks)
        wikitext = page.data['wikitext']
        ##print(wikitext)

    def parse_image_filename(self, plane):
        page = wptools.page(plane).get_parse()
        #print(page)
        infobox = page.data['infobox']
        print(infobox)
        if infobox is not None and 'image' in infobox:
            return infobox['image']
        else:
            return ""


if __name__ == "__main__":
    infoBox = InfoBox()
    #infoBox.parse_infobox()
    file = infoBox.parse_image_filename('Akaflieg München Mü13')
    print(file)