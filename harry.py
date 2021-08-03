from manim import *

class harry(Scene):
    def construct(self):
        r = ValueTracker(0.5) #Tracks the value of the radius
        
        triangle = always_redraw(lambda : Triangle(stroke_color = WHITE, stroke_width = 8).set_height(r.get_value() * 3))
        circle = always_redraw(lambda : Circle(radius =r.get_value(), stroke_color = WHITE, stroke_width = 8).shift(DOWN * 0.5))
        triangle.add_updater(lambda x : x.align_to(circle, DOWN))
        line = always_redraw(lambda : Line(start = triangle.get_top(), end = triangle.get_bottom(), stroke_color = WHITE, stroke_width = 8).align_to(circle, DOWN))
        
        self.play(LaggedStart(Create(circle), Create(triangle), Create(line), lag_ratio = 0.5))
        self.wait(1)
        self.play(r.animate.set_value(2), run_time = 5)
