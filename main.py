from gl import *

r = Render(800, 800)
#t = Texture('./model.bmp')
r.light = V3(0, 0, 1)

#r.active_texture = t
r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('./model.obj', translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')
r.display('out.bmp')