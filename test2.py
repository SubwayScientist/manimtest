from manim import *

class UpdateValueTracker1(Scene):
    def construct(self):
        theta = ValueTracker(PI/2)
        line_1= Line(ORIGIN,RIGHT*3,color=RED)
        line_2= Line(ORIGIN,RIGHT*3,color=GREEN)

        line_2.rotate(theta.get_value(),about_point=ORIGIN)

        line_2.add_updater(
                lambda m: m.set_angle(
                                    theta.get_value()
                                )
            )

        self.add(line_1,line_2)

        self.play(theta.animate.increment_value(PI/2))

        self.wait()


class UpdateValueTracker2(Scene):
    CONFIG={
        "line_1_color":ORANGE,
        "line_2_color":PINK,
        "lines_size":3.5,
        "theta":PI/2,
        "increment_theta":PI/2,
        "final_theta":PI,
        "radius":0.7,
        "radius_color":YELLOW,
    }
    def construct(self):
        # Set objets
        theta = ValueTracker(self.theta)
        line_1= Line(ORIGIN,RIGHT*self.lines_size,color=self.line_1_color)
        line_2= Line(ORIGIN,RIGHT*self.lines_size,color=self.line_2_color)

        line_2.rotate(theta.get_value(),about_point=ORIGIN)
        line_2.add_updater(
                lambda m: m.set_angle(
                                    theta.get_value()
                                )
            )

        angle= Arc(
                    radius=self.radius,
                    start_angle=line_1.get_angle(),
                    angle =line_2.get_angle(),
                    color=self.radius_color
            )

        # Show the objects

        self.play(*[
                ShowCreation(obj)for obj in [line_1,line_2,angle]
            ])

        # Set update function to angle

        angle.add_updater(
                    lambda m: m.become(
                            Arc(
                                radius=self.radius,
                                start_angle=line_1.get_angle(),
                                angle =line_2.get_angle(),
                                color=self.radius_color
                            )
                        )
            )
        # Remember to add the objects again to the screen 
        # when you add the add_updater method.
        self.add(angle)

        self.play(theta.animate.increment_value(self.increment_theta()))
        # self.play(theta.set_value,self.final_theta)

        self.wait()
        
import math
        
class DrawArc(Scene):
    def construct(self):
        angle = math.radians(180)
        arc =  Arc(radius=2,angle=angle)
        self.play(Create(arc))
