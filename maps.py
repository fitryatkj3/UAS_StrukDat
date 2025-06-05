'''
Program Representasi Graph dengan Algoritma Dijkstra dan TSP oleh:
Kelompok 7
1. Septiana Dwi Lestari     (24091397113)
2. Fitrya Chalifatus Zahro  (24091397117)
3. Naufal Ihsan Awari       (24091397131)
'''

# import library yang diperlukan
import heapq # untuk implementasi algoritma Dijkstra
import networkx as nx # untuk visualisasi graph
import matplotlib.pyplot as plt # untuk plotting graf
from itertools import permutations # untuk implementasi TSP

class Graph: # class untuk representasi graph
    def __init__(self): # konstruktor
        self.adj_list = {} # adjacency list untuk representasi graph
    
    def add_vertex(self, city): # fungsi untuk menambahkan vertex (kota)
        if city not in self.adj_list: # jika kota belum ada di graph
            self.adj_list[city] = {} # tambahkan kota ke adjacency list
    
    def add_edge(self, city1, city2, distance): # fungsi untuk menambahkan edge (jalur)
        self.adj_list[city1][city2] = distance # menambahkan jalur dari kota1 ke kota2 dengan jarak
        self.adj_list[city2][city1] = distance # menambahkan jalur dari kota2 ke kota1 dengan jarak yang sama
    
    def get_neighbors(self, city): # fungsi untuk mendapatkan tetangga suatu vertex (kota)
        return self.adj_list[city] # return dictionary tetangga suatu vertex (kota)

jawa_timur = Graph() # inisialisasi graph Jawa Timur

# menambahkan 10 vertex (kota) di Jawa Timur
cities = [
    "Surabaya", "Malang", "Kediri", "Blitar", "Madiun",
    "Jember", "Banyuwangi", "Pasuruan", "Probolinggo", "Lamongan"
]

for city in cities: # menambahkan vertex (kota) ke dalam graph
    jawa_timur.add_vertex(city) 

# menambahkan edge (jalur) antar vertex (kota) dengan jarak yang telah ditentukan dalam km
edges = [
    ("Surabaya", "Lamongan", 50), ("Surabaya", "Pasuruan", 65),
    ("Surabaya", "Probolinggo", 90), ("Malang", "Pasuruan", 45),
    ("Malang", "Probolinggo", 70), ("Malang", "Blitar", 45),
    ("Malang", "Kediri", 60), ("Kediri", "Blitar", 40),
    ("Kediri", "Madiun", 65), ("Blitar", "Madiun", 55),
    ("Madiun", "Lamongan", 120), ("Jember", "Banyuwangi", 60),
    ("Jember", "Probolinggo", 100), ("Jember", "Malang", 110),
    ("Banyuwangi", "Probolinggo", 150), ("Pasuruan", "Probolinggo", 35),
    ("Lamongan", "Madiun", 120), ("Surabaya", "Madiun", 130),
    ("Malang", "Jember", 110), ("Kediri", "Jember", 140),
    ("Blitar", "Jember", 130), ("Probolinggo", "Banyuwangi", 150),
    ("Pasuruan", "Malang", 45), ("Surabaya", "Malang", 90),
    ("Kediri", "Surabaya", 110), ("Blitar", "Surabaya", 120),
    ("Madiun", "Kediri", 65), ("Jember", "Pasuruan", 115),
    ("Banyuwangi", "Jember", 60), ("Lamongan", "Surabaya", 50)
]

for edge in edges: # menambahkan edge (jalur) ke dalam graph
    jawa_timur.add_edge(*edge)

def dijkstra(graph, start, end): # fungsi untuk implementasi Algoritma Dijkstra
    distances = {city: float('infinity') for city in graph.adj_list} # inisialisasi jarak awal dengan nilai tak terhingga
    distances[start] = 0 # jarak awal dari kota start ke kota start adalah 0
    previous = {city: None for city in graph.adj_list} # inisialisasi kota sebelumnya dengan nilai None
    priority_queue = [(0, start)] # inisialisasi priority queue dengan jarak awal dan kota start
    
    while priority_queue: # loop hingga priority queue kosong
        current_distance, current_city = heapq.heappop(priority_queue) # pop kota dengan jarak terkecil dari priority queue
        
        if current_city == end: # berhenti jika kota saat ini adalah kota tujuan
            break
            
        for neighbor, weight in graph.get_neighbors(current_city).items(): # loop melalui tetangga kota saat ini
            distance = current_distance + weight # hitung jarak ke tetangga kota saat ini
            
            if distance < distances[neighbor]: # jika jarak baru lebih cepat dari jarak sebelumnya
                distances[neighbor] = distance # update jarak
                previous[neighbor] = current_city # update kota sebelumnya
                heapq.heappush(priority_queue, (distance, neighbor)) # tambahkan ke priority queue
    
    if distances[end] != float('infinity'): # jika jarak ke kota tujuan tidak tak terhingga
        path = [] # inisialisasi jalur dengan nilai kosong
        current = end # inisialisasi kota saat ini dengan kota tujuan
        while current is not None: # loop hingga kota saat ini adalah kota start
            path.append(current) # tambahkan kota saat ini ke jalur
            current = previous[current] # update kota saat ini dengan kota sebelumnya
        path.reverse() # balik jalur
        return path, distances[end] # return jalur dan jarak ke kota tujuan
    else:
        return None, None # return None jika jarak ke kota tujuan tak terhingga

def tsp_bruteforce(graph, start): # fungsi untuk implementasi Algoritma TSP Brute Force
    cities = list(graph.adj_list.keys()) # inisialisasi kota dengan kunci dari adjacency list
    if start not in cities: # jika kota start tidak ada di kota
        return None, float('infinity') # return None dan jarak tak terhingga
    
    cities.remove(start) # hapus kota start dari kota
    shortest_path = None # inisialisasi jalur terpendek dengan nilai None
    min_distance = float('infinity') # inisialisasi jarak terpendek dengan nilai tak terhingga
    
    for perm in permutations(cities): # loop melalui semua permutasi kota
        current_distance = 0 # inisialisasi jarak saat ini dengan nilai 0
        current_city = start # inisialisasi kota saat ini dengan kota start
        path = [start] # inisialisasi jalur dengan kota start 
        valid_path = True # inisialisasi validitas jalur dengan nilai True
        
        for next_city in perm: # loop melalui kota berikutnya
            if next_city in graph.adj_list[current_city]: # jika kota berikutnya ada di adjacency list kota saat ini
                current_distance += graph.adj_list[current_city][next_city] # tambahkan jarak ke kota berikutnya
                current_city = next_city # update kota saat ini dengan kota berikutnya
                path.append(next_city) # tambahkan kota berikutnya ke jalur
            else:
                valid_path = False # jika kota berikutnya tidak ada di adjacency list kota saat ini, berhenti
                break 
        
        if valid_path and current_distance < min_distance: # jika jalur valid dan jarak saat ini lebih kecil dari jarak terpendek saat ini
            min_distance = current_distance # update jarak terpendek saat ini
            shortest_path = path 
    
    return shortest_path, min_distance # return jalur terpendek dan jarak terpendek

def main(): # fungsi utama
    print("Kota di Jawa Timur:") # cetak kota di Jawa Timur
    for i, city in enumerate(cities, 1): # loop melalui kota di Jawa Timur
        print(f"{i}. {city}") # cetak kota dengan nomor urut
    
    ''' Algoritma Dijkstra '''
    city_mapping = {city.lower(): city for city in cities} # inisialisasi mapping antar kota dalam bentuk kecil
    
    while True: # loop hingga pengguna memilih untuk berhenti
        print("\n=== Algoritma Dijkstra (Rute Tercepat Antar-Kota) ===") # cetak judul algoritma Dijkstra
        start_input = input("Masukkan kota asal (atau 'exit' untuk keluar): ").strip().lower() # input kota asal pengguna
        
        if start_input == 'exit': # jika pengguna memilih untuk keluar, berhenti
            break
            
        start = city_mapping.get(start_input) # inisialisasi kota asal pengguna dengan kunci dari mapping
        if not start: # jika kota asal tidak ada di mapping
            print("Kota tidak ditemukan! Silakan coba lagi.") # cetak pesan kesalahan
            continue
            
        end_input = input("Masukkan kota tujuan: ").strip().lower() # input kota tujuan pengguna
        end = city_mapping.get(end_input) # inisialisasi kota tujuan pengguna dengan kunci dari mapping
        if not end: # jika kota tujuan tidak ada di mapping
            print("Kota tujuan tidak ditemukan! Silakan coba lagi.") # cetak pesan kesalahan
            continue
            
        if start == end: # jika kota asal sama dengan kota tujuan
            print("Kota asal dan tujuan sama! Silakan pilih kota yang berbeda.") # cetak pesan kesalahan
            continue
        
        path, distance = dijkstra(jawa_timur, start, end) # jalankan algoritma Dijkstra untuk menemukan jalur terpendek antara kota awal dengan kota tujuan
        
        if path: # jika jalur terpendek ditemukan
            print(f"\nJalur tercepat dari {start} ke {end}:") # cetak judul jalur tercepat
            print(" -> ".join(path)) # cetak jalur tercepat
            print(f"Total jarak ditempuh: {distance} km") # cetak jarak total yang ditempuh
        else:
            print(f"\nTidak ditemukan rute yang valid dari {start} ke {end}!") # cetak pesan kesalahan
        
        lanjut = input("\nCari rute lain? (y/n): ").strip().lower() # input pengguna untuk melanjutkan atau berhenti
        if lanjut != 'y': # jika pengguna memilih untuk berhenti, berhenti
            break
    
    ''' Algoritma TSP '''
    while True: # loop hingga pengguna memilih untuk berhenti
        print("\n=== Traveling Salesman Problem (TSP) ===") # cetak judul TSP
        start_input = input("Masukkan kota awal TSP (atau 'exit' untuk keluar): ").strip().lower() # input kota awal pengguna
        
        if start_input == 'exit': # jika pengguna memilih untuk keluar, berhenti
            break
            
        start_city = city_mapping.get(start_input) # inisialisasi kota awal pengguna dengan kunci dari mapping
        if not start_city: # jika kota awal tidak ada di mapping
            print("Kota tidak ditemukan! Pilihan kota yang valid:") # cetak pesan kesalahan
            print(", ".join(cities)) # cetak kota yang valid
            continue
            
        path, distance = tsp_bruteforce(jawa_timur, start_city) # jalankan algoritma TSP dengan metode brute force
        
        if path: # jika jalur terpendek ditemukan
            print("\nRute TSP terbaik:") # cetak judul jalur TSP terbaik
            print(" -> ".join(path)) # cetak jalur TSP terbaik
            print(f"Total jarak tempuh: {distance} km") # cetak jarak total yang ditempuh
            
            print("\nVisualisasi Graph:") # cetak judul visualisasi grafik
            for i in range(len(path)-1): # loop untuk setiap kota di jalur TSP 
                print(f"{path[i]} --{jawa_timur.adj_list[path[i]][path[i+1]]}km--> {path[i+1]}") # cetak jalur antara kota
        else:
            print("\nTidak ditemukan rute yang valid untuk mengunjungi semua kota!") # cetak pesan kesalahan
            print("Kemungkinan penyebab:") # cetak penyebab
            print("- Graph tidak terhubung sepenuhnya") # ada kota yang terisolasi
            print("- Beberapa kota tidak terhubung langsung") # tidak ada edge (jalur) langsung antar kota
            
        lanjut = input("\nHitung TSP lagi? (y/n): ").strip().lower() # input pengguna untuk melanjutkan atau berhenti
        if lanjut != 'y': # jika pengguna memilih untuk berhenti, berhenti
            break

def visualize_graph(graph): # fungsi untuk implementasi visualisasi graph
    G = nx.Graph() # membuat graph kosong atau graph tidak berarah
    
    for city in graph.adj_list: # loop melalui setiap kota
        for neighbor, distance in graph.adj_list[city].items(): # loop tetangga
            G.add_edge(city, neighbor, weight=distance) # tambahkan edge (jalur) dengan atribut jarak
    
    pos = nx.spring_layout(G, seed=42)  # menentukan posisi node menggunakan algoritma spring layout
    
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue') # menggambar node dengan parameter
    
    nx.draw_networkx_edges(G, pos, width=1.5, edge_color='gray') # menggambar edge (jalur) dengan parameter
    
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif') # menggambar label nama kota
    
    edge_labels = nx.get_edge_attributes(G, 'weight') # mengambil atribut jarak untuk ditampilkan di edge (jalur)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8) # menggambar label jarak di setiap edge (jalur)
    
    plt.title("Peta Jawa Timur dengan Jarak Antar Kota (km)") # menambahkan judul visualisai
    plt.axis('off')  # menghilangkan axis
    plt.tight_layout() # adjust layout
    plt.show() # menampilkan visualisasi

if __name__ == "__main__":
    visualize_graph(jawa_timur) # menjalankan visualisasi graph
    main() # menjalankan program utama
    