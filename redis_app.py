import redis

# koneksi ke Redis server
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# menyimpan data
r.set("nama", "Zahadi Rizfy 2311082040 TRPL 3A")

# mengambil data
nama = r.get("nama")

print("Nama yang tersimpan di Redis:", nama)

# contoh counter
r.incr("pengunjung")

print("Jumlah pengunjung:", r.get("pengunjung"))