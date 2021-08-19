from manim import *

class rebound(Scene):
    def construct(self):
        e = ValueTracker(1)
        r = ValueTracker(-4)
        t = ValueTracker(0.)
        plane = NumberPlane()
        
        particle = always_redraw(lambda : 
            Ellipse(width=e.get_value(), height=1, 
                stroke_width = 5, stroke_color = PURPLE, 
                fill_color = PINK, fill_opacity = 1
            ).shift(UP*2 + RIGHT*r.get_value())
        )
        
        line1 = Line(start = RIGHT*4, end = RIGHT*4 + UP*4)
        line2 = Line(start = RIGHT*4+UP*4, end = RIGHT*4.5 + UP*3)
        line3 = Line(start = RIGHT*4+UP*3, end = RIGHT*4.5 + UP*2)
        line4 = Line(start = RIGHT*4+UP*2, end = RIGHT*4.5 + UP)
        line5 = Line(start = RIGHT*4+UP, end = RIGHT*4.5)
        line6 = Line(start = RIGHT*4, end = RIGHT*7)
        wall = VGroup(line1, line2, line3, line4, line5, line6)
        
        axes = Axes(x_range = [0,10,1], y_range = [0,3,1], 
            x_length = 10, y_length = 3, 
            axis_config = {"include_tip": True, "numbers_to_exclude": [0]}
        )
        axes.to_edge(DOWN)
        axis_labels = axes.get_axis_labels(x_label ='t', y_label = 'N(t)')
        graph = always_redraw(lambda :
            axes.get_graph(lambda x : 2*np.exp(-4*(x-5)**2), x_range=[0, t.get_value()], color=YELLOW
            )
        )
        
        #self.play(Write(plane))
        self.play(LaggedStart(
            Create(axes), Create(particle), Create(wall), Write(axis_labels),
            lag_ratio = 0.5, run_time = 1.5)
        )
        self.play(Create(graph))
        self.play(r.animate.set_value(3.5), t.animate.set_value(4),
            run_time = 4, rate_func = linear)
        self.play(r.animate.set_value(3.75), e.animate.set_value(0.5), 
            t.animate.set_value(5), rate_func = linear)
        self.play(r.animate.set_value(3.5), e.animate.set_value(1), 
            t.animate.set_value(6), rate_func = linear)
        self.play(r.animate.set_value(-4), t.animate.set_value(10),
            run_time = 4, rate_func = linear)
        
        self.wait()
        
        dx_list = [0.25, 0.1, 0.01]
        area = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=graph,
                    x_range = [0, 10],
                    stroke_width=0.1,
                    stroke_color=WHITE,
                    dx=dx
                )#.set_color_by_gradient(BLUE, PURPLE)
                for dx in dx_list
            ]
        )
        first_area = area[0]
        self.play(Create(first_area), run_time = 2)
        for k in range(1, len(dx_list)):
            new_area = area[k]
            self.play(Transform(first_area, new_area), run_time = 2)
            self.wait(0.5)

        self.wait()
        
        equation = Tex(r"$\Delta p = \int_{t_1}^{t_2} N(t)dt$"
        ).shift(DOWN*1.8 + RIGHT*3).set_color(TEAL_A)
        
        self.play(Write(equation), run_time = 1.5)
        self.wait(3)
