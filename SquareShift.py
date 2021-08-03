from manim import *

class SquareShift(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)
        
        self.play(ApplyMethod(square.set_fill, WHITE))
        self.wait(1)
        
        self.play(ApplyMethod(square.shift, UP), run_time=3)
        self.wait(1)
