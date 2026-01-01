  # 🌐 Maze DFS Algorithm

> Implementasi algoritma Depth-First Search (DFS) untuk penyelesaian maze dengan visualisasi interaktif menggunakan Python

[![Python](https://img.shields.io/badge/Python-100%25-3776AB?style=flat-square&logo=python&logoColor=white)](https://github.com/bagaspng/MazeDFSAlgorithm)
[![Algorithm](https://img.shields.io/badge/Algorithm-DFS-success?style=flat-square&logo=algolia&logoColor=white)](https://github.com/bagaspng/MazeDFSAlgorithm)
[![pyamaze](https://img.shields.io/badge/Library-pyamaze-blue?style=flat-square&logo=python&logoColor=white)](https://pypi.org/project/pyamaze/)


## 📋 Deskripsi

Maze DFS Algorithm adalah implementasi algoritma **Depth-First Search** untuk mencari jalur dalam labirin (maze). Proyek ini menggunakan library `pyamaze` untuk menciptakan visualisasi interaktif yang menunjukkan proses pencarian DFS secara real-time, mulai dari eksplorasi node hingga pembentukan jalur solusi.

## ✨ Fitur Utama

### 🎯 **Core Algorithm Features**
- 🔍 **DFS Implementation** - Algoritma Depth-First Search yang efisien
- 🎮 **Interactive Visualization** - Visualisasi real-time proses pencarian
- 📊 **Path Reconstruction** - Pembentukan jalur dari start ke goal
- 🎨 **Multi-Agent Display** - Menampilkan pencarian dan solusi secara terpisah

### 🛠️ **Technical Features**
- 📂 **CSV Maze Loading** - Support untuk maze dari file CSV
- 🎲 **Dynamic Maze Generation** - Generate maze otomatis
- 🚀 **Customizable Parameters** - Konfigurasi start/goal positions
- 📈 **Algorithm Analysis** - Tracking explored nodes dan path length

### 🎨 **Visualization Features**
- 🟢 **Search Process** - Agen hijau menunjukkan proses pencarian
- 🟡 **Solution Path** - Agen kuning menunjukkan jalur solusi
- 👣 **Footprints** - Jejak perjalanan agen
- 🔴 **Marked Cells** - Highlight cells dengan multiple choices

## 🧠 Algoritma DFS

### 📖 **Konsep Dasar**

Depth-First Search (DFS) adalah algoritma traversal graf yang: 

1. **Eksplorasi Mendalam** - Mengeksplorasi satu jalur sedalam mungkin
2. **Stack-Based** - Menggunakan struktur data stack (LIFO)
3. **Backtracking** - Kembali ke node sebelumnya jika jalan buntu
4. **Complete** - Akan menemukan solusi jika ada

### ⚙️ **Cara Kerja Algoritma**

```python
def DFS(maze, start):
    explored = [start]      # Nodes yang sudah dikunjungi
    frontier = [start]      # Stack untuk DFS
    path = {}              # Parent tracking untuk rekonstruksi
    
    while frontier:
        current = frontier.pop()    # Ambil dari stack (LIFO)
        
        if current == goal:         # Cek apakah sudah sampai tujuan
            break
            
        for neighbor in get_neighbors(current):
            if neighbor not in explored:
                explored.append(neighbor)
                frontier. append(neighbor)  # Tambah ke stack
                path[neighbor] = current   # Simpan parent
    
    return construct_path(path)
```

### 📊 **Kompleksitas Algoritma**

| Aspek | Big O Notation | Keterangan |
|-------|----------------|------------|
| **Time Complexity** | O(V + E) | V = vertices, E = edges |
| **Space Complexity** | O(V) | Untuk menyimpan explored nodes |
| **Path Optimality** | ❌ Not Optimal | Tidak menjamin jalur terpendek |
| **Completeness** | ✅ Complete | Pasti menemukan solusi jika ada |

## 🚀 Instalasi & Setup

### 📦 **Prerequisites**

```bash
# Python 3.7+
python --version

# pip package manager
pip --version
```

### 🔧 **Install Dependencies**

```bash
# Install pyamaze library
pip install pyamaze

# Alternative: install from requirements
pip install -r requirements.txt
```

### 📥 **Clone Repository**

```bash
git clone https://github.com/bagaspng/MazeDFSAlgorithm.git
cd MazeDFSAlgorithm
```

### 📋 **Requirements File**

```txt name=requirements.txt
pyamaze>=1.0.0
matplotlib>=3.5.0
numpy>=1.21.0
```

## 🎮 Penggunaan

### 🏃‍♂️ **Quick Start**

```bash
# Jalankan demo utama dengan maze dari CSV
python DFSDemo.py

# Jalankan dengan maze yang di-generate otomatis
python tes.py
```

### 🎯 **Customization Examples**

#### 📂 **Menggunakan Custom Maze**

```python
from pyamaze import maze, agent, COLOR

# Load maze dari file CSV
m = maze()
m.CreateMaze(loadMaze='your_custom_maze.csv')

# Set start dan goal position
start = (1, 1)
goal = (8, 8)
m._goal = goal

# Jalankan DFS
dSearch, dfsPath, fwdPath = DFS(m, start)
```

#### 🎲 **Generate Random Maze**

```python
# Create maze dengan ukuran custom
m = maze(15, 15)  # 15x15 maze
m. CreateMaze(2, 4)  # Goal di (2, 4)

# Jalankan DFS dengan start position custom
dSearch, dfsPath, fwdPath = DFS(m, (10, 1))
```

#### 🎨 **Kustomisasi Visualisasi**

```python
# Agent dengan style custom
search_agent = agent(m, x, y, 
                    goal=(gx, gy),
                    footprints=True, 
                    shape='square', 
                    color=COLOR.red,
                    filled=True)

solution_agent = agent(m, x, y,
                      goal=(gx, gy), 
                      footprints=True,
                      color=COLOR.blue,
                      filled=False)

# Trace path dengan options
m.tracePath({search_agent: dSearch}, 
           showMarked=True, 
           delay=50)
m.tracePath({solution_agent: fwdPath}, 
           delay=100)
```

## 📁 Struktur Project

```
MazeDFSAlgorithm/
│
├── 📄 DFSDemo.py              # Main demo dengan CSV maze
├── 📄 tes. py                  # Demo dengan generated maze
├── 📊 dfs_maze.csv           # Predefined maze data
├── 📂 __pycache__/           # Python cache files
├── 📋 requirements.txt       # Dependencies
└── 📖 README.md             # Documentation (this file)
```



## 🎓 Educational Content

### 📚 **Learning Objectives**

Dengan proyek ini, Anda akan mempelajari: 

1. **Graph Algorithms** - Konsep dasar algoritma graf
2. **Search Strategies** - Perbedaan DFS vs BFS vs A*
3. **Data Structures** - Stack, List, Dictionary usage
4. **Visualization** - Library untuk visualisasi algoritma
5. **Python Programming** - Advanced Python concepts


### 🧪 **Testing**

```python
import unittest

class TestDFSAlgorithm(unittest.TestCase):
    
    def setUp(self):
        self.maze = maze(5, 5)
        self.maze.CreateMaze()
    
    def test_dfs_finds_solution(self):
        """Test that DFS finds a valid solution"""
        dSearch, dfsPath, fwdPath = DFS(self.maze, (1, 1))
        self.assertIsNotNone(fwdPath)
        self.assertGreater(len(fwdPath), 0)
    
    def test_path_validity(self):
        """Test that found path is valid"""
        # Implementation
        pass

if __name__ == '__main__':
    unittest.main()
```


## 📚 References

### 📖 **Academic Papers**
- Tarjan, R. (1972). "Depth-First Search and Linear Graph Algorithms"
- Cormen, T. H., et al. (2009). "Introduction to Algorithms, 3rd Edition"

### 🌐 **Online Resources**
- [Python Algorithm Visualizations](https://visualgo.net/)
- [Graph Theory Tutorials](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- [pyamaze Documentation](https://pypi.org/project/pyamaze/)


<div align="center">



## 👨‍💻 Author

**Bagas Pangestu** ([@bagaspng](https://github.com/bagaspng))
  
---

**🌐 Exploring Algorithms, One Path at a Time 🌐**

[![GitHub stars](https://img.shields.io/github/stars/bagaspng/MazeDFSAlgorithm?style=social)](https://github.com/bagaspng/MazeDFSAlgorithm/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/bagaspng/MazeDFSAlgorithm?style=social)](https://github.com/bagaspng/MazeDFSAlgorithm/network/members)

**Made with ❤️ for the Computer Science Community**

</div>
