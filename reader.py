#!/usr/bin/env python3
# -*- coding: utf-

import smtplib
import imaplib
import email
from colorama import Fore
import getpass
import base64
import sys

'''
__project__ = "Girdle of Hypolita"
__author__ = "Emmanuel Ruaud"
__email__ = "eruaud@student.le-101.fr"
This 101 project will send an email to a specified address
'''
def get_text(msg):
	if msg.is_multipart():
		return get_text(msg.get_payload(0))
	else:
		return msg.get_payload(None, True)

def read_mail():
	try:
		data = []
		mail = imaplib.IMAP4_SSL("imap.yandex.com", 993)
		passwd = getpass.getpass(Fore.YELLOW + "type your password : ")
		mail.login("ewolfwood@yandex.com", passwd)
		mail.select("INBOX")
		for i in range(1, 3):
			result,data = mail.fetch(str(i), '(RFC822)')
			msg= email.message_from_bytes(data[0][1])
			print (Fore.YELLOW + "SUBJECT : " + msg["subject"])
			print (Fore.YELLOW + "FROM : " + msg["from"])
			print (Fore.WHITE + get_text(msg).decode("utf-8"))
	except:
		print ("Error")

if (len(sys.argv) == 1):
	read_mail()
else:
	print(Fore.YELLOW + "usage : python3 reader.py")
