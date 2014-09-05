from time import strftime
import os

#EXISTING_ORGANIZER_ITEMS = {"Notes" : [], "TODOs" : []}


class OrganizerItem:

    def __init__(self):
        self.name = strftime("%Y-%m-%d_%H:%M:%S")
        self.content = open(self.name, 'w')
        self.content.close()
        self.tags = []

    def add(self):
        pass        

    def remove(self):
        os.remove(self.name)

    def edit(self):
        pass

    def perview(self):
        self.content = open(self.name, 'r')
        print (self.content.read())

    def write_content_in_file(self):
        pass

    def add_tags(self):
        print("ADD TAGS TO THAT ITEM (to exit adding tags, enter '.':\n")
        while True:
            tag = input()
            if tag == '.':
                break
            self.tags.append(tag)


class Note(OrganizerItem):

    def __init__(self):
        super().__init__()

    def write_content_in_file(self):
        self.content = open(self.name, 'r+')
        self.content.truncate()
        self.content.close()
        self.content = open(self.name, 'w')
        self.content.write(self.text)
        self.content.close()
    

    def add(self):
        print("ENTER YOUR NOTE:\n")
        self.text = input()
        print("fFOR ADDING TAGS, PRESS \'t\' or  ")
        write_content_in_file()

    def edit(self):
        print ("NOTE NOW IS: \n\"")
        self.perview()
        print("\nENTER EDITED TEXT HERE:")
        self.text = input()
        self.write_content_in_file()
        

class TODO(OrganizerItem):
    #finish_date - add

    def __init__(self):
        super().__init__()
        self.start_date = self.name[:10]
        self.is_finished = False

    def write_content_in_file(self):
        self.content = open(self.name, 'r+')
        self.content.truncate()
        self.content.close()
        self.content = open(self.name, 'w')
        finished = "NO"
        if self.is_finished:
            finished = "YES"
        self.content.write("to do: " + self.text + "\nstarted on:" +
            self.start_date + "\nfinished: " + finished)
        self.content.close()
                

    def add(self):
        print("WHAT DO YOU HAVE TO DO: \n")
        self.text = input()
        

    def edit(self):
        print("NOTE NOW IS:\n")
        self.perview()
        print("TO CHANGE THE TEXT, PRESS T")
