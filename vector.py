import socket,threading,os,sys,time,random

global vetclock 
vetclock = {sys.argv[1]:0}

def stringify(lista):
    lista_string = ""
    for item in lista:
        lista_string += f",{item}:{lista[item]}"
    return lista_string[1:]

def destringify(lista_string,just_index=False):
    lista2 = {}
    revert_lista = lista_string.split(",")
    if not just_index:
        for item in revert_lista:
            item = item.split(":")
            lista2[item[0]]=int(item[1])
        return lista2
    return revert_lista

class UDPserver:
    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = ('localhost', int(port))
        self.clients = dict()
        self.port = port

    def listen(self):
        self.socket.bind(self.address)

        while True:
            data, client_address = self.socket.recvfrom(int(self.port))

            client_thread = threading.Thread(target=self.get_messages, args=(data, client_address))
            client_thread.start()

            self.clients[str(client_address[1])] = client_address

    def get_messages(self, data, client_address):
        global vetclock
        response = destringify(data.decode())
        vetclock[str(self.address[1])] += 1


        print(f"\nRECEBENDO MENSAGEM\nvetor atual{vetclock}")
        print(f"vetor recebido{response}")

        for item in response:
            if item not in vetclock.keys() or response[item] > vetclock[item]:
                vetclock[item] = response[item]
        print(f"vetor final{vetclock}")


    def run(self):
        transfer_message_thread = threading.Thread(target=self.listen)
        transfer_message_thread.start()

class UDPclient:
    def __init__(self, address):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = ('localhost', int(address))


    def letter_to(self,entity):
        global vetclock
        vetclock[str(self.address[1])] += 1
        print(f"\nENVIANDO MENSAGEM PARA {entity}")
        self.socket.sendto(stringify(vetclock).encode(), ('localhost', int(entity)))

        pass

    def send_message(self):
        global vetclock
        global proceed
        proceed = False

        while True:
            try:
                message = input("").split(" ")
                if len(message)<2:
                    message = message+[[]]
                action,entity = message[0],message[1]

                if action == "send":
                    self.letter_to(entity)

                if action == "neo" and entity != []:
                    print("\niniciando envio randômico, para parar escrever a palavra neo")
                    proceed = proceed != True 
                    thread0 = threading.Thread(target=self.bot_subway_money,args=(entity,)).start()
                
                if action == "p":
                    print("simulando processo interno")
                    vetclock[str(self.address[1])] += 1                   



                print(vetclock)
            except:
                os._exit(0)

    def bot_subway_money(self,stringified_processes):
        global proceed
        if proceed:
            elements = destringify(stringified_processes,just_index=True)
            time.sleep(random.randint(1, 4))
            self.letter_to(random.sample(elements, 1)[0])
            print(vetclock)

            self.bot_subway_money(stringified_processes)
    
    def run(self):
        thread1 = threading.Thread(target=self.send_message, args=())
        thread1.start()
   
print(vetclock)
threading.Thread(target=UDPserver(sys.argv[1]).run).start()
threading.Thread(target=UDPclient(sys.argv[1]).run).start()

while 1:
    1