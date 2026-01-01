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

### 🧪 **Experimental Features**

#### 🔬 **Algorithm Comparison**

```python
def compare_algorithms(maze):
    """Bandingkan DFS dengan algoritma lain"""
    
    # DFS Implementation
    dfs_start = time.time()
    dfs_path = DFS(maze)
    dfs_time = time. time() - dfs_start
    
    # BFS Implementation (for comparison)
    bfs_start = time.time()
    bfs_path = BFS(maze)  # Need to implement
    bfs_time = time.time() - bfs_start
    
    comparison = {
        'DFS': {
            'time':  dfs_time,
            'path_length': len(dfs_path),
            'nodes_explored': len(dfs_search)
        },
        'BFS': {
            'time': bfs_time, 
            'path_length': len(bfs_path),
            'nodes_explored': len(bfs_search)
        }
    }
    
    return comparison
```

#### 📈 **Statistics Tracking**

```python
class DFSAnalyzer:
    def __init__(self):
        self.stats = {
            'total_moves': 0,
            'backtrack_count': 0,
            'dead_ends_found': 0,
            'max_depth_reached': 0
        }
    
    def track_move(self, from_cell, to_cell):
        self.stats['total_moves'] += 1
        # Track other metrics
    
    def generate_report(self):
        return {
            'efficiency': self.calculate_efficiency(),
            'exploration_pattern': self.analyze_pattern(),
            'performance_metrics': self. stats
        }
```

## 🎨 Visualization Options

### 🎭 **Color Schemes**

```python
# Predefined color schemes
COLOR_SCHEMES = {
    'classic': {
        'search': COLOR.green,
        'solution': COLOR.yellow,
        'wall': COLOR.black,
        'path': COLOR.white
    },
    'ocean': {
        'search': COLOR.blue, 
        'solution': COLOR.cyan,
        'wall': COLOR.dark_blue,
        'path': COLOR.light_blue
    },
    'fire': {
        'search': COLOR.red,
        'solution': COLOR.orange,
        'wall':  COLOR.black,
        'path': COLOR.yellow
    }
}
```

### 🎬 **Animation Controls**

```python
def animated_dfs(maze, delay=100):
    """DFS dengan kontrol animasi custom"""
    
    search_agent = agent(maze, x, y, 
                        footprints=True,
                        color=COLOR.green)
    
    # Control animation speed
    maze.tracePath({search_agent: dfs_search}, 
                  delay=delay,          # ms delay between moves
                  showMarked=True,      # Highlight decision points
                  kill=False)           # Keep previous trails
    
    maze.run()
```

## 🚀 Extensions & Improvements

### 🔮 **Future Enhancements**

- [ ] **Web Interface** - Flask/Django web version
- [ ] **3D Maze** - Three-dimensional maze solving
- [ ] **Real-time Editing** - Interactive maze creation
- [ ] **Multiple Algorithms** - BFS, A*, Dijkstra comparison
- [ ] **AI Enhancement** - Machine learning optimization
- [ ] **Mobile App** - Android/iOS implementation
- [ ] **Multiplayer Mode** - Competitive maze solving
- [ ] **VR Integration** - Virtual reality maze experience

### 🎯 **Performance Optimizations**

```python
# Optimized DFS dengan set operations
def optimized_dfs(maze, start):
    explored = {start}  # Set for O(1) lookup
    frontier = [start]  # List for stack operations
    parent = {start: None}
    
    while frontier:
        current = frontier.pop()
        
        if current == maze._goal:
            return reconstruct_path(parent, start, current)
        
        for neighbor in get_neighbors(maze, current):
            if neighbor not in explored:
                explored.add(neighbor)  # O(1) operation
                frontier.append(neighbor)
                parent[neighbor] = current
```

## 📊 Benchmarking

### 🏃‍♂️ **Performance Tests**

```python
def benchmark_maze_sizes():
    """Benchmark DFS performance on different maze sizes"""
    
    sizes = [5, 10, 15, 20, 25, 30, 35, 40]
    results = []
    
    for size in sizes: 
        maze_obj = maze(size, size)
        maze_obj.CreateMaze()
        
        # Run multiple times for average
        times = []
        for _ in range(5):
            start_time = time.perf_counter()
            DFS(maze_obj)
            end_time = time.perf_counter()
            times.append(end_time - start_time)
        
        avg_time = sum(times) / len(times)
        results.append({
            'size': size,
            'avg_time': avg_time,
            'nodes': size * size
        })
    
    return results
```

## 🤝 Contributing

Contributions welcome! Here's how to contribute:

### 🔄 **Development Setup**

```bash
# Fork repository
git clone https://github.com/your-username/MazeDFSAlgorithm.git
cd MazeDFSAlgorithm

# Create development environment
python -m venv dfs_env
source dfs_env/bin/activate  # On Windows: dfs_env\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
```

### 📋 **Contribution Guidelines**

```python
# Code style guidelines
# 1. Follow PEP 8
# 2. Add type hints
def DFS(maze:  Maze, start: Optional[Tuple[int, int]] = None) -> Tuple[List, Dict, Dict]:
    """
    Depth-First Search algorithm for maze solving.
    
    Args: 
        maze: Maze object from pyamaze
        start: Starting position (row, col). If None, uses (rows, cols)
    
    Returns: 
        Tuple of (search_order, dfs_path, forward_path)
    """
    pass

# 3. Add comprehensive docstrings
# 4. Include unit tests
```

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

### 💡 **Enhancement Ideas**

- [ ] **Algorithm Variants** - Iterative deepening DFS
- [ ] **Maze Types** - Hexagonal, triangular mazes
- [ ] **Pathfinding Metrics** - Path quality analysis
- [ ] **Interactive Features** - Real-time parameter tuning
- [ ] **Educational Mode** - Step-by-step explanation
- [ ] **Performance Profiler** - Memory and time analysis

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Bagas Pangestu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software")...
```

## 👨‍💻 Author

**Bagas Pangestu** ([@bagaspng](https://github.com/bagaspng))

- 📧 Email: bagaspangestu0407@gmail.com
- 💼 LinkedIn: [Bagas Pangestu](https://linkedin.com/in/bagaspng)
- 🌐 Portfolio: [bagaspng.dev](https://bagaspng.dev)
- 🎓 Expertise: Algorithms, Data Structures, AI/ML

## 🙏 Acknowledgments

- **pyamaze Library** - Fantastic visualization framework
- **Python Community** - Continuous support and resources
- **Algorithm Researchers** - Foundational work on graph algorithms
- **Open Source Contributors** - Inspiration and best practices

## 📚 References

### 📖 **Academic Papers**
- Tarjan, R. (1972). "Depth-First Search and Linear Graph Algorithms"
- Cormen, T. H., et al. (2009). "Introduction to Algorithms, 3rd Edition"

### 🌐 **Online Resources**
- [Python Algorithm Visualizations](https://visualgo.net/)
- [Graph Theory Tutorials](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- [pyamaze Documentation](https://pypi.org/project/pyamaze/)

## 📞 Support

Need help? Contact us:

- 📖 **Documentation**: [Project Wiki](https://github.com/bagaspng/MazeDFSAlgorithm/wiki)
- 🐛 **Issues**: [Report Bugs](https://github.com/bagaspng/MazeDFSAlgorithm/issues)
- 💬 **Discussions**: [Q&A Forum](https://github.com/bagaspng/MazeDFSAlgorithm/discussions)
- 📧 **Email**: bagaspangestu0407@gmail.com

---

<div align="center">

**🌐 Exploring Algorithms, One Path at a Time 🌐**

[![GitHub stars](https://img.shields.io/github/stars/bagaspng/MazeDFSAlgorithm?style=social)](https://github.com/bagaspng/MazeDFSAlgorithm/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/bagaspng/MazeDFSAlgorithm?style=social)](https://github.com/bagaspng/MazeDFSAlgorithm/network/members)

**Made with ❤️ for the Computer Science Community**

</div>
