def WaterJogBFS(initStat, goalStat):
    Nodes = []
    visited = []
    Nodes.append((initStat[0], initStat[1], ''))
    visited.append(initStat)
    while Nodes:
	pair = Nodes.pop(0)
	if (pair[0], pair[1]) == goalStat:
	    return pair[2]
	visited.append((pair[0], pair[1]))
	children = GenerateChildren(pair[0], pair[1], pair[2])
	for i in children:
	    temp = (i[0], i[1])
	    if not temp in visited:
		Nodes.append(i)
    return 'Not Found'
    
def WaterJogDFS(initStat, goalStat, path, visited):
    if initStat == goalStat:
	return path
    children = GenerateChildren(initStat[0], initStat[1], path)
    for i in children:
	temp = (i[0], i[1])
	if not temp in visited:
	    visited.append(temp)
	    path = WaterJogDFS(temp, goalStat, i[2], visited)
	    if path:
		return path
    return ''
				
def GenerateChildren(x, y, tree):
    chld = []
    if x < 4:
	chld.append((4, y, tree + ' 1'))
    if y < 3:
	chld.append((x, 3, tree + ' 2'))
    if x > 0:
	chld.append((0, y, tree + ' 3'))
    if y > 0:
	chld.append((x, 0, tree + ' 4'))
    if x+y >= 4 and y >= 0:
	chld.append((4, y-(4-x), tree + ' 5'))
    if x+y >= 3 and x > 0:
	chld.append((x-(3-y), 3, tree + ' 6'))
    if x+y <= 4 and y > 0:
	chld.append((x+y, 0, tree + ' 7'))
    if x+y <= 3 and x > 0:
	chld.append((0, x+y, tree + ' 8'))
    if x == 0 and y == 2:
	chld.append((y, x, tree + ' 9'))
    if x == 2:
	chld.append((0, y, tree + ' 10'))
    return chld


if __name__ == '__main__':
    init = (0, 0)
    goal = (2, 0)
    v = []
    print 'Breadth First Search Applied Rules:', WaterJogBFS(init, goal)
    print 'Depth First Search Applied Rules:', WaterJogDFS(init, goal, '', v)
    
    
    