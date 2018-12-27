# utilities
import sys, smtplib, datetime
from os import environ
from configs import path_to_storage
from application_logger import *


def save_reminder(rem_msg, rem_date, store_path):
	""" writing a new reminder to the storage file """
	with open(store_path, "a") as storage_f:
		reminder = rem_msg + "%%%" + rem_date
		storage_f.write(reminder + "\n")		


def send_reminder(content):
	""" sending off a reminder via email """
	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	email_content = 'Subject: %s\n\n' % (content)
	mail.login(environ['GM_User'], environ['GM_PW'])
	mail.sendmail(environ['GM_User'], environ['GM_User'], email_content) 
	mail.close()


def send_todays_reminders():
	""" sending off reminders that are to be sent today 
							& return those that remain to be sent """
	not_sent_yet = []
	with open(path_to_storage, "r") as storage_f:
		for each in storage_f:
			reminder = each.split("%%%")
			reminder_msg = reminder[0]
			reminder_date = reminder[1].replace("\n", "")

			if reminder_date == get_date():
				send_reminder(reminder_msg)
				logger.info("Reminder was sent.")
			else:
				not_sent_yet.append(each)
	return not_sent_yet


def get_date():
	""" getting the current date in the format in which the dates of reminders are set """
	date = datetime.datetime.today().strftime("%d.%m.%Y")
	# shorten year part of string from lets say 1.1.2019 to 1.1.19
	formatted_date = date.replace(date[-4:], date[-2:])
	return formatted_date


def check_py_version(no):
	""" checking which python version is being used 
			- in order to invoke correct python 2 or 3 code respectively """
	if sys.version_info[0] == no:
		return True
	else:
		return False
