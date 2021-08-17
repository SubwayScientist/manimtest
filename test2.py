from manim import *

class test2(Scene):
    def construct(self):
        e = ValueTracker(0.01)
        
        spring = always_redraw(lambda :
            ParametricFunction(
                lambda t: np.array([
                    0.1*np.sin(10*t),
                    0.5*t*np.sin(e.get_value()) - t,
                    0
                ]), t_range = np.array([0.01, 1.5])                
            ).set_color(GREY).shift(LEFT*3 + UP*3)
        )
        
        
        self.add(spring)
        self.play(e.animate.set_value(15), run_time = 15, rate_func = linear)
