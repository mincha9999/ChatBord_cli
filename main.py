
import sys
import time
from datetime import datetime
import socket
import random
from threading import Thread
import urllib.request
import os

def check_connection(successfull_massage, unsuccessful_massage, if_exit):
    def connect_host_connection_check(host='http://google.com'):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False

    if connect_host_connection_check():
        print(successfull_massage)
    else:
        print(unsuccessful_massage)
        if if_exit:
            sys.exit()
        else:
            pass


try:
    from colorama import Fore, init, Back
    from playsound import playsound
    from pyngrok import ngrok
except:
    print("your required pakages are not installed!")
    prompt_y_n = input("proceed installation? [Y/n]>")
    
    if "y" in prompt_y_n or "Y" in prompt_y_n or "yes" in prompt_y_n:

        print("checking internet status...")
        check_connection("[+]Online!","[X]Offlie",True)

        print("starting the installation. please wait....")
        os.system("pip install pygame colorama")
        os.system("pip install playsound")
        os.system("pip install pyngrok")
        print("installation done!")
    else:
        sys.exit()


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def CB_command_quit():
    s.send(f"{name} has left the chat! ({date_now})".encode())
    sys.exit()
def CB_command_changecolor():
    client_color = random.choice(colors)

EXCLAIMATION_sign = Fore.LIGHTYELLOW_EX + "[!]" + Fore.RESET
ERROR_sign = Fore.LIGHTYELLOW_EX + "[" + Fore.RED + "X"+Fore.LIGHTYELLOW_EX+ "]" + Fore.RESET
FACT_sign = Fore.LIGHTYELLOW_EX + "[" + Fore.LIGHTBLUE_EX + "+" + Fore.LIGHTYELLOW_EX + "]" + Fore.RESET
STAR_sign = Fore.LIGHTYELLOW_EX + "[" + Fore.CYAN + "*" + Fore.LIGHTYELLOW_EX+ "]" + Fore.RESET


date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # current time info
Main_lobby = True
while Main_lobby:
    clear_screen()
    print(Fore.LIGHTYELLOW_EX + ">ChatBord_cli" + Fore.RESET)
    print("")
    print(Fore.LIGHTYELLOW_EX + "[1] Host chat    [2] Join chat")
    print("")
    option = input(Fore.LIGHTGREEN_EX + "Select>")

    if option == "1":
        HostChat_lobby = True
        while HostChat_lobby:
            clear_screen()
            print(Fore.LIGHTYELLOW_EX + ">ChatBord_cli" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + "[back] Back to main lobby")
            print("")
            print(Fore.LIGHTYELLOW_EX + "[1]Localhost  [2]ngrok   [3]custom" + Fore.RESET)
            print("")
            option = input(Fore.LIGHTGREEN_EX + "Select>")

            if option == "back":
                HostChat_lobby=False

            elif option == "1":

                #localhost ip configaration
                SERVER_IP = "127.0.0.1"
                server_ip_lobby=True
                while server_ip_lobby:
                    SERVER_PORT = int(input(f"{FACT_sign}{Fore.CYAN }Enter port>{Fore.RESET}"))
                    


                    if SERVER_PORT <= 9999 and SERVER_PORT >=1000:
                        #servercodegosbrrr
                        print(f"{FACT_sign}test: serverport " + str(SERVER_PORT))
                        # initialize list/set of all connected client's sockets
                        client_sockets = set()
                        print(FACT_sign +"initialized...")
                        # create a TCP socket
                        s = socket.socket()
                        print(STAR_sign+"Creating tcp connection...")
                        # make the port as reusable port
                        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        # bind the socket to the address we specified
                        s.bind((SERVER_IP, SERVER_PORT))
                        print(FACT_sign+"Done!")
                        # listen for upcoming connections
                        s.listen(5)
                        print(f"{STAR_sign} Listening as {SERVER_IP}:{SERVER_PORT}")
                        def listen_for_client(cs):
                            """
                            This function keep listening for a message from `cs` socket
                            Whenever a message is received, broadcast it to all other connected clients
                            """
                            while True:
                                try:
                                    # keep listening for a message from `cs` socket
                                    msg = cs.recv(1024).decode()
                                except Exception as e:
                                    # client no longer connected
                                    # remove it from the set
                                    print(f"{ERROR_sign} Error: {e}")
                                    client_sockets.remove(cs)
                                else:
                                    # if we received a message, replace the <SEP>
                                    # token with ": " for nice printing
                                    msg = msg.replace(separator_token, ": ")
                                    # iterate over all connected sockets
                                for client_socket in client_sockets:
                                    # and send the message
                                    client_socket.send(msg.encode())

                        while True: 
                            # we keep listening for new connections all the time
                            try:
                                client_socket, client_address = s.accept()
                                print(f"{FACT_sign} {client_address} connected.")
                            except KeyboardInterrupt():
                                print(EXCLAIMATION_sign + "Program Interupted!")
                            print("closing program")
                            # add the new connected client to connected sockets
                            client_sockets.add(client_socket)
                            # start a new thread that listens for each client's messages
                            t = Thread(target=listen_for_client, args=(client_socket,))
                            # make the thread daemon so it ends whenever the main thread ends
                            t.daemon = True
                            # start the thread
                            t.start()


                        #  close client sockets
                        for cs in client_sockets:
                         cs.close()
                        # close server socket
                        s.cl#525252se()

                    else:
                        print(f"{EXCLAIMATION_sign} {Fore.LIGHTRED_EX}Port number should be 4 digits,try again!{Fore.RESET}")
                        time.sleep(2)
            elif option == 2:
                SERVER_IP = "127.0.0.1"
                server_ip_lobby=True
                while server_ip_lobby:
                    SERVER_PORT = int(input(f"{FACT_sign}{Fore.CYAN }Enter port>{Fore.RESET}"))
                    
                    if SERVER_PORT <= 9999 and SERVER_PORT >=1000:
                        ngrok.connect()
            else:
                print(f"{EXCLAIMATION_sign} {Fore.LIGHTRED_EX}Wrong option,try again!{Fore.RESET}")
                time.sleep(2)


    elif option == "2":
        colors = [
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
        client_color = random.choice(colors)  # random color for client

        #SERVER_HOST = input(Fore.RESET + "enter server's IP: " + Fore.GREEN)  # server's IP
        #SERVER_PORT = int(input(Fore.RESET + "enter server's port: " + Fore.GREEN))  # server's port
        SERVER_HOST = "127.0.0.1"
        SERVER_PORT = 4444
        print("" + Fore.RESET)

        # initialize TCP socket
        s = socket.socket()
        print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
        # connect to the server
        try:
            s.connect((SERVER_HOST, SERVER_PORT))
            
        except ConnectionRefusedError:
            print(Fore.RED + "[X] machine refused to connect")
            print(Fore.YELLOW + "host might have stopped the room, try contacting host to recreate a chatroom" + Fore.RESET)
            print(Fore.YELLOW + "you may have entered wrong port " + Fore.RESET)
            print(Fore.YELLOW + "the server may has expired " + Fore.RESET)
            print(Fore.YELLOW + "you may not have internet connection " + Fore.RESET)
            break
        except TimeoutError:
            print(Fore.RED + "[X] timed out connection")
            print(Fore.YELLOW + "try again connecting to the server" + Fore.RESET)
            print(Fore.YELLOW + "wrong server address" + Fore.RESET)
            break
        except ValueError:
            print(Fore.RED + "[X] timed out connection")
            print(Fore.YELLOW + "try entering the correct value" + Fore.RESET)
            break

        print("[+] Connected.")

        name = str(input("Enter your username: "))

        
        clear_screen()
        notice = f"{name} joined this chat! ({date_now})\n"
        s.send(notice.encode())
        
        print(f'{client_color}You joined this chat!  {Fore.RESET}{Fore.LIGHTBLACK_EX}({date_now}){Fore.RESET}\n')


        def listen_for_messages():
            while True:


                
                message = s.recv(1024).decode()
                print()
                message_for_me = message.replace(f'{client_color}{name}{Fore.RESET}>{Fore.RESET}',f'{client_color}You{Fore.RESET}>{Fore.RESET}')

               #if message_for_me == f"{client_color}You{Fore.RESET}>{Fore.RESET}":
                    #playsound('/home/mincha/projects/ChatBord_cli/tok.mp3')
                #else:
                    #playsound('/home/mincha/projects/ChatBord_cli/bouce.wav')

                print(message_for_me)

        # receive massages
        t = Thread(target=listen_for_messages)
        t.daemon = True
        t.start()

        while True:
            # input message we want to send to the server
            try:
                client_msg = input(Fore.GREEN+">")
                to_send = f"{client_color}{name}{Fore.RESET}>{Fore.RESET}{client_msg}"
                s.send(to_send.encode())  # send massage



            except KeyboardInterrupt:
                s.send(f"{name} has left the chat! ({date_now})".encode())
                sys.exit()

            except ConnectionResetError():
                print(EXCLAIMATION_sign + "the server seeems to be closed or crashed")
                PRINT()
                exit()








    else:
        print(f"{EXCLAIMATION_sign} {Fore.LIGHTRED_EX}Wrong option,try again!{Fore.RESET}")
        time.sleep(2)
