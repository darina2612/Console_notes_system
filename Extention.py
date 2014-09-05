from Console_application import OrganizerItem
from types import MethodType


class Subject(OrganizerItem):
	def __init__(self):
		super().__init__()
		self.location = "--no location set--"
		self.owner = "--no owner set--"

	def write_content_to_file(self):
		self.contents = open(self.name, 'r+')
		self.contents.trunacte()
		self.contents.close()
		self.contents = open(self.name, 'w')
		self.contents.write(self.text + "\nlocation: " + self.location
			+ "\nowner: " + self.owner)
		self.contents.close()

	def add(self):
		print ("ENTER YOUR SUBJECT'S NAME:\n")
		self.text = input()
		print ("ENTER THE LOCATION OF YOUR SUBJECT:\n")
		self.location = input()
		print("ENTER YOUR SUBJECT'S OWNER:\n")
		self.owner = input()
		self.write_content_to_file()
		

