from manim import *
import numpy as np

class file1(MovingCameraScene) : 
    
    def get_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: np.sin((x+dx)),
            x_range = [4 , 0 , 4]
        )

    def construct(self) : 
        pixel_height = config["pixel_height"]  
        pixel_width = config["pixel_width"]
        
        
        sine_function=self.get_sine_wave().scale(0.25)
        d_theta=ValueTracker(0)
        def update_wave(func):
            func.become(
                self.get_sine_wave(dx=d_theta.get_value())
            )
            return func
        sine_function.add_updater(update_wave)
        
        text = Text("WHAT IS QUANTUM TUNNELING?" , font = "Adobe Arabic" , font_size = 20)
        
        text1 = Text("LET THIS BE A PARTICLE" , font = "Adobe Arabic" , font_size = 20).shift(2.6*UP)
        
        text2 = Text("AND THIS A WALL" , font = "Adobe Arabic" , font_size = 20).shift(2.6*UP + 2*RIGHT)
        
        text3 = Text("NOW IF WE MAKE THE BALL HIT THE WALL, THIS SHOULD HAPPEN" , font = "Adobe Arabic" , font_size = 20).shift(3*UP)
        
        text4 = Text("BUT DURING QUANTUM TUNNELING, THIS IS WHAT HAPPENS" , font = "Adobe Arabic" , font_size = 20).shift(3*UP)
        
        dot = Dot(radius = 0.05)
        dot.set_color(ORANGE)
        dot.shift(1*DOWN)
        
        line = Line(6*LEFT + 3.5*DOWN, 6*RIGHT + 3.5*DOWN , stroke_width = 1)
        
        rect = Rectangle(width = 0.3 , height = 4).next_to(line , UP , buff = 0.02)
        rect.set_color(RED)
        rect.set_fill(RED , opacity = 1)
        
        gr1 = VGroup(line , rect)
        
         
        self.play(Write(text))
        self.play(text.animate.shift(3*UP))
        self.play(Write(dot))
        self.play(Write(line))
        #self.play(dot.animate.shift(4.45*DOWN) , run_time = 1)
        #self.play(dot.animate.shift(2*UP) , run_time = 1.25)
        #self.play(dot.animate.shift(1*UP) , run_time = 1.40)
        #self.play(dot.animate.shift(2*DOWN) , run_time = 1)
        #self.play(dot.animate.shift(.7*UP) , run_time = 1.2)
        self.wait(0.7)
        self.play(Write(text1) , run_time = 0.5)
        self.play(dot.animate.shift(2*LEFT + 1*UP) , text1.animate.shift(2*LEFT))
        self.play(Write(rect) , Write(text2))
        self.play(FadeOut(text , text1 , text2) , run_time = 0.4)
        self.play(gr1.animate.shift(1*UP))
        self.wait(0.5)
        self.play(Write(text3) , run_time = 1)
        self.wait(0.5)
        self.play(dot.animate.shift(1.775*RIGHT))     
        self.play(dot.animate.shift(2*LEFT))
        self.wait(0.25)
        self.play(FadeOut(text3) , run_time = 0.5)
        self.wait(0.25)
        self.play(Write(text4))
        self.wait(0.25)
        self.play(rect.animate.set_fill(ORANGE , opacity = 0.4) ,self.camera.frame.animate.set(width = 4).move_to(rect) , dot.animate.shift(0.4*DOWN))
        self.play(dot.animate.shift(5*RIGHT) , run_time = 4)
        self.play(dot.animate.shift(5*LEFT) , run_time = 4)
        self.wait(0.5)
        self.play(self.camera.frame.animate.set(width = 15) , run_time = 2)
        #self.play(Create(sine_function))
        #self.play(d_theta.increment_value,2*PI,rate_func=linear)
        self.wait(10)