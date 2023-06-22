import datetime
import json
import smtplib
import os
import win32com.client as win32

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utilities.BaseClass import BaseClass
from utilities.JSONReader import JSON_Reader


class Test_SendEmail(BaseClass):

    def test_send_email_outlook(self):
        """
        This method is used to send email from Outlook. It uses JSON reader function to determine the Receiver, Body and
        Subject of the email ( ref EmailDetails.json file) and also attaches the allure report.

        Options are present to display the email / save the email / send the email.
        :return:
        """
        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')

        mailItem = olApp.CreateItem(0)
        mailItem.Subject = JSON_Reader.get_data_from_json(self, "Subject") + " " + datetime.datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S")

        mailItem.BodyFormat = 1
        mailItem.Body = JSON_Reader.get_data_from_json(self, "Body")
        mailItem.To = JSON_Reader.get_data_from_json(self, "To")

        print(BaseClass.getFilePath(self, "\\allure_report\\report.html"))
        mailItem.Attachments.Add(BaseClass.getFilePath(self, "\\allure_report\\report.html"))

        mailItem.Display()
        # mailItem.Save()
        mailItem.Send()
