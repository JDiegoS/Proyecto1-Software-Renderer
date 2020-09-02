#Juan Diego Solorzano 18151
#Proyecto 1
from gl import *

r = Render(800, 800)
r.light = V3(0, 0, 1)

#Background
r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
t = Texture('./models/house.bmp')
r.active_texture = t
r.framebuffer = t.framebuffer

#Soccer ball
r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
t = Texture('./models/ball2.bmp')
r.active_texture = t
r.load('./models/sphere.obj', translate=(0.08, -0.72, 0), scale=(0.27, 0.27, 0.27), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')

#Desk
r.lookAt(V3(1.5, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.active_texture = None
r.current_model = 'desk'
r.load('./models/desk2.obj', translate=(-2, -0.08, 0), scale=(1, 1, 1), rotate=(0, 0, 0))
r.draw_arrays('FLAT')

#Computer
r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.current_model = 'computer'
r.load('./models/computer2.obj', translate=(-0.4, 0.27, 0), scale=(0.04, 0.04, 0.04), rotate=(0, 90, 0))
r.draw_arrays('FLAT')

#Trophy
r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.current_model = 'trophy'
r.load('./models/trophy1.obj', translate=(0.75, 0.57, 0), scale=(0.7, 0.7, 0.7), rotate=(0, 0, 0))
r.draw_arrays('FLAT')

#Shelf
r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.current_model = 'shelf'
r.load('./models/shelf.obj', translate=(0.6, 0.5, 0), scale=(0.7, 0.7, 0.7), rotate=(0, 0, 0))
r.draw_arrays('FLAT')

#Books
r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.current_model = 'books'
r.load('./models/books.obj', translate=(0.47, 0.69, 0), scale=(0.4, 0.4, 0.4), rotate=(0, 0, 0))
r.draw_arrays('FLAT')

#Finish
r.display('out.bmp')