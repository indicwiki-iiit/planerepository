from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

class Translate:
    def translate(self, text):
        return transliterate(text, sanscript.IAST, sanscript.TELUGU)


if __name__ == "__main__":
    translate = Translate()
    str = translate.translate("Maximum speed")
    print(str)