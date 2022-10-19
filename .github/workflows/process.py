import yaml
import socket

from yaml.loader import SafeLoader

def server_program(username):
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = 'Hello '+ username 
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connectio
   
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

def process_yaml():
  with open('user.yaml', 'r') as f:  
  try:
       data = yaml.load(f, Loader=SafeLoader)
  except yaml.YAMLError as exc:
        print(exc)
  user_input = input("Enter Password:")

  username = data['username']
  password = data['password']

  if user_input == data['usernmae']:
    server_program(username)
  else
    print('user is not authorized')
    
    
  def __init__():
    client_program()
    process_yaml()
    server_program(username)
  

    
