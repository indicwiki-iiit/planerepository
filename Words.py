class Words:

    def __init__(self):
        words = {}
        words['maximum speed'] = 'మాక్సిమం స్పీడ్'
        words['Service ceiling'] =  'సర్వీస్ సెయిలింగ్'
        words['Power/mass'] =  'పవర్ / మాస్'
        words['Crew'] =  'క్రూ'
        words['Range'] =  'రేంజ్'
        words['Fuel capacity'] =  'ఫ్యూయల్ కెపాసిటీ'
        words['Capacity'] =  'కెపాసిటీ'
        words['Rate of climb'] =  'రేట్ అఫ్ చ్లింబ్'
        words['Primary users'] =  'ప్రైమరీ ఉసెర్స్'
        words['Primary user'] =  'ప్రైమరీ ఉసెర్స్'
        words['Length de-rigged'] =  'లెంగ్త్ de-రిగడ్'
        words['Width de-rigged (without tailplane)'] =  'విడ్త్ (వితౌట్ టైల్ప్లానే) de-రిగడ్'
        words['Width de-rigged (with tailplane)'] =  'విడ్త్ (విత్ టైల్ప్లానే) de-రిగడ్'
        words['Height de-rigged'] =  'హేఈఘ్ట్ de-రిగడ్'
        words['Aspect ratio'] =  'అస్పెచ్త్ రేషియో'
        words['Airfoil'] =  'పఐర్ఫాయిల్'
        words['Never exceed speed'] =  'నెవెర్ ఎక్స్ఎడ్ స్పీడ్'
        words['g limits'] =  'జి లిమిట్స్'
        words['Maximum glide ratio'] =  'మాక్సిమం గ్లిడ్ రేషియో'
        words['Rate of sink'] =  'రేట్ అఫ్ సింక్'
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