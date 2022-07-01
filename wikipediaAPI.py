import wikipediaapi

class WikiAPI:
    def print_sections(self, sections, level=0):
        for s in sections:
                print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text))
                self.print_sections(s.sections, level + 1)

    def getAPI(self):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page('Akaflieg München Mü13')
        print("Page - Exists: %s" % page_py.exists())
        print("Page - Title: %s" % page_py.title)

        print("Page - Summary: %s" % page_py.summary)
        #print("Page - Summary: %s" % page_py['References'])
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
            )

        p_wiki = wiki_wiki.page('Akaflieg München Mü13')
        print(p_wiki.text)

        self.print_sections(p_wiki.sections, 3)




if __name__ == "__main__":
    wikiAPI = WikiAPI()
    wikiAPI.getAPI()
