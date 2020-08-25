from collections import deque
from random import randint
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Cube:
    def __init__(self):
        # Create a new cube in a fresh state. Each key represents an index for a tile on the
        # respective face for that dictionary. Tiles are numbered 1-9 from top-left to
        # bottom-right.
        self.white_face = ['white' for tile in range(9)]
        self.green_face = ['green' for tile in range(9)]
        self.orange_face = ['orange' for tile in range(9)]
        self.blue_face = ['blue' for tile in range(9)]
        self.red_face = ['red' for tile in range(9)]
        self.yellow_face = ['yellow' for tile in range(9)]
        self.input_translator = {'white': self.white_face, 'green': self.green_face, 'orange': self.orange_face,
                                 'blue': self.blue_face, 'red': self.red_face, 'yellow': self.yellow_face}

    def reset(self):
        self.white_face = ['white' for tile in range(9)]
        self.green_face = ['green' for tile in range(9)]
        self.orange_face = ['orange' for tile in range(9)]
        self.blue_face = ['blue' for tile in range(9)]
        self.red_face = ['red' for tile in range(9)]
        self.yellow_face = ['yellow' for tile in range(9)]
        print('Cube reset to solved state.')

    # Rotation logic for tiles local to selected face. Defined for later use within
    # the full rotation algorithm.

    def local_rotate(self, face):
        # Selecting the indexes of the tiles associated with this move.
        from_face_idx = [0, 1, 2, 5, 8, 7, 6, 3]
        to_face_idx = deque(from_face_idx.copy())
        to_face_idx.rotate(-2)
        selected_face = self.input_translator[face]
        # Making a copy of the current face state for the associated tiles with this move.
        temp_face_copy = [selected_face[i] for i in from_face_idx]
        # Update the value at each tile into its rotated state.
        for i in range(len(from_face_idx)):
            selected_face[to_face_idx[i]] = temp_face_copy[i]

    def rotate(self, face):
        # Rotating the tiles local to this face.
        self.local_rotate(face)
        selected_face = self.input_translator[face]
        # Updating values for associated tiles around the edges.
        if face == 'white':
            print('***ROTATING WHITE FACE***')
            self.green_face[8], self.green_face[5], self.green_face[2], self.orange_face[6], self.orange_face[7], self.orange_face[8], self.blue_face[0], self.blue_face[3], self.blue_face[6], self.red_face[2], self.red_face[1], self.red_face[
                0] = self.red_face[2], self.red_face[1], self.red_face[0], self.green_face[8], self.green_face[5], self.green_face[2], self.orange_face[6], self.orange_face[7], self.orange_face[8], self.blue_face[0], self.blue_face[3], self.blue_face[6]
        elif face == 'green':
            print('***ROTATING GREEN FACE***')
            self.yellow_face[8], self.yellow_face[5], self.yellow_face[2], self.orange_face[0], self.orange_face[3], self.orange_face[6], self.white_face[0], self.white_face[3], self.white_face[6], self.red_face[0], self.red_face[3], self.red_face[
                6] = self.red_face[0], self.red_face[3], self.red_face[6], self.yellow_face[8], self.yellow_face[5], self.yellow_face[2], self.orange_face[0], self.orange_face[3], self.orange_face[6], self.white_face[0], self.white_face[3], self.white_face[6]
        elif face == 'orange':
            print('***ROTATING ORANGE FACE***')
            self.green_face[2], self.green_face[1], self.green_face[0], self.yellow_face[2], self.yellow_face[1], self.yellow_face[0], self.blue_face[2], self.blue_face[1], self.blue_face[0], self.white_face[2], self.white_face[1], self.white_face[
                0] = self.white_face[2], self.white_face[1], self.white_face[0], self.green_face[2], self.green_face[1], self.green_face[0], self.yellow_face[2], self.yellow_face[1], self.yellow_face[0], self.blue_face[2], self.blue_face[1], self.blue_face[0]
        elif face == 'blue':
            print('***ROTATING BLUE FACE***')
            self.white_face[8], self.white_face[5], self.white_face[2], self.orange_face[8], self.orange_face[5], self.orange_face[2], self.yellow_face[0], self.yellow_face[3], self.yellow_face[6], self.red_face[8], self.red_face[5], self.red_face[
                2] = self.red_face[8], self.red_face[5], self.red_face[2], self.white_face[8], self.white_face[5], self.white_face[2], self.orange_face[8], self.orange_face[5], self.orange_face[2], self.yellow_face[0], self.yellow_face[3], self.yellow_face[6]
        elif face == 'red':
            print('***ROTATING RED FACE***')
            self.green_face[6], self.green_face[7], self.green_face[8], self.white_face[6], self.white_face[7], self.white_face[8], self.blue_face[6], self.blue_face[7], self.blue_face[8], self.yellow_face[6], self.yellow_face[7], self.yellow_face[
                8] = self.yellow_face[6], self.yellow_face[7], self.yellow_face[8], self.green_face[6], self.green_face[7], self.green_face[8], self.white_face[6], self.white_face[7], self.white_face[8], self.blue_face[6], self.blue_face[7], self.blue_face[8]
        elif face == 'yellow':
            print('***ROTATING YELLOW FACE***')
            self.blue_face[8], self.blue_face[5], self.blue_face[2], self.orange_face[2], self.orange_face[1], self.orange_face[0], self.green_face[0], self.green_face[3], self.green_face[6], self.red_face[6], self.red_face[7], self.red_face[
                8] = self.red_face[6], self.red_face[7], self.red_face[8], self.blue_face[8], self.blue_face[5], self.blue_face[2], self.orange_face[2], self.orange_face[1], self.orange_face[0], self.green_face[0], self.green_face[3], self.green_face[6]
        else:
            print('Please type one of the following options: \'white\', \'green\', \'orange\', \'blue\', \'red\' or \'yellow\'.')

    def counter_rotate(self, face):
        # Rotating values local to this face.
        for i in range(3):
            self.local_rotate(face)
        # Updating values for associated tiles around the edges.
        if face == 'white':
            print('***ROTATING WHITE FACE COUNTER-CLOCKWISE***')
            self.red_face[2], self.red_face[1], self.red_face[0], self.green_face[8], self.green_face[5], self.green_face[2], self.orange_face[6], self.orange_face[7], self.orange_face[8], self.blue_face[0], self.blue_face[3], self.blue_face[
                6] = self.green_face[8], self.green_face[5], self.green_face[2], self.orange_face[6], self.orange_face[7], self.orange_face[8], self.blue_face[0], self.blue_face[3], self.blue_face[6], self.red_face[2], self.red_face[1], self.red_face[0]
        elif face == 'green':
            print('***ROTATING GREEN FACE COUNTER-CLOCKWISE***')
            self.red_face[0], self.red_face[3], self.red_face[6], self.yellow_face[8], self.yellow_face[5], self.yellow_face[2], self.orange_face[0], self.orange_face[3], self.orange_face[6], self.white_face[0], self.white_face[3], self.white_face[
                6] = self.yellow_face[8], self.yellow_face[5], self.yellow_face[2], self.orange_face[0], self.orange_face[3], self.orange_face[6], self.white_face[0], self.white_face[3], self.white_face[6], self.red_face[0], self.red_face[3], self.red_face[6]
        elif face == 'orange':
            print('***ROTATING ORANGE FACE COUNTER-CLOCKWISE***')
            self.white_face[2], self.white_face[1], self.white_face[0], self.green_face[2], self.green_face[1], self.green_face[0], self.yellow_face[2], self.yellow_face[1], self.yellow_face[0], self.blue_face[2], self.blue_face[1], self.blue_face[
                0] = self.green_face[2], self.green_face[1], self.green_face[0], self.yellow_face[2], self.yellow_face[1], self.yellow_face[0], self.blue_face[2], self.blue_face[1], self.blue_face[0], self.white_face[2], self.white_face[1], self.white_face[0]
        elif face == 'blue':
            print('***ROTATING BLUE FACE COUNTER-CLOCKWISE***')
            self.red_face[8], self.red_face[5], self.red_face[2], self.white_face[8], self.white_face[5], self.white_face[2], self.orange_face[8], self.orange_face[5], self.orange_face[2], self.yellow_face[0], self.yellow_face[3], self.yellow_face[
                6] = self.white_face[8], self.white_face[5], self.white_face[2], self.orange_face[8], self.orange_face[5], self.orange_face[2], self.yellow_face[0], self.yellow_face[3], self.yellow_face[6], self.red_face[8], self.red_face[5], self.red_face[2]
        elif face == 'red':
            print('***ROTATING RED FACE COUNTER-CLOCKWISE***')
            self.yellow_face[6], self.yellow_face[7], self.yellow_face[8], self.green_face[6], self.green_face[7], self.green_face[8], self.white_face[6], self.white_face[7], self.white_face[8], self.blue_face[6], self.blue_face[7], self.blue_face[
                8] = self.green_face[6], self.green_face[7], self.green_face[8], self.white_face[6], self.white_face[7], self.white_face[8], self.blue_face[6], self.blue_face[7], self.blue_face[8], self.yellow_face[6], self.yellow_face[7], self.yellow_face[8]
        elif face == 'yellow':
            print('***ROTATING YELLOW FACE COUNTER-CLOCKWISE***')
            self.red_face[6], self.red_face[7], self.red_face[8], self.blue_face[8], self.blue_face[5], self.blue_face[2], self.orange_face[2], self.orange_face[1], self.orange_face[0], self.green_face[0], self.green_face[3], self.green_face[
                6] = self.blue_face[8], self.blue_face[5], self.blue_face[2], self.orange_face[2], self.orange_face[1], self.orange_face[0], self.green_face[0], self.green_face[3], self.green_face[6], self.red_face[6], self.red_face[7], self.red_face[8]
        else:
            print('Please type one of the following options: \'white\', \'green\', \'orange\', \'blue\', \'red\' or \'yellow\'.')

    def scramble(self):
        # Dictionary used to interpret RNG output into a colour face.
        colour_dict = {0: 'white', 1: 'green',
                       2: 'orange', 3: 'blue', 4: 'red', 5: 'yellow'}
        for i in range(20):
            rotation = randint(0, 1)
            colour = colour_dict[randint(0, 5)]
            if rotation == 0:
                self.rotate(colour)
            else:
                self.counter_rotate(colour)


my_cube = Cube()

##################
# Making interface
##################


def build_vertices_front(x = 0, y = 3, z = 0):
    vertices = []
    for row in range(3):
        for tile in range(3):
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x += 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            y -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x += 1
            y += 1
        x -= 3
        y -= 1
    return vertices

def build_vertices_right(x = 3, y = 3, z = 0):
    vertices = []
    for row in range(3):
        for tile in range(3):
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            z -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            y -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            z += 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            z -= 1
            y += 1
        z += 3
        y -= 1
    return vertices

def build_vertices_left(x = 0, y = 3, z = -3):
    vertices = []
    for row in range(3):
        for tile in range(3):
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            z += 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            y -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            z -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            z += 1
            y += 1
        z -= 3
        y -= 1
    return vertices

def build_vertices_top(x = 0, y = 3, z = -3):
    vertices = []
    for row in range(3):
        for tile in range(3):
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x += 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            z += 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x += 1
            z -= 1
        x -= 3
        z += 1
    return vertices

def build_vertices_bottom(x = 0, y = 0, z = 0):
    vertices = []
    for row in range(3):
        for tile in range(3):
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x += 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            z -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x += 1
            z += 1
        x -= 3
        z -= 1
    return vertices

def build_vertices_back(x = 3, y = 3, z = -3):
    vertices = []
    for row in range(3):
        for tile in range(3):
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            y -= 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x += 1
            current_vertex = [x, y, z]
            vertices.append(current_vertex)
            x -= 1
            y += 1
        x += 3
        y -= 1
    return vertices


def build_vertices():
    vertices = []
    front = build_vertices_front()
    right = build_vertices_right()
    left = build_vertices_left()
    top = build_vertices_top()
    bottom = build_vertices_bottom()
    back = build_vertices_back()
    vertices += front
    vertices += right
    vertices += left
    vertices += top
    vertices += bottom
    vertices += back
    return vertices

def build_edges(vertices):
    vert_total = len(vertices)
    i = 0
    edges = []
    while i < vert_total:
        current_edge = [i, i+1]
        edges.append(current_edge)
        current_edge = [i, i+3]
        edges.append(current_edge)
        current_edge = [i+1, i+2]
        edges.append(current_edge)
        current_edge = [i+2, i+3]
        edges.append(current_edge)
        i += 4
    return edges

def build_faces(vertices):
    vertex_list = list(range(len(vertices)))
    faces = []
    i = 0
    while i < len(vertices):
        faces.append(vertex_list[i:i+4])
        i += 4
    return faces


vertices = build_vertices()

edges = build_edges(vertices)

faces = build_faces(vertices)


colours = ((1, 1, 1), (0, 1, 0), (1, 0.5, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1), )
three_colours = (
    (0, 1, 0), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 0, 0),
    (0, 1, 0), (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1), (1, 0, 0),
    (0, 1, 0), (0.168, 0.592, 0.286), (0.168, 0.592, 0.286), (0.168, 0.592, 0.286), (0.168, 0.592, 0.286), (0.168, 0.592, 0.286), (0.168, 0.592, 0.286), (0.168, 0.592, 0.286), (1, 0, 0),
    (0, 1, 0), (0.984, 0.588, 0.054), (0.984, 0.588, 0.054), (0.984, 0.588, 0.054), (0.984, 0.588, 0.054), (0.984, 0.588, 0.054), (0.984, 0.588, 0.054), (0.984, 0.588, 0.054), (1, 0, 0),
    (0, 1, 0), (0.623, 0.164, 0.015), (0.623, 0.164, 0.015), (0.623, 0.164, 0.015), (0.623, 0.164, 0.015), (0.623, 0.164, 0.015), (0.623, 0.164, 0.015), (0.623, 0.164, 0.015), (1, 0, 0),
    (0, 1, 0), (1, 0.933, 0.2), (1, 0.933, 0.2), (1, 0.933, 0.2), (1, 0.933, 0.2), (1, 0.933, 0.2), (1, 0.933, 0.2), (1, 0.933, 0.2), (1, 0, 0),
    )
edge_colour = (0, 0, 0)


def cube_display():
    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv(edge_colour)
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    x = 0
    for face in faces:
        glColor3fv(three_colours[x])
        x += 1
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-1.5, -1.5, -15)
    glRotatef(0, 0, 0, 0)
    glClearColor(0, 0.1, 0.1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 1, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube_display()
        pygame.display.flip()
        pygame.time.wait(10)


main()
