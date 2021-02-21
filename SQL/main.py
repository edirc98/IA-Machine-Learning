#CDS Collection Aplication. 
from Service.SQL_Connector import Connector
from Models.Language import Language
from Repository.LanguageRepository import AdminLanguage

c = Connector()
aL = AdminLanguage(c)

listLanguages = aL.getLanguages()

for l in listLanguages:
    print(l)

#newLang = Language(0,"Mandarin")
#aL.createLanguage(newLang)