class Words:

    def __init__(self):
        words = {}
        words['maximum speed'] = 'మాక్సిమం స్పీడ్'
        self.words  = words
    def getWord(self, text):
        if text in self.words:
            return self.words[text]
        else:
            return text


if __name__ == "__main__":
    words = Words()
    str = words.getWord('maximum speed')
    print(str)