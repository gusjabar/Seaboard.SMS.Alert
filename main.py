import os
import sys

from sms import *


def main(argv):
    try:
        if len(argv) > 1:
            # argv[1] has your filename
            filename = argv[1]
            send(filename)
        else:
            menu()
    except Exception as e:
        file = open("logerr.txt", "w")
        file.write("Error has been ocurred: " + str(e))
        file.close()


def menu():
    print("Main Menu")
    print(30 * '=')
    print("1-Send SMS")
    print("2-List resources")
    print("0-Exit")
    while True:
        menuItem = int(input("choose an option[0-2] :"))
        print("you choose:", menuItem)

        if menuItem == 0:
            print("option 0")
            cls()
            menu()
        elif menuItem == 1:
            print("Sending a SMS")
            print(30 * '-')
            msg = input("Write a message to send: ")
            send(msg)
        elif menuItem == 2:
            print("List of resources")
            print(30 * '-')
            listingResources()


def cls():
    print(os.name)
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main(sys.argv)
