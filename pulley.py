from manim import *

class pulley(Scene):
    def construct(self):
        e = ValueTracker(PI / 2)
        
        roof1 = Line(start = LEFT*5 + UP*3, end = LEFT + UP*3)
        roof2 = Line(start = LEFT*5 + UP*3, end = LEFT*4.2 + UP*3.3)
        roof3 = Line(start = LEFT*4 + UP*3, end = LEFT*3.2 + UP*3.3)
        roof4 = Line(start = LEFT*3 + UP*3, end = LEFT*2.2 + UP*3.3)
        roof5 = Line(start = LEFT*2 + UP*3, end = LEFT*1.2 + UP*3.3)
        roof = VGroup(roof1,roof2,roof3,roof4,roof5)
        
        floor1 = Line(start = LEFT*5 + DOWN*3, end = LEFT + DOWN*3)
        floor2 = Line(start = LEFT*5 + DOWN*3, end = LEFT*4.2 + DOWN*3.3)
        floor3 = Line(start = LEFT*4 + DOWN*3, end = LEFT*3.2 + DOWN*3.3)
        floor4 = Line(start = LEFT*3 + DOWN*3, end = LEFT*2.2 + DOWN*3.3)
        floor5 = Line(start = LEFT*2 + DOWN*3, end = LEFT*1.2 + DOWN*3.3)
        floor = VGroup(floor1,floor2,floor3,floor4,floor5)
        
        circle = always_redraw(lambda : 
            Circle(
                radius = 0.5, 
                stroke_color = WHITE, stroke_width = 5, 
                fill_color = YELLOW, fill_opacity = 1
                )
                .shift(LEFT*3 + UP + UP*np.sin(e.get_value())
            )        
        )
        mass = always_redraw(lambda : 
            Rectangle(
                width = 0.5, height = 0.3, 
                stroke_color = WHITE, stroke_width = 3, 
                fill_color = BLUE_E, fill_opacity = 1
                )
                .shift(LEFT*3.5 + DOWN*0.5 + 2*UP*np.sin(e.get_value())
            )        
        )
        spring = always_redraw(lambda :
            ParametricFunction(
                lambda t: np.array([
                    0.1*np.sin(20*t),
                    0.66666*t*np.sin(e.get_value()) - t,
                    0
                ]), t_range = np.array([0., 1.5])                
            ).set_color(GREY).shift(LEFT*3 + UP*3)
        )
        string_p = always_redraw(lambda:
            Line(start = LEFT*2.5 + DOWN*3, end = circle.get_right()
            ).set_color(BLUE_B)
        )
        string_m = always_redraw(lambda:
            Line(start = circle.get_left(), end = mass.get_top()
            ).set_color(BLUE_B)
        )
        
        axes = Axes(x_range = [14,40,1], y_range = [-3,3,1],
            x_length = 7, y_length = 6, 
            axis_config = {"include_tip": True, "numbers_to_exclude": [0]}
        ).shift(RIGHT*3.2)
        axis_labels = axes.get_axis_labels(x_label ='t', y_label = 'y(t)')
        graph_p = always_redraw(lambda :
            axes.get_graph(lambda x : np.sin(x) + 1, x_range=[4.499*PI, e.get_value()], color=YELLOW
            )
        )
        graph_m = always_redraw(lambda :
            axes.get_graph(lambda x : 2*np.sin(x) - 0.5, x_range=[4.499*PI, e.get_value()], color=BLUE_E
            )
        )        
        
        plane = NumberPlane()
        #self.play(Write(plane), Write(axes))

        self.play(LaggedStart(Create(roof), Create(floor), lag_ratio=0.35))
        self.play(LaggedStart(Create(spring), DrawBorderThenFill(circle), lag_ratio=0.7))
        self.play(e.animate.set_value(4.5*PI), run_time = 12, rate_func = linear)
        self.play(LaggedStart(Create(string_p), Create(string_m), Create(mass), lag_ratio=0.8))
        self.play(LaggedStart(Write(axes), Write(axis_labels), lag_ratio=0.35))
        self.add(graph_p, graph_m)
        self.play(e.animate.set_value(12.5*PI), run_time = 24, rate_func = linear)

        
        
        
        
