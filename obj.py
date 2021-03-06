import struct

def color(r, g, b):
  return bytes([b, g, r])


def try_int_minus1(s, base=10, val=None):
  try:
    return int(s, base) - 1
  except ValueError:
    return val


class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        self.vertices = []
        self.tvertices = []
        self.normals = []
        self.faces = []
        self.read()

    def read(self):
        for line in self.lines:
            if line:
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    prefix = ''
                if prefix == 'v':
                    #print(line)
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'vt':
                    #print(value)
                    res = list(map(float, value.split(' ')))
                    '''if len(res) == 2:
                        res.append(0.00)'''
                    self.tvertices.append(res)
                elif prefix == 'vn': #normales
                    self.normals.append(list(map(float,value.split(' '))))
                elif prefix == 'f':
                    self.faces.append([list(map(try_int_minus1, face.split('/'))) for face in value.split(' ')])

class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        #Lectura de archivo bmp
        image = open(self.path, "rb")
        image.seek(2 + 4 + 4)
        header_size = struct.unpack('=l', image.read(4))[0]
        image.seek(2 + 4 + 4 + 4 + 4)
        self.width = struct.unpack('=l', image.read(4))[0]
        self.height = struct.unpack('=l', image.read(4))[0]
        image.seek(header_size)

        self.framebuffer = []

        for y in range(self.height):
            self.framebuffer.append([])
            for x in range(self.width):
                b = ord(image.read(1))
                g = ord(image.read(1))
                r = ord(image.read(1))
                self.framebuffer[y].append(color(r, g, b))
        image.close()
        

    def get_color(self, tx, ty, intensity=1):
        #Valor que corresponde a la coordenada
        x = int(tx * self.width)
        y = int(ty * self.height)
        #no numpy
        try:
            return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.framebuffer[y][x]))
        except:
            pass