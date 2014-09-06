from time import strftime
import os

#EXISTING_ORGANIZER_ITEMS = {"Notes" : [], "TODOs" : []}

FRAME = "\n" + ''.join(['=']*80) + "\n" + ''.join(['=']*80) + "\n"

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
        print ("\n" + FRAME + self.content.read() + FRAME)
        self.content.close()

    def __repr__(self):
        self.content = open(self.name, 'r')
        representstion = "\n" + FRAME + self.content.read() + FRAME
        self.content.close()
        return representstion

    def write_tags(self):
        return "TAGS: " + (", ".join(self.tags) + "\n")

    def add_or_remove_tags(self):
        print("\nADD\REMOVE TAGS TO THAT ITEM:\n" +
              "FOR ADDING PRESS \'A\' OR \'a\', FOR REMOVEING TAGS " +
              "PRESS \'R\' OR \'r\'\n"
              "(to exit adding/removeing tags, enter '.'):\n")
        users_choice = input()
        if users_choice == 'A' or users_choice == 'a':
            print("\nADD TAGS:\n")
            while True:
                tag = input()
                if tag == '.':
                    break
                self.tags.append(tag)
        elif users_choice == 'R' or users_choice == 'r':
            if len(self.tags) == 0:
                print("\n!!!NO TAGS TO REMOVE!!!\n")
                return
            print("\nPRESS NUMBERS OF TAGS YOU WANT TO REMOVE:\n")
            number_in_order = 1
            items_to_delete = []
            for possition in range(0, len(self.tags)):
                print(str(number_in_order) + " : " + self.tags[possition] +
                      "\n")
                number_in_order = number_in_order + 1
            while True:
                possition_to_remove_at = input()
                if possition_to_remove_at == '.':
                    break
                items_to_delete.append(
                    self.tags[int(possition_to_remove_at) - 1])
            for item in items_to_delete:
                self.tags.remove(item)

    def add_tags_to_content(self):
        OrganizerItem.add_or_remove_tags(self)
        self.write_content_in_file()

  	
class Note(OrganizerItem):

    def __init__(self):
        super().__init__()
        self.text = ''
        self.write_content_in_file()

    def write_content_in_file(self):
        self.content = open(self.name, 'r+')
        self.content.truncate()
        self.content.close()
        self.content = open(self.name, 'w')
        self.content.write("NOTE: " + self.text + "\n" +
            OrganizerItem.write_tags(self))
        self.content.close()

    def add_or_remove_tags(self):
        self.add_tags_to_content()

    def add(self):
        print("\nENTER YOUR NOTE:\n")
        self.text = input()
        print("\nFOR ADDING TAGS, PRESS \'t\' or  \'T\':\n")
        users_choice = input()
        if(users_choice == 't' or users_choice == 'T'):
            self.add_or_remove_tags()
        self.write_content_in_file()

    def edit(self):
        print ("\nNOTE NOW IS: \n\"")
        self.perview()
        print(
            "\nTO CHANGE YOUR NOTE, PRESS \'1\';" +
            "\nTO CHANGE TAGS, PRESS \'2\'.\n")
        users_choice = input()
        if users_choice == '1':
            print("\nENTER EDITED TEXT HERE:\n")
            self.text = input()
        if users_choice == '2':
            self.add_or_remove_tags()
        self.write_content_in_file()


class TODO(OrganizerItem):
    #finish_date - add

    def __init__(self):
        super().__init__()
        self.text = ''
        self.start_date = self.name[:10]
        self.is_finished = False
        self.finish_date = ''
        self.write_content_in_file()

    def write_content_in_file(self):
        self.content = open(self.name, 'r+')
        self.content.truncate()
        self.content.close()
        self.content = open(self.name, 'w')
        finished = "NO"
        if self.is_finished:
            finished = "YES"
        self.content.write("TO DO: " + self.text + "\nSTARTED ON: " +
                           self.start_date + "\nFINISHED: " + finished +
                           "\nFINISHED ON: " + "\n" +
                           OrganizerItem.write_tags(self) + "\n")
        self.content.close()

    def add_tags(self):
        self.add_tags_to_content()

    def add(self):
        print("\nWHAT DO YOU HAVE TO DO: \n")
        self.text = input()
        print("\nFOR ADDING TAGS, PRESS \'t\' or  \'T\':\n")
        users_choice = input()
        if users_choice == 't' or users_choice == 'T':
            self.add_or_remove_tags()
        self.write_content_in_file()

    def edit(self):
        print("TODO NOW IS:\n")
        self.perview()
        print(
            "\nTO CHANGE WHAT YOU HAVE TO DO, PRESS \'1\';" +
            "\nTO MARK/UNMARK AS FINISHED, PRESS \'2\'\n" +
            "\n TO CHANGE TAGS, PRESS \'3\'.\n")
        users_choice = input()
        if users_choice == '1':
            print ("ENTER YOUR NEW ASSIGNMENT:\n")
            self.text = input()
        if users_choice == '2':
            print(
                "\nPRESS \'Y\'/\'y\' TO SET AS FINNISHED AND \'N\'/\'n\'" +
                " TO SET AS NOT FINNISHED:\n")
            finished = input()
            if finished == 'Y' or finished == 'y':
                self.is_finished = True
                self.finish_date = strftime("%Y-%m-%d_%H:%M:%S")[:10]
            elif finished == 'N' or finished == 'n':
                self.finished = False
                self.finish_date = ''
        if users_choice == '3':
            self.add_or_remove_tags()
        self.write_content_in_file()
