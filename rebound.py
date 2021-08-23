from manim import *

class rebound(Scene):
    def construct(self):
        e = ValueTracker(1)
        h = ValueTracker(1)
        r = ValueTracker(-4)
        t = ValueTracker(0.)
        n = ValueTracker(0.)
        plane = NumberPlane()
        
        particle = always_redraw(lambda : 
            Ellipse(width=e.get_value(), height=h.get_value(), 
                stroke_width = 5, stroke_color = PURPLE, 
                fill_color = PINK, fill_opacity = 1
            ).shift(UP*2 + RIGHT*r.get_value())
        )

        line1 = Line(start = RIGHT*4,        end = RIGHT*4 + UP*4     )
        line2 = Line(start = RIGHT*4+UP*4,   end = RIGHT*4.25 + UP*3.5)
        line3 = Line(start = RIGHT*4+UP*3.5, end = RIGHT*4.25 + UP*3  )
        line4 = Line(start = RIGHT*4+UP*3,   end = RIGHT*4.25 + UP*2.5)
        line5 = Line(start = RIGHT*4+UP*2.5, end = RIGHT*4.25 + UP*2  )
        line6 = Line(start = RIGHT*4+UP*2,   end = RIGHT*4.25 + UP*1.5)
        line7 = Line(start = RIGHT*4+UP*1.5, end = RIGHT*4.25 + UP    )
        line8 = Line(start = RIGHT*4+UP,     end = RIGHT*4.25 + UP*0.5)
        line9 = Line(start = RIGHT*4+UP*0.5, end = RIGHT*4.25         )
        line10 = Line(start = RIGHT*4, end = RIGHT*7)
        wall = VGroup(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10)
        
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
        
        normal = always_redraw(lambda :
            Arrow(start = particle.get_center(), end = particle.get_center() + LEFT*n.get_value()
            )
        )
        N = Tex(r"$N$")
        N.add_updater(lambda x: x.next_to(normal, UP, buff = 0.2))
        
        momentum = always_redraw(lambda :
            Arrow(start = particle.get_center(), end = particle.get_center() + RIGHT*2
            )
        )
        p1 = Tex(r"$p_1$")
        p1.add_updater(lambda x: x.next_to(momentum, UP, buff = 0.2))
        
        momentum2 = always_redraw(lambda :
            Arrow(start = particle.get_center(), end = particle.get_center() + LEFT*2
            )
        )
        p2 = Tex(r"$p_2$")
        p2.add_updater(lambda x: x.next_to(momentum2, UP, buff = 0.2))
        
        #self.play(Write(plane))
        self.play(LaggedStart(
            Create(axes), Create(particle), Create(wall), Write(axis_labels),
            lag_ratio = 0.5, run_time = 1.5)
        )
        self.play(Create(graph), Create(normal))
        self.play(Create(momentum), Write(p1))
        self.play(r.animate.set_value(3.5), t.animate.set_value(4),
            run_time = 4, rate_func = linear)
        self.add(N)
        self.remove(momentum, p1)
        self.play(r.animate.set_value(3.75), e.animate.set_value(0.5), h.animate.set_value(1.3), 
            t.animate.set_value(5), n.animate.set_value(2.), rate_func = linear)
        self.play(r.animate.set_value(3.5), e.animate.set_value(1), h.animate.set_value(1),
            t.animate.set_value(6), n.animate.set_value(0.), rate_func = linear)
        self.remove(N)
        self.add(momentum2, p2)
        self.play(r.animate.set_value(-4), t.animate.set_value(10),
            run_time = 4, rate_func = linear)
        self.play(FadeOut(momentum2), FadeOut(p2))
        
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
        self.wait(4)
