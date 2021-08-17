from manim import *

class pulley(Scene):

    def spring(self, t):
        return np.array((0.1*np.sin(10*t), -t, 0))

    def construct(self):
        e = ValueTracker(0.)
        
        circle = always_redraw(lambda : 
            Circle(
                radius = 0.5, 
                stroke_color = WHITE, stroke_width = 5, 
                fill_color = YELLOW, fill_opacity = 1
                )
                .shift(LEFT*3 + UP + UP*np.sin(e.get_value())
            )        
        )
        spring = always_redraw(lambda :
            ParametricFunction(
                lambda t: np.array([
                    0.1*np.sin(10*t),
                    0.66666*t*np.sin(e.get_value()) - t,
                    0
                ]), t_range = np.array([0., 1.5])                
            ).set_color(GREY).shift(LEFT*3 + UP*3)
        )
        
        
        self.play(Create(circle))
        self.add(spring)
        self.play(e.animate.set_value(15), run_time = 15, rate_func = linear)

        
        
        
        
