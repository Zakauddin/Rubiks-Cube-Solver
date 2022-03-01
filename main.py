from vpython import *  # For 3D
import copy


class Cube:
    def __init__(self):
        self.parent = self
        self.rotationApplied = "Initial"
        self.top = [['y', 'y', 'y'],
                    ['y', 'y', 'y'],
                    ['y', 'y', 'y']]

        self.back = [['o', 'o', 'o'],
                     ['o', 'o', 'o'],
                     ['o', 'o', 'o']]

        self.left = [['b', 'b', 'b'],
                     ['b', 'b', 'b'],
                     ['b', 'b', 'b']]

        self.front = [['r', 'r', 'r'],
                      ['r', 'r', 'r'],
                      ['r', 'r', 'r']]

        self.right = [['g', 'g', 'g'],
                      ['g', 'g', 'g'],
                      ['g', 'g', 'g']]

        self.bottom = [['w', 'w', 'w'],
                       ['w', 'w', 'w'],
                       ['w', 'w', 'w']]

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
        if self.top != [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]:
            return False

        if self.back != [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]:
            return False

        if self.left != [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]:
            return False

        if self.front != [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]:
            return False

        if self.right != [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]:
            return False

        if self.bottom != [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]:
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


moveNbr = 0  # Number of movements performed, useful for statistics
fps = 24  # For the visual, number of images per second

# Plot the correspondence between faces and vectors
faces = {'F': (color.red, vector(0, 0, 1)),
         'B': (color.orange, vector(0, 0, -1)),
         'U': (color.yellow, vector(0, 1, 0)),
         'L': (color.blue, vector(-1, 0, 0)),
         'D': (color.white, vector(0, -1, 0)),
         'R': (color.green, vector(1, 0, 0))}

# Put the colors on each small cube, face by face.
stickers = []
for face_color, axis in faces.values():
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            # Start with all the stickers up, then we turn

            sticker = box(color=face_color, pos=vector(x, y, 1.5),
                          length=0.98, height=0.98, width=0.05)
            cos_angle = dot(vector(0, 0, 1), axis)
            pivot = (cross(vector(0, 0, 1), axis) if cos_angle == 0 else vector(1, 0, 0))
            sticker.rotate(angle=acos(cos_angle), axis=pivot, origin=vector(0, 0, 0))
            stickers.append(sticker)


# Rotate parts of the cube in 3 dimensions
def rotate3D(key):
    if key[0] in faces:
        face_color, axis = faces[key[0]]
        angle = ((pi / 2) if len(key) > 1 else -pi / 2)
        for r in arange(0, angle, angle / fps):
            rate(fps)
            for sticker in stickers:
                if dot(sticker.pos, axis) > 0.5:
                    sticker.rotate(angle=angle / fps, axis=axis,
                                   origin=vector(0, 0, 0))
    elif key[0] == 'E':
        axis = vector(0, 0.5, 0)
        angle = ((pi / 2) if len(key) > 1 else -pi / 2)
        for r in arange(0, angle, angle / fps):
            rate(fps)
            for sticker in stickers:
                sticker.rotate(angle=angle / fps, axis=axis, origin=vector(0, 0, 0))
    sleep(1)


cube = Cube()
cube.rotate_back()
rotate3D("B")

cube.rotate_front()
rotate3D("F")

sleep(3)

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
            cube1.rotationApplied = "U"
            cube1.rotate_top()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "D"
            cube1.rotate_bottom()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "L"
            cube1.rotate_left()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "R"
            cube1.rotate_right()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "B"
            cube1.rotate_back()
            queue.append(cube1)

            cube1 = copy.deepcopy(cube)
            cube1.parent = cube
            cube1.rotationApplied = "F"
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
    rotate3D(i.rotationApplied)
    i.print_cube()
    print("")

