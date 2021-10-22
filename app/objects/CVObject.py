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

    def completeCV(self):
        if not self.emailAdress:
            self.extractMails()
        if not self.phoneNumber:
            self.extractPhoneNumbers()

    def getBody(self):
        res = dict()
        self.completeCV()

        res["info"] = self.info
        res["emailAdress"] = self.emailAdress
        res["phoneNumber"] = self.phoneNumber

        return res

    def extractPhoneNumbers(self):
        phonenumbers = re.findall(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b", self.info)
        if len(phonenumbers) > 0:
            self.phoneNumber = phonenumbers[0]

    def extractMails(self):
        emails = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", self.info)

        if len(emails) == 1:
            self.emailAdress = emails[0]
        elif len(emails) > 1:
            for adr in emails:
                adrprefix = adr.split("@")[0]
                if '.' in adrprefix:
                    prefixComponents = adrprefix.split('.')
                    for component in prefixComponents:
                        if component in self.info:
                            self.emailAdress = adr
                if adrprefix in self.info:
                    self.emailAdress = adr
