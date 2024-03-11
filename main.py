import socket, threading,os

class TCPserver:
    def __init__(self,address,TYPE="TCP"):
        self.socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',int(address))
        self.clients = dict()

    def get_messages(self,entity,entity_name):
        while 1:
            try:
                input = entity.recv(self.address[1]).decode()
                
                if input.split(":")[0] in self.clients.keys():
                    self.clients[input.split(":")[0]].send(input.encode())



                print(f"{entity_name}: {input}")
            except(ConnectionResetError):
                os._exit(0)

    def listen(self):
        self.socket.bind(self.address)
        self.socket.listen()
        
        while 1:

            cliente, cliente_sitio = self.socket.accept()
            
            cliente_thread = threading.Thread(target=self.get_messages, args=(cliente,str(cliente_sitio[1]))).start()
            self.clients[str(cliente_sitio[1])] = (cliente )            
            print(f"connection {len(self.clients)} stablished with {cliente_sitio[1]}")
            print(self.clients)

    def send_message(self):
        while 1:
            try:
                message = input("").encode()
                for client in self.clients:
                    self.clients[client].send(message)

            except:
                os._exit(0)

    def run(self):
        listenThread = threading.Thread(target=self.listen).start()
        send_messageThread = threading.Thread(target=self.send_message).start()

        while 1:
            1
TCPserver(123).run()