from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class JSON_Reader(BaseClass):

    @staticmethod
    def get_data_from_json(self, emailcontent):

        file = open(BaseClass.getFilePath(self, "\\test_data\\EmailDetails.json"), "r")
        x = file.read()
        finaldata = json.loads(x)
        print(finaldata[emailcontent])

        return finaldata[emailcontent]


