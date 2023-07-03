import datetime
import win32com.client as win32
from utilities.BaseClass import BaseClass


def send_email_outlook():
        """
        This method is used to send email from Outlook. It uses JSON reader function to determine the Receiver, Body and
        Subject of the email ( ref EmailDetails.json file) and also attaches the allure report.

        Options are present to display the email / save the email / send the email.
        :return:
        """
        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')

        mailItem = olApp.CreateItem(0)
        mailItem.Subject = BaseClass.conf_data["email"]["Subject"] + " " + datetime.datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S")

        mailItem.BodyFormat = 1
        mailItem.Body = BaseClass.conf_data["email"]["Body"]
        mailItem.To = BaseClass.conf_data["email"]["To"]

        #print(BaseClass.getFilePath(self, "\\allure_report\\report.html"))
        #mailItem.Attachments.Add(BaseClass.getFilePath(self, "\\allure_report\\report.html"))

        mailItem.Display()
        # mailItem.Save()
        mailItem.Send()
