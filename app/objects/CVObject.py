import re


class CVObject():

    def __init__(self, info, id):
        # CONSTANT
        self.index = "cv_search"
        self.doc_type = 'cv'

        # META INFO
        self.id = id
        self.info = info

        # MINED DATA
        self.emailAdress = ""
        self.phoneNumber = ""
        self.variousURL = ""

    def completeCV(self):
        if not self.emailAdress:
            self.extractMails()
        if not self.phoneNumber:
            self.extractPhoneNumbers()
        if not self.variousURL:
            self.extractVariousURL()


    def getBody(self):
        res = dict()
        self.completeCV()

        res["info"] = self.info
        res["emailAdress"] = self.emailAdress
        res["phoneNumber"] = self.phoneNumber
        res["variousURL"] = self.variousURL

        return res

    def extractVariousURL(self):
        regexURL = r"(https?://[^\s]+)"
        URLs = re.findall(regexURL, self.info)
        if len(URLs) > 0:
            self.variousURL = URLs

    def extractPhoneNumbers(self):
        regexGeneralCase = r"\++\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}[-.\s]?\d{1,9}[-.\s]?\d{1,9}"
        regexSpecialCase = r"\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}[-.\s]?\d{1,9}[-.\s]?\d{1,9}"
        phonenumbers = re.findall(regexGeneralCase, self.info)
        if len(phonenumbers) > 0:
            self.phoneNumber = phonenumbers[0]
        else:
            tokenLines = self.info.split("\n")
            for line in tokenLines:
                if "phone" in line.lower():
                    phonenumbers = re.findall(regexSpecialCase, self.info)
                    if len(phonenumbers) > 0:
                        self.phoneNumber = phonenumbers[0]
                        break

    def extractMails(self):
        emails = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", self.info)

        if len(emails) == 1:
            self.emailAdress = emails[0]
        elif len(emails) > 1:
            print("cas cool")
            for adr in emails:
                adrprefix = adr.split("@")[0]
                if '.' in adrprefix:
                    prefixComponents = adrprefix.split('.')
                    for component in prefixComponents:
                        if component in self.info:
                            self.emailAdress = adr
                if adrprefix in self.info:
                    self.emailAdress = adr
