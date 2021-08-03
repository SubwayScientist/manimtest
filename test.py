from manim import *

class test(Scene):
    def construct(self):
        p1= [-1,-1,0]
        p2= [1,-1,0]
        p3= [1,1,0]
        p4= [-1,1,0]
        a = Line(p1,p2).append_points(Line(p2,p3).get_points()).append_points(Line(p3,p4).get_points())
        #print(dir(a))
        
        point_start= a.get_start()
        point_end  = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}").scale(0.5).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}").scale(0.5).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}").scale(0.5).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.get_points()])
        self.add(a)
        self.wait(1)



class test2(Scene):
    def construct(self):
        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length = 6, y_length = 6)
        #axes.to_edge(LEFT, buff=2)
        square = Square().set_fill(RED, opacity = 0.5)
        square.set_width(1)
        circle = Circle(stroke_width = 6, stroke_color = PINK, fill_color = BLUE_B, fill_opacity = 0.8)
        
        self.play(Write(axes))
        self.play(Write(square))
        self.play(square.animate.shift(RIGHT*2), run_time = 2)
        self.play(square.animate.shift(UP*3), run_time = 2)
        self.play(square.animate.shift(LEFT*2 + DOWN*3))
        self.play(Transform(square, circle))
        self.wait(1)
        
class test3(Scene):
    def construct(self):
        rectangle = RoundedRectangle(stroke_width = 8, stroke_color = WHITE, fill_color = BLUE_B, width = 4.5, height = 2)
        mathtext = MathTex("\\frac{3}{4} = 0.75").set_color_by_gradient(GREEN, PINK).set_height(1.5)
        mathtext.move_to(rectangle.get_center())
        mathtext.add_updater(lambda x : x.move_to(rectangle.get_center()))
        
        self.play(FadeIn(rectangle))
        self.play(Write(mathtext))
        self.play(rectangle.animate.shift(RIGHT * 2), run_time=3)
        self.wait(1)
        mathtext.clear_updaters()
        self.play(rectangle.animate.shift(LEFT*2))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
