from socket import *

def send_command(socket, command):
    socket.send(command.encode())
    response = socket.recv(8192).decode()
    return response

def login(server, user, password):
    login_command = f'LOGIN:::CTAG::UN={user},PWD={password};'
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server, 3337))
    response = send_command(s, login_command)
    return s, response
