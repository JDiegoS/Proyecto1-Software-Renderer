#Juan Diego Solorzano 18151
#Proyecto 1

import random
import math
from obj import Obj, Texture
from lib import *

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
white = bytes([255, 255, 255])
black = bytes([0, 0, 0])

class Render(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clearC = black
        self.current_color = white
        self.glClear()
        self.light = V3(0,0,1)
        self.active_texture = None
        self.active_vertex_array = []

    def glInit(self, width, height):
        return

    #Area para pintar
    def glViewPort(self, x, y, width, height):
        self.xw = x
        self.yw = y
        self.widthw = width
        self.heightw = height

    #Pintar imagen   
    def glClear(self):
        self.framebuffer = [
            [black for x in range(self.width)]
            for y in range(self.height)
        ]
        self.zbuffer = [[-float('inf') for x in range(self.width)] for y in range(self.height)]

    #Color para pintar imagen
    def glClearColor(self, r, g, b):
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        self.clearC = bytes([b, g, r])
        self.glClear()

    #Crear archivo de la imagen
    def glFinish(self, filename):
        writebmp(filename, self.width, self.height, self.framebuffer)

    def display(self, filename='out.bmp'):
        """
        Displays the image, a external library (wand) is used, but only for convenience during development
        """
        self.glFinish(filename)

        try:
            from wand.image import Image
            from wand.display import display

            with Image(filename=filename) as image:
                display(image)
        except ImportError:
            pass  # do nothing if no wand is installed

    def set_color(self, color):
        self.current_color = color

    #Pintar punto
    def glVertex(self, x, y, color = None):
        try:
            self.framebuffer[y][x] = color or self.current_color
        except:
            pass

    def triangle(self):
        A = next(self.active_vertex_array)
        B = next(self.active_vertex_array)
        C = next(self.active_vertex_array)



        if self.active_texture:
            tA = next(self.active_vertex_array)
            tB = next(self.active_vertex_array)
            tC = next(self.active_vertex_array)

        bbox_min, bbox_max = bbox(A, B, C)

        normal = norm(cross(sub(B, A), sub(C, A)))
        intensity = dot(normal, self.light)
        if intensity < 0:
            return

        for x in range(int(bbox_min.x), int(bbox_max.x + 1)):
            for y in range(int(bbox_min.y), int(bbox_max.y + 1)):
                w, v, u = barycentric(A, B, C, V2(x, y))
                if w < 0 or v < 0 or u < 0:  # 0 is actually a valid value! (it is on the edge)
                    continue

                if self.active_texture:
                  tx = tA.x * w + tB.x * u + tC.x *v
                  ty = tA.y * w + tB.y * u + tC.y * v

                  #print(tx)
                  #print(ty)

                  color = self.active_texture.get_color(tx, ty, intensity)
                  #print(color)
                else:
                  
                  color = white
                z = A.z * w + B.z * v + C.z * u

                if x < 0 or y < 0:
                    continue

                if x < len(self.zbuffer) and y < len(self.zbuffer[x]) and z > self.zbuffer[x][y]:
                    self.glVertex(x, y, color)
                    self.zbuffer[x][y] = z

    def transform(self, vertex):
        augmented_vertex = [
        [vertex.x],
        [vertex.y],
        [vertex.z],
        [1]
        ]
        transformed_vertex = matrixMul(self.Projection, self.Viewport)
        transformed_vertex = matrixMul(transformed_vertex, self.View)
        transformed_vertex = matrixMul(transformed_vertex, self.Model)
        transformed_vertex = matrixMul(transformed_vertex, augmented_vertex)

        transformed_vertex = [
            transformed_vertex[0][0],
            transformed_vertex[1][0],
            transformed_vertex[2][0]
        ]

        return V3(*transformed_vertex)

    def load(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
        self.loadModelMatrix(translate, scale, rotate)

        model = Obj(filename)
        vertex_buffer_object = []

        for face in model.faces:
            for facepart in face:
                vertex = self.transform(V3(*model.vertices[facepart[0]]))
                vertex_buffer_object.append(vertex)

            if self.active_texture:
                for facepart in face:
                    tvertex = V3(*model.tvertices[facepart[1]])
                    vertex_buffer_object.append(tvertex)

        self.active_vertex_array = iter(vertex_buffer_object)

    def loadModelMatrix(self, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
        translate = V3(*translate)
        scale = V3(*scale)
        rotate = V3(*rotate)

        translation_matrix = [
        [1, 0, 0, translate.x],
        [0, 1, 0, translate.y],
        [0, 0, 1, translate.z],
        [0, 0, 0, 1],
        ]


        a = rotate.x
        rotation_matrix_x = [
        [1, 0, 0, 0],
        [0, math.cos(a), -math.sin(a), 0],
        [0, math.sin(a),  math.cos(a), 0],
        [0, 0, 0, 1]
        ]

        a = rotate.y
        rotation_matrix_y = [
        [math.cos(a), 0,  math.sin(a), 0],
        [     0, 1,       0, 0],
        [-math.sin(a), 0,  math.cos(a), 0],
        [     0, 0,       0, 1]
        ]

        a = rotate.z
        rotation_matrix_z = [
        [math.cos(a), -math.sin(a), 0, 0],
        [math.sin(a),  math.cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
        ]
        rotation_matrix = matrixMul(rotation_matrix_x, rotation_matrix_y)
        rotation_matrix = matrixMul(rotation_matrix, rotation_matrix_z)
        scale_matrix = [
        [scale.x, 0, 0, 0],
        [0, scale.y, 0, 0],
        [0, 0, scale.z, 0],
        [0, 0, 0, 1],
        ]

        result_matrix = matrixMul(translation_matrix, rotation_matrix)
        result_matrix = matrixMul(result_matrix, scale_matrix)
        self.Model = result_matrix

    def loadViewMatrix(self, x, y, z, center):
        M = [
        [x.x, x.y, x.z,  0],
        [y.x, y.y, y.z, 0],
        [z.x, z.y, z.z, 0],
        [0,     0,   0, 1]
        ]

        O = [
        [1, 0, 0, -center.x],
        [0, 1, 0, -center.y],
        [0, 0, 1, -center.z],
        [0, 0, 0, 1]
        ]

        self.View = matrixMul(M, O)

    def loadProjectionMatrix(self, coeff):
        self.Projection =  [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, coeff, 1]
        ]

    def loadViewportMatrix(self, x = 0, y = 0):
        self.Viewport =  [
        [self.width/2, 0, 0, x + self.width/2],
        [0, self.height/2, 0, y + self.height/2],
        [0, 0, 128, 128],
        [0, 0, 0, 1]
        ]

    def lookAt(self, eye, center, up):
        z = norm(sub(eye, center))
        x = norm(cross(up, z))
        y = norm(cross(z, x))
        self.loadViewMatrix(x, y, z, center)
        self.loadProjectionMatrix(-1 / length(sub(eye, center)))
        self.loadViewportMatrix()

    def draw_arrays(self, polygon):
        if polygon == 'TRIANGLES':
            try:
                while True:
                    self.triangle()
            except StopIteration:
                print('Done.')