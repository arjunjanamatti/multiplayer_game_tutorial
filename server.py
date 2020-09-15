import socket
from _thread import *
import sys


server = '192.168.43.196'
port = 5555

# set up the socket to bind it
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# we are setting up a connection using a port on our server on our network, which will look for certain connections
try:
    s.bind((server, port))

except socket.error as e:
    str(e)


# below will open the port, if 2 is mentioned, it will allow only 2 people to enter the network
s.listen(2)
print('Waiting for the connection, server started!!!')

def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])

pos = [(0, 0), (100, 100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ''
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data


            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print('Received: ', reply)
                print('Sending: ', reply)

            conn.sendall(str.encode(make_pos(reply)))

        except:
            break

    print('Lost connection')
    conn.close()


currentPlayer = 0

# while loop will continuously look for connections
while True:
    conn, addr = s.accept()
    print('Connected to: ', conn, 'with address: ', addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1