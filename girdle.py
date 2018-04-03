#!/usr/bin/env python3
# -*- coding: utf-

import smtplib
from email.message import EmailMessage
import sys
import os
from colorama import Fore
import getpass

'''
__project__ = "Girdle of Hypolita"
__author__ = "Emmanuel Ruaud"
__email__ = "eruaud@student.le-101.fr"
This 101 project will send an email to a specified address
'''

def main(filename, recipient):
	with open(filename) as fp:
		msg = EmailMessage()
		msg.set_content(fp.read())
	msg["Subject"] = "Girdle of Hypolita"
	msg["From"] = "ewolfwood@yandex.com"
	msg["To"] = recipient
	try:
		print (Fore.YELLOW + "Connecting to smtp.yandex.com...")
		s = smtplib.SMTP('smtp.yandex.com', 587)
		s.starttls()
		passwd = getpass.getpass(Fore.YELLOW + "type your password : ")
		s.login('ewolfwood@yandex.com', passwd)
		print (Fore.YELLOW + "Sending email to " + recipient + "...")
		s.send_message(msg)
		s.quit()
	except smtplib.SMTPException:
		print (Fore.RED + "Error: unable to send email")
	except ConnectionRefusedError:
		print (Fore.RED + "Error: unable to connect through SMTP")
	except:
		print (Fore.RED + "Error : An error occured")
	else:
		print (Fore.GREEN + "Your email has been successfully sent.")

if (len(sys.argv) == 3):
	main(sys.argv[1], sys.argv[2])
else:
	print(Fore.YELLOW + "usage : python3 girdle.py mail_file recipient_adress")
