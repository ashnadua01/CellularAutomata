# rule for iteration
def rule(curr, left, right, up, down, upLeft, upRight, downLeft, downRight):
    sum = left + right + up + down + upLeft + upRight + downLeft + downRight
    if curr == 1:
        if sum > 3:
            return 0
        elif sum < 2:
            return 0
        else:
            return 1
    if curr == 0:
        if sum == 3:
            return 1
        else:
            return 0

# open configuration file
file = open("q2/config.txt", "r")

# reading first line of config file
line = file.readline().strip()
numbers = line.split(" ")

# for gride size and number of initial states
m = int(numbers[0])
n = int(numbers[1])
k = int(numbers[2])

# initializing empty grid as list
grid = []

# appending list to make list of lists 
# i.e. 2d matrix
for i in range(n+2):
    grid.append([0] * (m+2))

# reading remaining of config file,
# for position of the initial states
for i in range(k):
    newLine = file.readline().strip()
    pos = newLine.split(" ")
    col = int(pos[0])
    col = col + 1
    rowBelow = int(pos[1])
    rowBelow = rowBelow + 1
    row = n + 2 - rowBelow
    col = col - 1
    grid[row][col] = 1

#priniting initial grid
print("Initial State:")
for i in range(1, n+1):
        for j in range(1, m+1):
            if grid[i][j] == 1:
                print("X", end="")
            else:
                print("O", end="")
        print()

# taking input of number of iterations
iterations = input("Enter the number of iterations: ")
iterations = int(iterations)

# initializing empty lists to store positions of 
# living and dead cells for each iteration
positionLive = []
positionDead = []

# running loop, till user enters -1
while (iterations != -1):
    # applying rule for each cell
    # in  each iteration
    for a in range(iterations):
        file2 = open("q2/output.txt", "w")
        for i in range(1, n+1):
            for j in range(1, m+1):
                # storing value of all 
                # neighbours of the current cell
                curr = grid[i][j]
                left = grid[i][j-1]
                right = grid[i][j+1]
                up = grid[i-1][j]
                down = grid[i+1][j]
                upLeft = grid[i-1][j-1]
                upRight = grid[i-1][j+1]
                downLeft = grid[i+1][j-1]
                downRight = grid[i+1][j+1]
                # applying rule to the current cell
                check = rule(curr, left, right, up, down, upLeft, upRight, downLeft, downRight)
                if int(check) == 1:
                    x = i
                    y = j
                    tup = (x, y)
                    positionLive.append(tup)
                elif int(check) == 0:
                    x = i
                    y = j
                    tup = (x, y)
                    positionDead.append(tup)
        # making changes, for cells that are 
        # living in the next iteration
        for tup in positionLive:
            x = tup[0]
            y = tup[1]
            grid[x][y] = 1
        positionLive.clear()
        # making changes, for cells that are 
        # dead in the next iteration
        for tup in positionDead:
            x = tup[0]
            y = tup[1]
            grid[x][y] = 0
        positionDead.clear()

        # writing final state, after 
        # iterations to output.txt
        for i in range(1, n+1):
            for j in range(1, m+1):
                if grid[i][j] == 1:
                    file2.write("X")
                else:
                    file2.write("O")
            file2.write('\n')
        file2.close()

    # printing final state, after 
    # iterations on the terminal
    for i in range(1, n+1):
        for j in range(1, m+1):
            if grid[i][j] == 1:
                print("X", end="")
            else:
                print("O", end="")
        print()

    # taking input of iterations
    iterations = input("Enter the number of iterations: ")
    iterations = int(iterations)

file.close()