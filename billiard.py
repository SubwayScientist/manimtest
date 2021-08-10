from manim import *

class billiard(Scene):
    def construct(self):
        plane = NumberPlane()
        
        circle1 = Circle(radius = 1, fill_color = PURPLE_E, fill_opacity = 1).shift(LEFT*4 + DOWN)
        vector1 = Arrow(start = LEFT, end = RIGHT*2).next_to(circle1.get_center(), RIGHT, buff=0)
        #vector1.add_updater(lambda x : x.next_to(circle1.get_center(), RIGHT, buff=0))
        v0 = Tex(r"$v_0$").next_to(vector1.get_center(), UP, buff = 0.2)
        ball1 = VGroup(circle1, vector1, v0)
        
        ball2 = Circle(radius = 1, fill_color = RED, fill_opacity = 1).shift(RIGHT*3.75)
        
        particle1 = Circle(radius = 3, stroke_color = PURPLE_E, stroke_width = 15).shift(LEFT*3 + DOWN)
        particle2 = Circle(radius = 3, stroke_color = RED, stroke_width = 15).shift(RIGHT*2.75 + UP)
        
        line = Line(start = UP*4 + LEFT*1.5, end = DOWN*4 + RIGHT*1.2, stroke_width = 10)
        tangent = DashedVMobject(line)    #slope = -2.963, inverse = 0.3375
        line2 = Line(start = LEFT*0.2, end = RIGHT*1.8 + UP*0.675, stroke_width = 6)
        line3 = Line(start = LEFT*0.2, end = LEFT*4.2 + DOWN*1.35, stroke_width = 6)
        bissect = DashedVMobject(line3)
        
        vector2 = Arrow(start = LEFT*4, end = LEFT*0.25, buff = 0, max_tip_length_to_length_ratio=0.05)
        
        self.play(Write(plane))
        self.play(LaggedStart(DrawBorderThenFill(ball2), Create(ball1), lag_ratio = 0.5))
        self.play(ball1.animate.shift(RIGHT*6), run_time = 4)
        self.wait(2)
        self.play(LaggedStart(FadeOut(ball1, ball2), FadeIn(particle1, particle2), lag_ratio = 0.2))
        self.wait(1)
        self.play(Write(tangent), run_time = 2)
        self.play(Create(vector2))
        self.play(Create(bissect))
        self.wait(3)
