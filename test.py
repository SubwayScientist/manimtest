from manim import *

class test(Scene):
    def construct(self):
        axes = NumberPlane(x_range = [0,5,1], y_range = [0,3,1], x_length = 5, y_length = 3).add_coordinates()
        axes.to_edge(UR)
        #axis_labels = axes.get_axis_labels(x_label ='x', y_label = 'f(x)')
        
        graph = axes.get_graph(lambda x : x**0.5, x_range = [0,4], color = YELLOW)
        graphing_stuff = VGroup(axes, graph)
        
        self.play(DrawBorderThenFill(axes))
        self.play(Create(graph))
        self.play(graphing_stuff.animate.shift(DOWN*4))
        self.play(axes.animate.shift(LEFT*3), run_time = 3)
        self.play(graphing_stuff.animate.shift(UP))
        
      
class test2(Scene):
    def func(self, t):
        return np.array((3 - t**2, t, 0))

    def construct(self):
        plane = NumberPlane().add_coordinates()
    
        func = ParametricFunction(self.func, t_range = np.array([0, TAU]), fill_opacity=0).set_color(RED)
        
        self.add(plane)
        self.play(Create(func))
        
class test3(Scene):
    def construct(self):
        f = lambda t: np.array([t**2, t, 0])
        func = ParametricFunction(f, t_min = -3, t_max = 3)

        self.play(Create(func))




       
        

        
        
        
        
        
        
        
        
        
        
        
