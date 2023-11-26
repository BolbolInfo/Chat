import socket
import _thread
import os

def create_files():
    # Create a 'Log' folder if it doesn't exist
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    # Create log files for each room within the 'Log' folder if they don't exist
    for room_number in range(1, NUM_ROOMS + 1):
        log_file = os.path.join(LOG_FOLDER, f"room_{room_number}_chat_log.txt")
        if not os.path.exists(log_file):
            open(log_file, "a").close()



def send_message(conn,message):
    for room, room_clients in ROOMS.items():
        if conn in room_clients:
            for user in room_clients:
                if  user != conn :
                    try:
                        user.sendall(message.encode())
                    except:
                        print(f'failed to send data to {user} ')
                        

def load_last(ROOM_CHICE):
    ch=""
    log_file = os.path.join(LOG_FOLDER, f"room_{ROOM_CHICE}_chat_log.txt")
    with open(log_file, "r") as file:
        chatH=file.readlines()[-10:]
    ch=''
    for i in chatH:
        ch+=i
    if ch=='':
        return '\n no previos chat'
    else:
        return '\n'+ch





def client_thread(conn, addr):
    USERNAME = None
    ROOM_CHICE = None
    while True: 
        try:
            data = conn.recv(1024)
            if not data:
                break
            received_data = data.decode()  # Convert received bytes to string
            if USERNAME == None:
                USERNAME = received_data
                
            elif ROOM_CHICE == None:
                ROOM_CHICE = int(received_data)  
                
                ROOMS[ROOM_CHICE].append(conn)
                print(f"User '{USERNAME}' joined Room {ROOM_CHICE}")
                msg=load_last(ROOM_CHICE)

                conn.sendall(msg.encode())



            else:
                message=received_data
                save_to_log(int(ROOM_CHICE), message)


                send_message(conn,message)




        except Exception as e:
            print("Error:", e)
            break
    remove_client(conn)




def remove_client(conn):
    for room, clients in ROOMS.items():
        if conn in clients:
            clients.remove(conn)
            break

    conn.close()







def save_to_log(room, message):
    log_file = os.path.join(LOG_FOLDER, f"room_{room}_chat_log.txt")
    with open(log_file, "a") as file:
        file.write(message[1:] + '\n')




def start_server():
    print("Server is running on",HOST,'[',PORT,']','... ')

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((HOST, PORT))

    server_socket.listen()

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected with {addr}")
        _thread.start_new_thread(client_thread, (conn, addr))



if __name__ == '__main__':

    HOST = '192.168.43.1'  # Mobile hotspot IP address | local host : 127.0.0.1
    PORT = 5050
    LOG_FOLDER = "Log"  # Folder to store log files
    NUM_ROOMS = 5  # Number of rooms

    create_files()


    ROOMS = {room: [] for room in range(1, NUM_ROOMS + 1)}

    start_server()






