# DFSDemo.py
from pyamaze import maze, agent, COLOR

def DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}
    dSearch = []
    while frontier:
        currCell = frontier.pop()
        dSearch.append(currCell)
        if currCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    child = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    child = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    child = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    child = (currCell[0] + 1, currCell[1])
                if child in explored:
                    continue
                explored.append(child)
                frontier.append(child)
                dfsPath[child] = currCell
    # Rekonstruksi path dari start ke goal
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return dSearch, dfsPath, fwdPath

if __name__ == '__main__':
    m = maze()
    m.CreateMaze(loadMaze='dfs_maze.csv')  # Pastikan file ada di folder yang sama

    # Set start dan goal
    start = (1, 1)
    goal = (8, 8)
    m._goal = goal  # Pastikan goal di-set dengan benar

    dSearch, dfsPath, fwdPath = DFS(m, start)

    # Agent akan menelusuri urutan penelusuran DFS (animasi pencarian)
    a = agent(m, start[0], start[1], goal=goal, footprints=True, shape='square', color=COLOR.green)
    m.tracePath({a: dSearch}, showMarked=True)

    # Agent lain menelusuri solusi DFS (path dari start ke goal)
    b = agent(m, start[0], start[1], goal=goal, footprints=True, color=COLOR.yellow)
    m.tracePath({b: fwdPath})

    m.run()
