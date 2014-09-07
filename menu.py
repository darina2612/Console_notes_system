from console_application import *
from extention import *


ITEMS = {"Note": [], "TODO": [], "Subject": []}
TYPES = {"Note": Note, "TODO": TODO, "Subject": Subject}


def items_listed():
    items_listed = []
    for key in ITEMS:
        items_listed.extend(ITEMS[key])
    return items_listed


def select(items):
    print("\nSELECT NUMBER:\n")
    for index in range(0, len(items)):
        print ("((" + str(index + 1) + "))" + str(items[index]) + '\n')
    users_choice = input()
    if not users_choice.isdigit():
        return "fail"
    return items[int(users_choice) - 1]


def print_types_names_for_selection():
    for organizer_item_type in TYPES.keys():
        print("\nFOR " + organizer_item_type + " TYPE \'" +
              organizer_item_type + '\'')


def add_item():
    print_types_names_for_selection()
    item_type = input()
    if not item_type in TYPES.keys():
        print ("\n!!!NO SUCH TYPE OF OF ITEM!!!\n")
        return "fail"
    item = TYPES[item_type]()
    ITEMS[item_type].append(item)
    item.add(input)
    print(item)
    return item


def search_by_type(item_type):
    return ITEMS[item_type]


def search_by_word(items, word):
    items_found = []
    for item in items:
        if word in repr(item):
            items_found.append(item)
    return items_found


def serach_by_start_date(items, date):
    items_found = []
    for item in items:
        if item.name[:10] == date:
            items_found.append(item)
    return items_found


def search_by_tag(items, tag):
    items_found = []
    for item in items:
        if tag in item.tags:
            items_found.append(item)
    return items_found


def print_list_of_items(items):
    for item in items_listed():
        print(item)


def searching():
    selection = items_listed()
    print("SEARCH:\n")
    # print_list_of_items(selection)
    print("TYPE THE TYPE OF ITEM YOU WANT TO SEARCH:\n")
    print_types_names_for_selection()
    users_choice = input()
    if users_choice in TYPES.keys():
        selection = search_by_type(users_choice)
    print("SELECT \'y\' IF YOU WANT TO SEARCH BY START DATE:\n")
    users_choice = input()
    if users_choice == 'y':
        print("TYPE DATE IN \'YYYY-MM-DD\' FORMAT:\n")
        date = input()
        selection = search_by_start_date(selection, date)
    print("SELECT \'y\' TO SEARCH WORD:\n")
    users_choice = input()
    if users_choice == 'y':
        print("TYPE THE WORD YOU WANT TO SEARCH FOR:\n")
        word = input()
        selection = search_by_word(selection, word)
    print("SELECT \'y\'TO SEARCH BY TAG:\n")
    users_choice = input()
    if users_choice == 'y':
        selection = search_by_tag(selection, tag)
    print("FOUND :\n")
    print_list_of_items(selection)
    while True:
        print("IF YOU WANT TO EDIT ITEM, SELECT \'e\' OR \'E\';\n" +
              "IF YOU WANT TO PERVIEW IT, SELECT \'p\' OR \'P\'" +
              "TO DELETE ITEM, SELECT \'D\' OR \'d\'"
              "TO CONTINUE, PRESS \'.\'\n")
        users_choice = input()
        if users_choice == '.':
            break
        if users_choice == 'e' or users_choice == 'E':
            item_to_edit = select(selection)
            if isinstance(item_to_edit, str):
                continue
            item_to_edit.edit(input)
        if users_choice == 'p' or users_choice == 'P':
            item_to_perview = select(selection)
            if isinstance(item_to_perview, str):
                continue
            item_to_perview.perview()
        if users_choice in ['D', 'd']:
            item_to_delete = select(selection)
            if isinstance(item_to_delete, str):
                continue
            item_to_delete.delete()
            ITEMS[str(item_to_delete.__class__.__name__)].remove(
                item_to_delete)


def menu():
    print(FRAME + "WELCOME!\n")
    while True:
        print("FOR ADDING NEW ITEM, SELECT \'1\';\n" +
              "FOR SEARCHING, SELECT \'2\';\n" +
              "FOR EXIT, SELECT \'E\' OR \'e\';\n")
        users_selection = input()
        if(users_selection == '1'):
            item = add_item()
            if isinstance(item, str):
                continue
            print("TO EDIT YOUR ITEM, SELECT \'C\' OR \'c\'\n" +
                  "TO DELETE IT, SELECT \'D\' OR \'d\'")
            users_choice = input()
            if users_choice == 'C' or users_choice == 'c':
                item.edit(input)
            if users_choice == 'D' or users_choice == 'd':
                item.remove(input)
                ITEMS[str(item.__class__.__name__)].remove(item)
        if users_selection == '2':
            searching()
        if(users_selection == 'E' or users_selection == 'e'):
           # with open("current_items.pickle", 'wb', pickle.HIGHEST_PROTOCOL) as saved_items:
            #    pickle.dump(ITEMS, saved_items)
            print("\nBYE!" + "\n" + FRAME + "\n")
            break


def main():
    menu()

if __name__ == '__main__':
    main()
