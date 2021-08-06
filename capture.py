from manim import *


class capture(Scene):

    def func1(self, t):
        return np.array((3 - t**4, -1.5*t, 0))
        
    def func2(self, t):
        return np.array((4 - t**4, -2*t, 0))
        
    def func3(self, t):
        return np.array((2 - t**4, -1*t, 0))
        
    def construct(self):
        
        plane = NumberPlane(x_range = [-10,10,1], y_range = [-10,10,1], x_length = 20, y_length = 20)
        Earth = Circle(radius = 1, stroke_width = 5, stroke_color = GREEN_E, fill_color = BLUE_E, fill_opacity = 1).shift(RIGHT * 2)
        zone = Ellipse(width=1.5, height=4.6, stroke_width = 5, stroke_color = BLUE_E, fill_color = BLUE_C, fill_opacity = 0.5).shift(LEFT * 3)
        
        projectile1 = Circle(radius = 0.1, fill_color = ORANGE, fill_opacity = 1)
        func1 = ParametricFunction(self.func1, t_range = np.array([-1.732, 0]), fill_opacity=0).set_color(YELLOW)
        x1 = Star(n=8, outer_radius=0.1, inner_radius = 0.01, color = PURPLE_A).shift(LEFT*6 + UP*2.55)
        
        projectile2 = Circle(radius = 0.12, fill_color = ORANGE, fill_opacity = 1)
        func2 = ParametricFunction(self.func2, t_range = np.array([-1.778, 1.778]), fill_opacity=0).set_color(YELLOW)
        x2 = Star(n=8, outer_radius=0.1, inner_radius = 0.01, color = PURPLE_A).shift(LEFT*6 + UP*3.5)
        
        projectile3 = Circle(radius = 0.15, fill_color = ORANGE, fill_opacity = 1)
        func3 = ParametricFunction(self.func3, t_range = np.array([-1.68, -0.8166]), fill_opacity=0).set_color(YELLOW)
        x3 = Star(n=8, outer_radius=0.1, inner_radius = 0.01, color = PURPLE_A).shift(LEFT*6 + UP*1.6)
        
        star = Star(n=7, outer_radius = 0.3, inner_radius = 0.01, color = YELLOW).shift(RIGHT * 1.555 + UP * 0.8166)
        
        line1 = ArcBetweenPoints(start = [0,0,1], end = [0.05,-0.6,1], angle = -0.2)
        line2 = ArcBetweenPoints(start = [0,0,1], end = [0.5,-0.5,1], angle = -1.2)
        line3 = ArcBetweenPoints(start = [0,0,1], end = [0.7,-0.1,1], angle = -0.7)
        impact = VGroup(line1, line2, line3).set_color_by_gradient(YELLOW, ORANGE).shift(RIGHT*3)
        
        #self.play(Write(plane))
        self.play(DrawBorderThenFill(Earth))
        self.add(x2)
        self.play(MoveAlongPath(projectile2, func2), run_time = 6)
        self.play(FadeOut(projectile2), run_time=0.5)
        self.add(x3)
        self.play(MoveAlongPath(projectile3, func3), run_time = 2)
        self.play(Transform(projectile3, star))
        self.play(FadeOut(projectile3, star))
        self.add(x1)
        self.play(MoveAlongPath(projectile1, func1), run_time = 3)
        self.play(Transform(projectile1, impact))
        self.play(FadeOut(projectile1, impact))
        self.play(Create(zone))
        self.wait(3)
