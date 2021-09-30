import os
import sys
import time
from datetime import datetime
import socket
import random
from threading import Thread
import urllib.request


try:
    from colorama import Fore, init, Back
except:
    print("your required modules are not installed!")
    prompt_y_n=input("proceed installation? [Y/n]>>>")
    if "y" in prompt_y_n or "Y" in prompt_y_n or "yes" in prompt_y_n:
        print("starting the installation. please wait....")
        os.system("pip install pygame colorama")
    else:
        sys.exit()

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def check_connection(successfull_massage,unsuccessful_massage):
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False

    print(
        successfull_massage if connect( ) else unsuccessful_massage
          )

date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # current time info
clear_screen()
lobby = "on"
while lobby == "on":
    print(Fore.YELLOW+">ChatBord_cli"+Fore.RESET)
    print("")
    print("")
    print("[1] Host chat    [2] Join chat")
    print("")
    option = input(Fore.LIGHTGREEN_EX + "Select>")
    if option == "1":
        pass
    elif option == "2":
        colors=[
            Fore.BLUE,
            Fore.CYAN,
            Fore.GREEN,
            Fore.LIGHTBLACK_EX,
            Fore.LIGHTBLUE_EX,
            Fore.LIGHTCYAN_EX,
            Fore.LIGHTGREEN_EX,
            Fore.LIGHTMAGENTA_EX,
            Fore.LIGHTRED_EX,
            Fore.LIGHTYELLOW_EX,
            Fore.MAGENTA,
            Fore.RED,
            Fore.YELLOW
        ]
        client_color=random.choice(colors)  # random color for client

        SERVER_HOST=input(Fore.RESET+"enter server's IP: "+Fore.GREEN)  # server's IP
        SERVER_PORT=int(input(Fore.RESET+"enter server's port: "+Fore.GREEN))  # server's port
        print(""+Fore.RESET)
        separator_token=" "  # this is to separate the client name & message

        # initialize TCP socket
        s=socket.socket()
        print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
        # connect to the server
        try:
            s.connect((SERVER_HOST,SERVER_PORT))
        except ConnectionRefusedError:
            print(Fore.RED + "[X] machine refused to connect")
            print(Fore.YELLOW +"try contacting host to recreate a chatroom"+Fore.RESET)
            print(Fore.YELLOW+"you may have entered wrong port "+Fore.RESET)
            break
        except TimeoutError:
            print(Fore.RED+"[X] timed out connection")
            print(Fore.YELLOW+"try againg connecting to the server"+Fore.RESET)
            print(Fore.YELLOW+"wrong server address"+Fore.RESET)
            break
        except ValueError:
            print(Fore.RED+"[X] timed out connection")
            print(Fore.YELLOW+"try entering the correct value"+Fore.RESET)
            break


        print("[+] Connected.")
        # prompt the client for a name
        name=input("Enter your username: ")

        clear_screen()

        print("in order to left the chat type 'self-left'")
        notice = f"{name} joined this chat! ({date_now})\n"
        s.send(notice.encode())

        def listen_for_messages():
            while True:
                message=s.recv(1024).decode()
                print()
                print(message)

        # receive massages
        t=Thread(target=listen_for_messages)
        t.daemon=True
        t.start()

        while True:
            # input message we want to send to the server
            to_type = input(Fore.YELLOW + ">"+Fore.RESET)
            to_send = f"{client_color}{name}{Fore.RESET}{Fore.YELLOW}>{to_type}{Fore.RESET}"
            # send massage
            s.send(to_send.encode())
            # a way to exit the program
            if to_send.lower()=='self-left':
                s.send(Fore.RED + f"{name} has left the chat".encode()+ Fore.RESET)
                s.close()
                sys.exit()



    else:
        print(Fore.RED+"oops,wrong option!"+Fore.RESET)
        time.sleep(1)
        print(Fore.RED+"try again"+Fore.RESET)
        time.sleep(1)
        clear_screen()


