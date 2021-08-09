from manim import *


class capture(Scene):

    def func1(self, t):
        return np.array((3 - t**4, -1.5*t, 0))
        
    def func2(self, t):
        return np.array((4 - t**4, -2*t, 0))
        
    def func3(self, t):
        return np.array((2 - t**4, -1*t, 0))
        
    def construct(self):
    
        e = ValueTracker(4.6)
        
        plane = NumberPlane(x_range = [-10,10,1], y_range = [-10,10,1], x_length = 20, y_length = 20)
        
        Earth = Circle(radius = 1, stroke_width = 5, stroke_color = GREEN_E, fill_color = BLUE_E, fill_opacity = 1).shift(RIGHT * 2)
        radius_R = Line(start = Earth.get_center(), end = Earth.get_top(), color = WHITE)
        R = Tex("$R$").next_to(radius_R.get_center(), LEFT, buff = 0.2).scale(1)
        planet = VGroup(Earth, radius_R, R)
        
        zone = always_redraw(lambda : Ellipse(width=e.get_value()*0.3, height=e.get_value(), stroke_width = 5, stroke_color = BLUE_E, fill_color = BLUE_C, fill_opacity = 0.5).shift(LEFT * 3))
        radius_b = always_redraw(lambda : Line(start = zone.get_center(), end = zone. get_top(), color = WHITE))
        b = always_redraw(lambda : Tex("$b$").next_to(radius_b.get_center(), LEFT, buff = 0.2).scale(1))
        captureZone = VGroup(zone, radius_b, b)
        
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
        
        rectangle = RoundedRectangle(stroke_width = 8, stroke_color = WHITE, width = 6.5, height = 1.8).next_to(planet, DOWN, buff = 0.5)
        equation = Tex(r"$\pi b^2 = 2 \pi \frac{GMR}{v_0^2} + \pi R^2$").scale(1.3)
        equation.add_updater(lambda x : x.move_to(rectangle.get_center()))
        
        dot = Circle(radius = 0.2, fill_color = ORANGE, fill_opacity = 1).shift(LEFT*6 + UP*2.55)
        vector = always_redraw(lambda : Arrow(start = LEFT, end = ((RIGHT*10) / e.get_value())))
        vector.add_updater(lambda y : y.next_to(dot, RIGHT, buff=0))
        v_0 = always_redraw(lambda : Tex(r"$v_0$").next_to(vector.get_center(), UP, buff = 0.2).scale(1))
        v_0.move_to(LEFT*4.45 + UP *2.9)
        particle = VGroup(dot, vector, v_0)
        
        #self.play(Write(plane))
        self.play(Create(planet), run_time = 2.5)
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
        self.add(func1)
        self.play(Create(captureZone), run_time = 2.5)
        self.remove(func1)
        self.play(FadeIn(rectangle))
        self.play(Write(equation), run_time = 2)
        self.play(FadeOut(x1,x2,x3))
        self.play(Create(particle))
        self.play(e.animate.set_value(10), run_time = 6)
        self.play(e.animate.set_value(2), run_time = 6)
        self.wait(3)
