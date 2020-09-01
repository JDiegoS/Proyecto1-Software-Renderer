from gl import *

r = Render(800, 800)
r.light = V3(0, 0, 1)


r.lookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))

#baskett = Texture('./models/Basketball.bmp')
#r.active_texture = baskett
r.load('./models/sphere.obj', translate=(0.08, -0.77, 0), scale=(0.27, 0.27, 0.27), rotate=(0, 0, 0))
r.draw_arrays('FLAT')


r.current_model = 'desk'
r.load('./models/desk.obj', translate=(-0.65, -0.3, 0), scale=(0.003, 0.003, 0.003), rotate=(0, 0, 0))
r.draw_arrays('FLAT')

r.current_model = 'computer'
r.load('./models/computer2.obj', translate=(-0.4, 0.19, 0), scale=(0.04, 0.04, 0.04), rotate=(0, 90, 0))
r.draw_arrays('FLAT')

'''r.current_model = 'computer'
r.load('./models/Stand.obj', translate=(0.62, 0.62, 0), scale=(0.085, 0.085, 0.085), rotate=(0, 0, 0))
r.draw_arrays('FLAT')'''

r.current_model = 'computer'
r.load('./models/shelf.obj', translate=(0.6, 0.5, 0), scale=(0.7, 0.7, 0.7), rotate=(0, 0, 0))
r.draw_arrays('FLAT')

r.display('out.bmp')