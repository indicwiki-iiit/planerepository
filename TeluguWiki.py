import wptools

class TeluguWiki:
    def parse_infobox(self):
        page = wptools.page('Akaflieg München Mü13').get_parse()
        print(page)
        infobox = page.data['infobox']
        ##print(infobox)
        parsetree = page.data['parsetree']
        #print(parsetree)
        #iwlinks = page.data['iwlinks']
        ##print(iwlinks)
        #wikitext = page.data['wikitext']
        ##print(wikitext)
        #wikidata = page.get_wikidata()
        #print(wikidata)

if __name__ == "__main__":
    infoBox = TeluguWiki()
    infoBox.parse_infobox()
