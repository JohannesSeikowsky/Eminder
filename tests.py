# selectively testing functionalities
import unittest
from utils import get_date, save_reminder, send_todays_reminders 
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

		# to be added -
		# test for save_reminder and send_todays_reminders

if __name__ == "__main__":
	unittest.main(exit=False)
