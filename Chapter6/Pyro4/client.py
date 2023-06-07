import Pyro4

schedules = [
    {"stasiun": "Gambir", "jadwal": "08:00"},
    {"stasiun": "Bandung", "jadwal": "09:30"},
    {"stasiun": "Yogyakarta", "jadwal": "11:15"},
    {"stasiun": "Surabaya", "jadwal": "13:45"},
    {"stasiun": "Malang", "jadwal": "15:20"}
]

server = Pyro4.Proxy("PYRONAME:server")
print(server.penjadwalan_kereta(schedules))
