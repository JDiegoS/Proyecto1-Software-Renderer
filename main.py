from gl import *

r = Render(800, 800)
r.light = V3(0, 0, 1)

r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
t = Texture('./models/house.bmp')
r.active_texture = t
r.framebuffer = t.framebuffer

r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
t = Texture('./models/ball2.bmp')
r.active_texture = t
r.load('./models/sphere.obj', translate=(0.08, -0.74, 0), scale=(0.27, 0.27, 0.27), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')

r.lookAt(V3(0.15, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.active_texture = None
r.current_model = 'desk'
r.load('./models/desk.obj', translate=(-0.65, -0.27, 0), scale=(0.003, 0.003, 0.003), rotate=(0, 0, 0))
r.draw_arrays('FLAT')

r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.current_model = 'computer'
r.load('./models/computer2.obj', translate=(-0.4, 0.22, 0), scale=(0.04, 0.04, 0.04), rotate=(0, 90, 0))
r.draw_arrays('FLAT')

r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.current_model = 'trophy'
r.load('./models/trophy1.obj', translate=(0.75, 0.57, 0), scale=(0.7, 0.7, 0.7), rotate=(0, 0, 0))
r.draw_arrays('FLAT')

r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.current_model = 'shelf'
r.load('./models/shelf.obj', translate=(0.6, 0.5, 0), scale=(0.7, 0.7, 0.7), rotate=(0, 0, 0))
r.draw_arrays('FLAT')

r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.current_model = 'books'
r.load('./models/books.obj', translate=(0.47, 0.68, 0), scale=(0.4, 0.4, 0.4), rotate=(0, 0, 0))
r.draw_arrays('FLAT')


r.display('out.bmp')