from manim import *

class updater(Scene):
    def construct(self):
        rectangle = RoundedRectangle(stroke_width = 8, stroke_color = WHITE, fill_color = BLUE_B, width = 4.5, height = 2)
        mathtext = MathTex("\\frac{3}{4} = 0.75").set_color_by_gradient(GREEN, PINK).set_height(1.5)
        mathtext.move_to(rectangle.get_center())
        mathtext.add_updater(lambda x : x.move_to(rectangle.get_center()))
        
        self.play(FadeIn(rectangle))
        self.play(Write(mathtext))
        self.play(rectangle.animate.shift(RIGHT * 2), run_time=3)
        self.wait(1)
        mathtext.clear_updaters()
        self.play(rectangle.animate.shift(LEFT*2))
