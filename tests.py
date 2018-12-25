# selectively testing functionalities
import unittest
from utils import get_date
from email_rem import save_reminder, send_relevant_reminders
from configs import path_to_storage


class TestClass(unittest.TestCase):

	def test_get_date(self):
		date = get_date()
		# check length and composition of date string
		self.assertEqual(len(date), 8)
		parts_of_date = date.split(".")
		self.assertEqual(len(parts_of_date), 3)		
		for each in parts_of_date:
			self.assertTrue(each.isdigit() and len(each) == 2)

	# def test_save_reminder(self):
	# 	test_rem_msg = "this is the test reminder"
	# 	test_rem_date = "12.12.2012"
	# 	save_reminder(test_rem_msg, test_rem_date, path_to_storage)





if __name__ == "__main__":
	unittest.main(exit=False)
