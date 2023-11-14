class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

class Server:
    start_ip = 0

    @classmethod
    def create_ip(cls):
        cls.start_ip += 1
        return cls.start_ip

    def __init__(self):
        self.ip = self.create_ip
        self.buffer = []

    @staticmethod
    def send_data(data: Data):
        if data.ip in Router.buffer:
            Router.buffer[data.ip].append(data)

    def get_data(self):
        temp_buffer = self.buffer.copy()
        self.buffer.clear()
        return temp_buffer



class Router:
    connected_servers = []
    buffer = {}

    @classmethod
    def send_data(cls):
        for server in cls.connected_servers:
            if server.ip in cls.buffer:
                for data in cls.buffer[server.ip]:
                    server.buffer.append(data)
        cls.buffer.clear()

    @classmethod
    def link(cls, server:Server):
        cls.connected_servers.append(server)
        cls.buffer [server.ip] = []

    @classmethod
    def unlink(cls, server):
        if server.ip in cls.buffer:
            cls.buffer.pop(server.ip)

server1 = Server()
server2 = Server()
Router.link(server1)
Router.link(server2)
Router.link(Server())
Router.link(Server())
server_receiver = Server()
Router.link(server_receiver)
server1_sender.send_data(Data("Hello", server_receiver.ip))
server2_sender.send_data(Data("Hello", server_receiver.ip))
server_receiver
Router.send_data()
print(server)