import socket
import threading
from colors import text  # Import the colors module
import time

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                print(data.decode())  # Print the received data
        except Exception as e:
            print("Error:", e)
            break


def send_message(username, color_code):
    while True:
        message = input(color_code+'['+username+'] : ' +"\033[0m" )
        formatted_time = time.strftime("[%Y-%m-%d] [%H:%M:%S] ", time.localtime())
        formatted_message = "\n"+formatted_time + color_code+'['+username+'] : ' +"\033[0m" +message# Apply color to username
        client_socket.sendall(formatted_message.encode())  # Send the formatted message



def verif(ch):
    ch=ch.upper()
    i=0
    test=True
    while test==True and i<len(ch):
        if "A"<=ch[i]<="Z" or ch[i]=="_" or ch[i].isdigit():
            i+=1
        else:
            test=False
    return test
	



if __name__ == "__main__":

    username = input("Enter your username: ")
    while verif(username)==False or username=="":
        username = input("Enter a valid  username: ")

    # Display available colors from the colors module
    print("Available colors:")
    print("1. RED  2. GREEN  3. BLUE  4. YELLOW  5. PURPLE  6. ORANGE  7. PINK  8. BROWN  9. WHITE 10.RANDOM")
    color_choice = input("Choose your color (Enter a number from 1 to 10): ")
    
    while not(color_choice in ["1","2","3","4","5","6","7","8","9","10"]) :
        color_choice = input("Choose your color (Enter a number from 1 to 10): ")
    color_choice=int(color_choice)
    
    
    # Assign the chosen color code
    colors_list = [text.RED, text.GREEN, text.BLUE, text.YELLOW, text.PURPLE, text.ORANGE, text.PINK, text.BROWN,  text.WHITE, text.random()]
    color_code = colors_list[color_choice - 1]

    colored_username = color_code+username+"\033[0m"




    HOST = '192.168.43.1'  # Mobile hotspot IP address | local host : 127.0.0.1

    PORT = 5050

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))



    client_socket.send(colored_username.encode())


    print('Available RoomChats : ')
    print(" .1 .2 .3 .4 .5 ")
    room_choice = input("Choose a room chat (Enter a number from 1 to 5): ")
    while not(room_choice in ["1","2","3","4","5"]) :
        room_choice = input("Choose a room chat (Enter a number from 1 to 5): ")
    
    
    client_socket.send(room_choice.encode())



    initial_thread = threading.Thread(target=receive_messages)
    initial_thread.start()

    send_thread = threading.Thread(target=send_message, args=(username, color_code))
    send_thread.start()
