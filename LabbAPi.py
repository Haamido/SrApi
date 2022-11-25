import requests
import sys
import time
import json




def kanal1():
    url = requests.get('http://api.sr.se/api/v2/channels/132?format=json').text
    url_info = json.loads(url)
    for item in url_info.items():
        print(item)


def kanal2():
    url = requests.get("http://api.sr.se/api/v2/channels/163?format=json").text
    url_info = json.loads(url)
    for item in url_info.items():
        print(item)


def kanal3():
    url = requests.get("http://api.sr.se/api/v2/channels/164?format=json").text
    url_info = json.loads(url)
    for item in url_info.items():
        print(item)


def kanal4():
    url = requests.get("http://api.sr.se/api/v2/channels/212?format=json").text
    url_info = json.loads(url)
    for item in url_info.items():
        print(item)


def kanal5():
    url = requests.get("http://api.sr.se/api/v2/channels/210?format=json").text
    url_info = json.loads(url)
    for item in url_info.items():
        print(item)


def menu():
    while (True):
        print("""" Menu - Choose a Radio station:
1. p1
2. p2
3. p3
4. p4 Göteborg
5. p4 Gävleborg   
        
        """"")

        choice = int(input("### Choice? "))
        if choice == 1:
            print(kanal1())
        elif choice == 2:
            print(kanal2())
        elif choice == 3:
            print(kanal3())
        elif choice == 4:
            print(kanal4())
        elif choice == 5:
            print(kanal5())
        else:
            print("Please choose a station with the value 1-5 ")


if __name__ == "__main__":
    menu()
