import console_application
from console_application import OrganizerItem


class Subject(OrganizerItem):

    def __init__(self):
        OrganizerItem.__init__(self)
        self.text = ''
        self.location = "--no location set--"
        self.owner = "--no owner set--"
        self.write_content_in_file()

    def write_content_in_file(self):
        self.content = open(self.name, 'r+')
        self.content.truncate()
        self.content.close()
        self.content = open(self.name, 'w')
        self.content.write("SUBJECT: " + self.text + "\nLOCTION: " +
                           self.location + "\nOWNER: " + self.owner + "\n" +
                           OrganizerItem.write_tags(self))

        self.content.close()

    def add_or_remove_tags(self, input_function):
        self.add_tags_to_content(input_function)

    def add(self, input_function):
        print ("\nENTER YOUR SUBJECT'S NAME:\n")
        self.text = input_function()
        print ("\nENTER THE LOCATION OF YOUR SUBJECT:\n")
        self.location = input_function()
        print("\nENTER YOUR SUBJECT'S OWNER:\n")
        self.owner = input_function()
        self.add_or_remove_tags(input_function)
        self.write_content_in_file()

    def edit(self, input_function):
        print("\nNOTE NOW IS:\n")
        self.perview()
        print("\nTO CHANGE ITEM'S SUBJECT, PRESS \'1\';\n" +
              "TO CHANGE ITEM'S LOCTION, PRESS \'2\';\n" +
              "TO CHANGE ITEM'S OWNER, PRESS \'3\';\n" +
              "TO CHANGE ITEM'S TAGS, PRESS \'4\'.\n")
        users_choice = input_function()
        if users_choice == '1':
            print("\nENTER YOUR NEW SUBJECT:\n")
            self.text = input_function()
        if users_choice == '2':
            print("\nENTER YOUR SUBJECT'S NEW LOCATION:\n")
            self.location = input_function()
        if users_choice == '3':
            self.location = input_function()
        if users_choice == '4':
            self.add_or_remove_tags(input_function)
        self.write_content_in_file()
