from manim import *

class test3(Scene):
    def construct(self):
        r = ValueTracker(0.5) #Tracks the value of the radius
        
        triangle = always_redraw(lambda : Triangle(stroke_color = WHITE, stroke_width = 8).set_height(r.get_value() * 2))
        circle = always_redraw(lambda : Circle(radius =r.get_value(), stroke_color = WHITE, stroke_width = 8).align_to(triangle, DOWN)
                            
        self.add(triangle)
        self.add(circle)
        self.wait(1)
