from manim import *

class coord(Scene):
    def construct(self):
        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length = 6, y_length = 6).add_coordinates()
        #axes.to_edge(LEFT, buff=2)
        square = Square().set_fill(RED, opacity = 0.5)
        square.set_width(1)
        circle = Circle(stroke_width = 6, stroke_color = PINK, fill_color = BLUE_B, fill_opacity = 0.8)
        
        self.play(Write(axes))
        self.play(Write(square))
        self.play(square.animate.shift(RIGHT*2), run_time = 2)
        self.play(square.animate.shift(UP*3), run_time = 2)
        self.play(square.animate.shift(LEFT*2 + DOWN*3))
        self.play(Transform(square, circle))
        self.wait(1)
