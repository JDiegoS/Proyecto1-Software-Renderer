from gl import *

r = Render(800, 800)
r.light = V3(0, 0, 1)


r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))

#baskett = Texture('./models/Basketball.bmp')
#r.active_texture = baskett
r.load('./models/sphere.obj', translate=(0, -0.55, 0), scale=(0.35, 0.35, 0.35), rotate=(0, 0, 0))
r.draw_arrays('FLAT')


r.current_model = 'desk'
r.load('./models/desk.obj', translate=(-0.6, -0.3, 0), scale=(0.0032, 0.0032, 0.0032), rotate=(0, 0, 0))
r.draw_arrays('FLAT')


r.load('./models/computer2.obj', translate=(-0.3, 0.3, 0), scale=(0.04, 0.045, 0.045), rotate=(0, 80, 0))
r.draw_arrays('FLAT')

r.display('out.bmp')