from manim import *

class barycenter(Scene):
    def construct(self):
        e = ValueTracker(0.25)
        x = ValueTracker(1.)
        
        sun = Circle(radius=1, 
            stroke_width = 8, stroke_color = ORANGE, fill_color=YELLOW_E, fill_opacity=1
        ).shift(LEFT)
        planet1 =  Circle(radius=0.25, 
            stroke_width = 5, stroke_color = MAROON_E, 
            fill_color=MAROON, fill_opacity=1
        ).shift(RIGHT*6)
        planet2 =  Circle(radius=0.5, 
            stroke_width = 5, stroke_color = MAROON_E, 
            fill_color=MAROON, fill_opacity=1
        ).shift(RIGHT*6)
        
        
        self.play(LaggedStart(DrawBorderThenFill(sun), DrawBorderThenFill(planet1), lag_ratio = 0.35))
                
        func1 = ParametricFunction(
            lambda t: np.array([
                6*np.cos(t), 3.5* np.sin(t), 0
            ]), t_range = np.array([0,4*PI])
        )
        func2 = ParametricFunction(
            lambda t: np.array([
                -np.cos(t), -np.sin(t), 0
            ]), t_range = np.array([0,4*PI])
        )
        func3 = ParametricFunction(
            lambda t: np.array([
                5*np.cos(t) + 1, 3.5*np.sin(t), 0
            ]), t_range = np.array([0,4*PI])
        )
        circle = Circle(radius = 0.3)    
        cm = always_redraw(lambda :
            Cross(
                circle,
                stroke_color = DARK_GREY, stroke_width = 10
            ).shift(LEFT*x.get_value())
        )
        
        line = Line(start = sun.get_center(), end = planet1.get_center())
        dashed_line = DashedVMobject(line)
        
        self.play(Create(dashed_line), run_time = 2, rate_func = linear)
        self.play(Create(cm))
        self.play(FadeOut(cm), FadeOut(dashed_line))
        
        self.play(MoveAlongPath(planet1, func1), 
            run_time = 10, rate_func = linear
        )
        self.play(FadeIn(cm), FadeIn(dashed_line))
        self.play(Transform(planet1, planet2), x.animate.set_value(0.), run_time = 5)
        self.wait()
        self.play(FadeOut(cm), FadeOut(dashed_line))
        self.remove(planet1, planet2)
        self.play(MoveAlongPath(planet2, func3), MoveAlongPath(sun, func2),
            run_time = 10, rate_func = linear
        )
        self.wait(3)
