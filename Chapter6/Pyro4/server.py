import Pyro4


class Server:
    @Pyro4.expose
    def penjadwalan_kereta(self, list_jadwal: list[dict[str, str]]) -> str:
        strFinal = ""
        for i in list_jadwal:
            strFinal += self.jadwal_perjalanan(i) + "\n"
        return strFinal

    def jadwal_perjalanan(self, data: dict[str,str]) -> str:
        print(f"Memproses jadwal perjalanan kereta api di stasiun {data['stasiun']}")
        return f"Jadwal perjalanan kereta api di stasiun {data['stasiun']} datang pada jam {data['jadwal']}."

def startServer():
    server = Server()
    # make a Pyro daemon
    daemon = Pyro4.Daemon()
    # locate the name server running
    ns = Pyro4.locateNS()
    # register the server as a Pyro object
    uri = daemon.register(server)
    # register the object with a name in the name server
    ns.register("server", uri)
    # print the uri so we can use it in the client later
    print("Ready. Object uri =", uri)
    # start the event loop of the server to wait for calls
    daemon.requestLoop()


if __name__ == "__main__":
    startServer()
