from manim import *

class test2(Scene):
    def construct(self):
        e = ValueTracker(4.5*PI)
        
        axes = Axes(x_range = [14,40,1], y_range = [-2,2,1],
            x_length = 7, y_length = 4, 
            axis_config = {"include_tip": True, "numbers_to_exclude": [0]}
        ).shift(RIGHT*3.2)
        axis_labels = axes.get_axis_labels(x_label ='t', y_label = 'y(t)')
        graph_p = always_redraw(lambda :
            axes.get_graph(lambda x : np.sin(x), x_range=[4.499*PI, e.get_value()], color=YELLOW
            )
        )
        graph_m = always_redraw(lambda :
            axes.get_graph(lambda x : 2*np.sin(x), x_range=[4.499*PI, e.get_value()], color=BLUE_E
            )
        )
        
        self.play(LaggedStart(Write(axes), Write(axis_labels), lag_ratio=0.35))
        self.add(graph_p, graph_m)
        self.play(e.animate.set_value(12.5*PI), run_time = 8, rate_func = linear)
