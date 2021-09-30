import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
import os

# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

client_color = random.choice(colors)  # random color for client
date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # current time information

SERVER_HOST = input(Fore.RESET+"enter server's IP: "+Fore.GREEN)  #server's IP
SERVER_PORT = input(Fore.RESET+"enter server's port: "+Fore.GREEN)  # server's port
print(""+Fore.RESET)
separator_token = "<SEP>" # this is to separate the client name & message

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
# prompt the client for a name
name = input("Enter your username: ")

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send = input(f"{client_color} {name}{separator_token}: {Fore.RESET}")
    # a way to exit the program
    if to_send.lower() == 'q':
        break
    # finally, send the message
    s.send(to_send.encode())

# close the socket
s.close()