from manim import *

class rebound(Scene):
    def construct(self):
        e = ValueTracker(1)
        r = ValueTracker(-4)
        plane = NumberPlane()
        
        particle = always_redraw(lambda : Ellipse(width=e.get_value(), height=1, stroke_width = 5, stroke_color = PURPLE, fill_color = PINK, fill_opacity = 1).shift(UP*2 + RIGHT*r.get_value()))
        
        line1 = Line(start = RIGHT*4, end = RIGHT*4 + UP*4)
        line2 = Line(start = RIGHT*4+UP*4, end = RIGHT*4.5 + UP*3)
        line3 = Line(start = RIGHT*4+UP*3, end = RIGHT*4.5 + UP*2)
        line4 = Line(start = RIGHT*4+UP*2, end = RIGHT*4.5 + UP)
        line5 = Line(start = RIGHT*4+UP, end = RIGHT*4.5)
        wall = VGroup(line1, line2, line3, line4, line5)
        
        axes = Axes(x_range = [0,10,1], y_range = [0,3,1], x_length = 10, y_length = 3, axis_config = {"include_tip": True, "numbers_to_exclude": [0]}).add_coordinates()
        axes.to_edge(DOWN)
        #axis_labels = axes.get_axis_labels(x_label ='x', y_label = 'f(x)')
        
        self.play(Write(plane))
        self.play(Create(axes))
        self.play(Create(particle))
        self.play(Create(wall))
        self.play(LaggedStart(r.animate.set_value(3.75), e.animate.set_value(0.5), lag_ratio = 0.35), run_time = 5)
        self.play(LaggedStart(e.animate.set_value(1), r.animate.set_value(-4), lag_ratio = 0.35), run_time = 5)
        #self.play(e.animate.set_value(0.5), r.animate.set_value(3.75))
        self.wait(3)
