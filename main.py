import copy


class Cube:
    def __init__(self):
        self.parent = self
        self.rotationApplied = "Initial"
        self.top = [['Y', 'Y', 'Y'],
                    ['Y', 'Y', 'Y'],
                    ['Y', 'Y', 'Y']]

        self.left = [['O', 'O', 'O'],
                     ['O', 'O', 'O'],
                     ['O', 'O', 'O']]

        self.front = [['B', 'B', 'B'],
                      ['B', 'B', 'B'],
                      ['B', 'B', 'B']]

        self.right = [['R', 'R', 'R'],
                      ['R', 'R', 'R'],
                      ['R', 'R', 'R']]

        self.back = [['G', 'G', 'G'],
                     ['G', 'G', 'G'],
                     ['G', 'G', 'G']]

        self.bottom = [['W', 'W', 'W'],
                       ['W', 'W', 'W'],
                       ['W', 'W', 'W']]

    def rotate_right(self):
        temp = [self.front[0][2], self.front[1][2], self.front[2][2]]
        self.front[0][2] = self.bottom[0][2]
        self.front[1][2] = self.bottom[1][2]
        self.front[2][2] = self.bottom[2][2]

        self.bottom[0][2] = self.back[2][0]
        self.bottom[1][2] = self.back[1][0]
        self.bottom[2][2] = self.back[0][0]

        self.back[0][0] = self.top[2][2]
        self.back[1][0] = self.top[1][2]
        self.back[2][0] = self.top[0][2]

        self.top[0][2] = temp[0]
        self.top[1][2] = temp[1]
        self.top[2][2] = temp[2]

        temp1 = [self.right[0][1], self.right[0][2]]
        self.right[0][2] = self.right[0][0]
        self.right[0][1] = self.right[1][0]
        self.right[0][0] = self.right[2][0]
        self.right[1][0] = self.right[2][1]
        self.right[2][0] = self.right[2][2]
        self.right[2][1] = self.right[1][2]
        self.right[2][2] = temp1[1]
        self.right[1][2] = temp1[0]

    def rotate_left(self):
        # front will be overriden by top
        # top will be overriden by back
        # back will be overriden by bottom
        # bottom will be overriden by temp
        # left will be replaced through convention

        temp = [self.front[0][0], self.front[1][0], self.front[2][0]]
        self.front[0][0] = self.top[0][0]
        self.front[1][0] = self.top[1][0]
        self.front[2][0] = self.top[2][0]

        self.top[0][0] = self.back[2][2]
        self.top[1][0] = self.back[1][2]
        self.top[2][0] = self.back[0][2]

        self.back[0][2] = self.bottom[0][0]
        self.back[1][2] = self.bottom[1][0]
        self.back[2][2] = self.bottom[2][0]

        self.bottom[0][0] = temp[0]
        self.bottom[1][0] = temp[1]
        self.bottom[2][0] = temp[2]

        temp1 = [self.left[0][1], self.left[0][2]]
        self.left[0][2] = self.left[0][0]
        self.left[0][1] = self.left[1][0]
        self.left[0][0] = self.left[2][0]
        self.left[1][0] = self.left[2][1]
        self.left[2][0] = self.left[2][2]
        self.left[2][1] = self.left[1][2]
        self.left[2][2] = temp1[1]
        self.left[1][2] = temp1[0]

    def rotate_front(self):
        temp = [self.top[2][0], self.top[2][1], self.top[2][2]]
        self.top[2][0] = self.left[2][2]
        self.top[2][1] = self.left[1][2]
        self.top[2][2] = self.left[0][2]

        self.left[0][2] = self.bottom[0][0]
        self.left[1][2] = self.bottom[0][1]
        self.left[2][2] = self.bottom[0][2]

        self.bottom[0][0] = self.right[0][0]
        self.bottom[0][1] = self.right[1][0]
        self.bottom[0][2] = self.right[2][0]

        self.right[0][0] = temp[0]
        self.right[1][0] = temp[1]
        self.right[2][0] = temp[2]

        temp1 = [self.front[0][1], self.front[0][2]]
        self.front[0][2] = self.front[0][0]
        self.front[0][1] = self.front[1][0]
        self.front[0][0] = self.front[2][0]
        self.front[1][0] = self.front[2][1]
        self.front[2][0] = self.front[2][2]
        self.front[2][1] = self.front[1][2]
        self.front[2][2] = temp1[1]
        self.front[1][2] = temp1[0]

    def rotate_back(self):
        temp = [self.top[0][0], self.top[0][1], self.top[0][2]]
        self.top[0][0] = self.right[0][2]
        self.top[0][1] = self.right[1][2]
        self.top[0][2] = self.right[2][2]

        self.right[0][2] = self.bottom[2][2]
        self.right[1][2] = self.bottom[2][1]
        self.right[2][2] = self.bottom[2][0]

        self.bottom[2][2] = self.left[2][0]
        self.bottom[2][1] = self.left[1][0]
        self.bottom[2][0] = self.left[0][0]

        self.left[0][0] = temp[2]
        self.left[1][0] = temp[1]
        self.left[2][0] = temp[0]

        temp1 = [self.back[0][1], self.back[0][2]]
        self.back[0][2] = self.back[0][0]
        self.back[0][1] = self.back[1][0]
        self.back[0][0] = self.back[2][0]
        self.back[1][0] = self.back[2][1]
        self.back[2][0] = self.back[2][2]
        self.back[2][1] = self.back[1][2]
        self.back[2][2] = temp1[1]
        self.back[1][2] = temp1[0]

    def rotate_top(self):
        temp = [self.front[0][0], self.front[0][1], self.front[0][2]]
        self.front[0][0] = self.right[0][0]
        self.front[0][1] = self.right[0][1]
        self.front[0][2] = self.right[0][2]

        self.right[0][0] = self.back[0][0]
        self.right[0][1] = self.back[0][1]
        self.right[0][2] = self.back[0][2]

        self.back[0][0] = self.left[0][0]
        self.back[0][1] = self.left[0][1]
        self.back[0][2] = self.left[0][2]

        self.left[0][0] = temp[0]
        self.left[0][1] = temp[1]
        self.left[0][2] = temp[2]

        temp1 = [self.top[0][1], self.top[0][2]]
        self.top[0][2] = self.top[0][0]
        self.top[0][1] = self.top[1][0]
        self.top[0][0] = self.top[2][0]
        self.top[1][0] = self.top[2][1]
        self.top[2][0] = self.top[2][2]
        self.top[2][1] = self.top[1][2]
        self.top[2][2] = temp1[1]
        self.top[1][2] = temp1[0]

    def rotate_bottom(self):
        temp = [self.front[2][0], self.front[2][1], self.front[2][2]]
        self.front[2][0] = self.left[2][0]
        self.front[2][1] = self.left[2][1]
        self.front[2][2] = self.left[2][2]

        self.left[2][0] = self.back[2][0]
        self.left[2][1] = self.back[2][1]
        self.left[2][2] = self.back[2][2]

        self.back[2][0] = self.right[2][0]
        self.back[2][1] = self.right[2][1]
        self.back[2][2] = self.right[2][2]

        self.right[2][0] = temp[0]
        self.right[2][1] = temp[1]
        self.right[2][2] = temp[2]

        temp1 = [self.bottom[0][1], self.bottom[0][2]]
        self.bottom[0][2] = self.bottom[0][0]
        self.bottom[0][1] = self.bottom[1][0]
        self.bottom[0][0] = self.bottom[2][0]
        self.bottom[1][0] = self.bottom[2][1]
        self.bottom[2][0] = self.bottom[2][2]
        self.bottom[2][1] = self.bottom[1][2]
        self.bottom[2][2] = temp1[1]
        self.bottom[1][2] = temp1[0]

    def is_solved(self):
        if self.top != [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]:
            return False

        if self.left != [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]:
            return False

        if self.front != [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]:
            return False

        if self.right != [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]:
            return False

        if self.back != [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]:
            return False

        if self.bottom != [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]:
            return False

        return True

    def compare(self, obj):
        if self.top != obj.top:
            return False

        if self.left != obj.left:
            return False

        if self.front != obj.front:
            return False

        if self.right != obj.right:
            return False

        if self.back != obj.back:
            return False

        if self.bottom != obj.bottom:
            return False

        return True

    def print_cube(self):

        for row in range(0, 3):
            print("                  ", self.top[row])

        print()

        for row in range(0, 3):
            print(self.left[row], "  ", self.front[row], "  ", self.right[row], "  ", self.back[row], "  ")

        print()

        for row in range(0, 3):
            print("                  ", self.bottom[row])


cube = Cube()

cube.rotate_back()
cube.rotate_right()


queue = []
alreadyVisitedArray = []
queue.append(cube)

done = False
while not done:
    cube = queue.pop(0)

    if cube.is_solved():
        done = True
        print("Queue length: ", len(queue))
    else:

        alreadyVisited = False
        if alreadyVisitedArray:
            for i in alreadyVisitedArray:
                if cube.compare(i):
                    alreadyVisited = True

        if not alreadyVisited:
            alreadyVisitedArray.append(cube)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "Top"
            cube1.rotate_top()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "Bottom"
            cube1.rotate_bottom()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "Left"
            cube1.rotate_left()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "Right"
            cube1.rotate_right()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "Back"
            cube1.rotate_back()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "Front"
            cube1.rotate_front()
            queue.append(cube1)

print("Solution Found")

solution = []
while cube.rotationApplied != "Initial":
    solution.insert(0, cube)
    cube = cube.parent

solution.insert(0, cube)

for i in solution:
    print(i.rotationApplied)
    i.print_cube()
    print("")
