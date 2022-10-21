"""
FelipedelosH

replace Stranger characters and return txtA == txtB

"""
class WordsComparator:
    def __init__(self) -> None:
        pass

    def compare(self, txtA, txtB):
        txtA = self.cleanWord(txtA)
        txtB = self.cleanWord(txtA)
        return txtA == txtB

    def cleanWord(self, txt):
        txt = txt.lower()
        # Delete stranger characters
        for i in ['0','1','2','3','4','5','6','7','8','9','-',',','(provincia)','(estación de tren)','(',')','\'','.','_']:
            txt = txt.replace(i, '')
        # Replace
        dataReplace = [('á','a'),('é','e'),('í','i'),('ó','o'),('ú','u'),('ä','a'),('ë','e'),('ï','i'),('ö','o'),('ü','u'),('ñ','n')]
        for i in dataReplace:
            txt = txt.replace(i[0], i[1])
        
        return txt.strip()
