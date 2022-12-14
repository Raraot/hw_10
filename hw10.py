import functools
from collections import UserDict

# ДЕКОРАТОРИ
def welcome(func):                                                        # декоратор оформлення привітання
    def inner(*args, **kwargs):
        print("-"*36+"\n  Welcome to Assistant Console Bot\n"+"-"*36)
        return func(*args, **kwargs)
    return inner


def input_error(func):                                                    # декоратор обробки помилок
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("""You have not entered all data!!!
--------------------------------------------------------------------------------------------------
for adding new phone number please input:   add name tel.      (example: add Volodymyr 345-45-45)
for change please input:                    change name tel.   (example: change Volodymyr 2345789)
for reading please input:                   phone name         (example: phone Volodymyr)
--------------------------------------------------------------------------------------------------""")
        except KeyError:
            print("This user was not found in the phone book!")
        except ValueError:
            print("Invalid value. Try again.")
    return wrapper

# КЛАСИ
class FieldHandler:

    @ input_error
    def handler(self, vvod):                                                        # функція обробки команд
        if vvod.lower() == "hello":
            return "How can I help you?"
        elif vvod.lstrip()[0:3].lower() == "add":
            name = vvod.split(" ")[1]
            phone = vvod.split(" ")[2]
            adressbook.add_data(name, phone)
        elif "change" in vvod.lower():
            name = vvod.split(" ")[1]
            phone = vvod.split(" ")[2]
            adressbook.change_data(name, phone)
        elif "phone" in vvod.lower():
            return adressbook.data[vvod.split(" ")[1]]
        elif "show all" in vvod.lower():
            return adressbook.show_all()
        else:
            return "Unknown command, please input correct data or command!"


class AddressBook(UserDict, FieldHandler):
    
    def show_all(self):
        if self.data == {}:
            my_string ="Your phone book is empty."
        else:
            my_string ="Display full phone book:\n"
            for key, value in adressbook.data.items():
                my_string += ('{:<12} {:<15}\n'.format(key, ", ".join(value)))
        return my_string
    
    def change_data(self, name, phone):
        ph_list = self.data.get(name, [])
        ph_list[0] = phone
        self.data[name] = ph_list 

    def add_data(self ,name , phone = "", email = "" ):
        ph_list = self.data.get(name, [])
        ph_list.append(phone)
        self.data[name] = ph_list

class Name(FieldHandler):
    def __init__(self, name):
        self.name = name


class Phone(FieldHandler):
    def __init__(self, phone = ""):
        self.phone = phone


class Record(FieldHandler):
    def __init__(self ,name = "" , phone_list = [], email = ""):
        self.name = name
        self.phone_list = phone_list
        self.email = email


@ welcome
def main():
    while True:
        vvod = input(": ")
        if vvod.strip().lower() in [".", "good bye", "close", "exit", "stop", "palyanytsya"]:
            print("-"*36+"\n  Good bye!\n"+"-"*36)
            break
        else:
            print_me = fieldhandler.handler(vvod)
            if print_me != None:                                                # необхідне прінтування 
                print(print_me)
            continue

if __name__ == '__main__':
    adressbook = AddressBook()
    record = Record()
    fieldhandler = FieldHandler()
    main()