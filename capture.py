from manim import *
from scipy.optimize import fsolve

class capture(Scene):

    def func(self, t):
        return np.array((3 - t**2, -t, 0))
        
    def construct(self):
        #e = ValueTracker(-3)
        
        plane = NumberPlane(x_range = [-10,10,1], y_range = [-10,10,1], x_length = 20, y_length = 20)
        func = ParametricFunction(self.func, t_range = np.array([-3, 3]), fill_opacity=0).set_color(YELLOW)
        #dot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity = 0.8).scale(0.8).move_to(func.get_end()))
        
        Earth = Circle(radius = 1, stroke_width = 5, stroke_color = GREEN_E, fill_color = BLUE_E, fill_opacity = 1).shift(RIGHT * 2)
        
        #graph = always_redraw(lambda : plane.get_graph(lambda x : (9-3*x)**0.5, x_range=[-7, 7], color = YELLOW))
        projectile1 = Circle(radius = 0.2)
        
        self.play(Write(plane))
        self.play(DrawBorderThenFill(Earth))
        self.add(projectile1, func)
        self.play(MoveAlongPath(projectile1, func), run_time = 6)
        #self.play(e.animate.set_value(3), run_time = 6, rate_func = linear)
        self.wait(3)
        
    
