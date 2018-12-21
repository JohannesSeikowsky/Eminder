# utilities
import smtplib, datetime
from os import environ

def send_reminder(reminder_msg):
	email_content = 'Subject: %s\n\n' % (reminder_msg)
	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	mail.login(environ['GM_User'], environ['GM_PW'])
	mail.sendmail(environ['GM_User'], environ['GM_User'], email_content) 
	mail.close()

def get_date():
	date = datetime.datetime.today().strftime("%d.%m.%Y")
	# shorten year part of string from lets say 1.1.2019 to 1.1.19
	formatted_date = date.replace(date[-4:], date[-2:])
	return formatted_date
