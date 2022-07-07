class Words:

    def __init__(self):
        words = {}
        words['maximum speed'] = 'మాక్సిమం స్పీడ్'
        words['Service ceiling'] =  'సర్వీస్ సెయిలింగ్'
        words['Power/mass'] =  'పవర్/మాస్'
        words['Take-off Run'] =  'టేక్-ఆఫ్ రన్'
        words['Take-off distance to 50 ft (15 m)'] =  'టేక్డి-ఆఫ్స్టె డిస్టెన్స్ తో 50 ft (15 m)'
        words['Crew'] =  'క్రూ'
        words['Disc loading'] =  'డిస్క్ లోడింగ్'
        words['Blade tip speed'] =  'బ్లేడ్ టిప్ స్పీడ్'
        words['Blade section'] =  'బ్లేడ్ సెక్షన్'
        words['Main rotor area'] =  'మెయిన్ రోటర్ ఏరియా'
        words['Main rotor diameter'] =  'మెయిన్ రోటర్ దిమ్మెటర్'
        words['Absolute ceiling'] =  'అబ్సొల్యూట్ సెయిలింగ్'
        words['Landing Roll'] =  'లాండింగ్ రోల్'
        words['Minimum control speed'] =  'మినిమం కంట్రోల్ స్పీడ్'
        words['Developed into'] =  'డెవలప్డ్ ఇంటూ'
        words['Endurance'] =  'ఎండ్యూరన్స్'
        words['Status'] =  'ప్రస్తుత పరిస్థితి'
        words['Hardpoints'] =  'హార్డపోయింట్స్'
        words['Landing distance'] =  'లాండింగ్ డిస్టెన్స్'
        words['Payload with full fuel'] =  'పేలోడ్ విత్ ఫుల్ ఫ్యూయల్'
        words['Take off distance'] =  'టేక్ ఆఫ్ డిస్టెన్స్'
        words['Cabin length'] =  'కేబిన్ లెంగ్త్'
        words['Cabin width'] =  'కేబిన్ విడ్త్'
        words['Cabin Height'] =  'కేబిన్ హేఈఘ్ట్'
        words['Max Landing Weight'] =  'మాక్స్ లాండింగ్ వెయిట్'
        words['Max takeoff weight'] =  'మాక్స్ టేకాఫ్ వెయిట్'
        words['Range'] =  'రేంజ్'
        words['Produced'] =  'ఉత్పత్తి చేసిన సంవత్సరం'
        words['Developed from'] =  'డెవలప్డ్ ఫ్రమ్'
        words['Time to altitude'] =  'టైం తో ఆల్టిట్యుడ్'
        words['Stall speed'] =  'స్టాల్ స్పీడ్'
        words['Issued by'] =  'జారీ చేసారు'
        words['Successor programs'] =  'తదుపరి కార్యక్రమాలు'
        words['Fuel capacity'] =  'ఫ్యూయల్ కెపాసిటీ'
        words['Capacity'] =  'కెపాసిటీ'
        words['Owners and operators'] =  'ఓనర్స్ అండ్ ఒపేరాతోర్స్'
        words['Serial'] =  'సీరియల్'
        words['Construction number'] =  'కన్స్ట్రక్షన్ నెంబర్'
        words['Closed'] =  'క్లోస్డ్'
        words['Coordinates'] =  'కోఆర్డినెట్స్'
        words['Location'] =  'లొకేషన్'
        words['Organization'] =  'ఆర్గనైజషన్'
        words['In service'] =  'ఇన్ సర్వీస్'
        words['Other name(s)'] =  'ఇతర పేర్లు'
        words['Registration'] =  'రిజిస్ట్రేషన్'
        words['Fate'] =  'పరిస్థితి'
        words['Preserved at'] =  'మ్యూజియం'
        words['Rate of climb'] =  'రేట్ అఫ్ చ్లింబ్'
        words['Primary users'] =  'ప్రైమరీ యూజర్స్'
        words['Primary user'] =  'ప్రైమరీ యూజర్'
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