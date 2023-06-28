import json

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class JSON_Reader(BaseClass):

    @staticmethod
    def get_data_from_json(emailcontent, filepath):
        """
        This method is used to read details from JSON file. JSON file contains project specific data.
        :param self:
        :param emailcontent:
        :return:
        """

        #file = open(BaseClass.getFilePath(self, "\\test_data\\EmailDetails.json"), "r")
        file = open(BaseClass.getFilePath(self, filepath), "r")
        x = file.read()
        finaldata = json.loads(x)
        print(finaldata[emailcontent])

        return finaldata[emailcontent]
