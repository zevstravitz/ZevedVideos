#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

class RecursionOpeningQuote(OpeningQuote):
    CONFIG = {
        "quote" : [
            "`Begin at the beginning,' the King said, very gravely, \\\\ `and go on till you come to the end: then stop.'"
        ],
        "highlighted_quote_terms": {
          "seen" : BLUE,
          "believed": PURPLE
        },
        "fade_in_kwargs": {
            "lag_ratio": 0.5,
            "rate_func": linear,
            "run_time": 3,
        },
        "author" : "Lewis Carroll, Alice In Wonderland"
    }

class Recursion(Scene):
  def construct(self):
    recursion = TextMobject("\\texttt{Recursion}")
    recursion.scale(3)
    self.play(Write(recursion))
    self.wait(4)


class ToUnderstand(OpeningQuote):
    CONFIG = {
        "quote" : [
            "To understand ", "recursion,", "you \\\\ must first understand ", "recursion.",
        ],
        "highlighted_quote_terms": {
          "recursion" : BLUE
        },
        "fade_in_kwargs": {
            "lag_ratio": 0.5,
            "rate_func": linear,
            "run_time": 3,
        },
        "author" : "Unknown"
    }

class FactorialExamples(Scene):
  def construct(self):
    fact_5 = TexMobject("5! = 5\\cdot4\\cdot3\\cdot2\\cdot1")
    fact_4 = TexMobject("4! = 4\\cdot3\\cdot2\\cdot1")
    fact_3 = TexMobject("3! = 3\\cdot2\\cdot1")
    fact_2 = TexMobject("2! = 2\\cdot1")
    fact_1 = TexMobject("1! = 1")

    fact_5.move_to(UP*2)
    fact_4.move_to(UP*1)
    # fact_3
    fact_2.move_to(DOWN*1)
    fact_1.move_to(DOWN*2)

    self.play(FadeInFrom(fact_5, RIGHT),
              FadeInFrom(fact_4, LEFT),
              FadeInFrom(fact_3, RIGHT),
              FadeInFrom(fact_2, LEFT),
              FadeInFrom(fact_1, RIGHT))
    self.wait(8)

class FactorialDef(Scene):
  def construct(self):
    def1_A = TexMobject("1")
    def1_B = TextMobject("if \\, n=0")

    def1_A.shift(UP)
    def1_B.shift(UP)

    def2_A = TexMobject("n\\cdot (n-1)\\cdot (n-2)... 3,2,1")
    def2_B = TexMobject("if \\, n\\geq 1")

    def1_B.next_to(def1_A, RIGHT).shift(RIGHT*0.5)
    def2_B.next_to(def2_A, RIGHT).shift(RIGHT*0.5)

    def1_A.align_to(def2_A,LEFT)
    def1_B.align_to(def2_B,LEFT)

    def_group=VGroup(def1_A,def2_A, def1_B, def2_B)
    braces=Brace(def_group, LEFT)
    eq_text = braces.get_text("n! = ")

    total_wrap = VGroup(def1_A,def2_A, def1_B, def2_B, braces, eq_text)

    self.play(GrowFromCenter(braces),
              Write(eq_text))
    self.wait(1)
    self.play(FadeIn(def_group))
    self.wait(4)

    self.play(total_wrap.move_to, UP*2.5,
              run_time = 3)
          
    fact_5 = TexMobject("5! = 5\\cdot")
    fact_4_in_5 = TexMobject("4\\cdot3\\cdot2\\cdot1").next_to(fact_5, RIGHT)
    fact_4_in_5.set_color(BLUE)
    fact_5_group = VGroup(fact_5, fact_4_in_5).move_to(ORIGIN)
    self.play(Write(fact_5_group))

    self.wait(7)
    fact_4_brace = Brace(fact_4_in_5, DOWN)
    fact_4_brace_text = fact_4_brace.get_text("4!").set_color(BLUE)
    self.play(GrowFromCenter(fact_4_brace),
              FadeInFromDown(fact_4_brace_text))
    self.wait(5)

    fact_5_wrap_group = VGroup(fact_5_group, fact_4_brace, fact_4_brace_text)
      
    fact_4 = TexMobject("4! = 4\\cdot")
    fact_3_in_4 = TexMobject("3\\cdot2\\cdot1").next_to(fact_4, RIGHT)
    fact_3_in_4.set_color(BLUE)
    fact_4_group = VGroup(fact_4, fact_3_in_4).move_to(DOWN)

    fact_3_brace = Brace(fact_3_in_4, DOWN)
    fact_3_brace_text = fact_3_brace.get_text("3!").set_color(BLUE)

    fact_4_wrap_group = VGroup(fact_4_group, fact_3_brace, fact_3_brace_text)

    self.play(fact_5_wrap_group.shift, UP)
    self.wait()
    self.play(Write(fact_4_group),
              GrowFromCenter(fact_3_brace),
              FadeInFromDown(fact_3_brace_text))
    self.wait(4)

    self.play(FadeOutAndShiftDown(fact_5_wrap_group),
              FadeOutAndShiftDown(fact_4_wrap_group))

    self.play(total_wrap.move_to, ORIGIN,
              run_time = 3)

    self.wait(6)

    def2_A_v2 = TexMobject("n\\cdot (n-1)!").move_to(def2_A.get_center())  
    def2_A_v2.align_to(def1_A,LEFT)

    self.play(ReplacementTransform(def2_A, def2_A_v2),
              run_time = 1)

    self.wait(7)

class GuessingGameBinary(Scene):
    def construct(self):
        LOC = LEFT*6
        points = []
        for i in range(50):
            curr = Dot(LOC)
            curr.set_color(RED)
            curr.scale(0.7)
            
            points.append(curr)
            LOC += RIGHT*0.25
            if i==40: points[40].set_color(BLUE)
        
        points_group = VGroup(*points)
        points_group.move_to(ORIGIN)
        self.play(FadeInFromDown(points_group),
                  run_time = 5)
        
        self.wait(3)

        ## Random guessing
        lin_guesses = [points[25], points[37], points[43], points[40]]
        arrows = [Arrow(start=LEFT, end=RIGHT).move_to(lin_guesses[0].get_center() + UP),
                  Arrow(start=LEFT, end=RIGHT).move_to(lin_guesses[1].get_center() + UP),
                  Arrow(start=RIGHT, end=LEFT).move_to(lin_guesses[2].get_center() + UP)]
        
        not_viable = [VGroup(*points[0:26]), VGroup(*points[24:38]), VGroup(*points[43:50])]

        for arrow in arrows: arrow.scale(0.7) 
        
        for i in range(len(lin_guesses)):
            if i == len(lin_guesses)-1:
                self.play(lin_guesses[i].scale, 4,
                          lin_guesses[i].set_color, GREEN,
                          run_time = 1.5,
                          rate_func = there_and_back_with_pause)
                self.play(FadeOutAndShiftDown(VGroup(*[points[38], points[39], points[41], points[42]])),
                          run_time = 1)
            else:
                self.play(lin_guesses[i].scale, 3,
                          lin_guesses[i].set_color, WHITE,
                          run_time = 1.5,
                          rate_func = there_and_back)
                self.play(ShowCreation(arrows[i]),
                          run_time = 0.5,
                          rate_func=there_and_back)
                self.play(FadeOutAndShiftDown(not_viable[i]),
                          run_time = 1)
        self.wait(4)

class FactorialTree(Scene):
  def construct(self):
    # ARROW TEMPLATES
    left_arrow = Arrow(UP*0.5, LEFT)
    right_arrow = Arrow(UP*0.5, RIGHT)

    fact_5_top = TexMobject("5!").move_to(UP*3).set_color(BLUE)

    arrow_5_left = left_arrow.copy().shift(UP*2.25)
    arrow_5_right = right_arrow.copy().shift(UP*2.25)

    fact_5_left = TexMobject("5").move_to(UP*2+LEFT).set_color(GREEN)
    fact_5_right = TexMobject("4!").move_to(UP*2+RIGHT).set_color(BLUE)
    fact_5_mult = TexMobject("\\cdot").move_to(UP*2).scale(2)

    self.play(Write(fact_5_top),
              Write(fact_5_left),
              Write(fact_5_right),
              Write(fact_5_mult))

    self.play(GrowArrow(arrow_5_left),
              GrowArrow(arrow_5_right))

    fact_4_left = TexMobject("4").move_to(fact_5_right.get_center() + DOWN*1 + LEFT).set_color(GREEN)
    fact_4_right = TexMobject("3!").move_to(fact_5_right.get_center() + DOWN*1 + RIGHT).set_color(BLUE)
    fact_4_mult = TexMobject("\\cdot").move_to(fact_5_right.get_center() + DOWN*1).scale(2)
    arrow_4_left = left_arrow.copy().shift(RIGHT+UP*1.25)
    arrow_4_right = right_arrow.copy().shift(RIGHT+UP*1.25)
    
    self.play(Write(fact_4_left),
              Write(fact_4_right),
              Write(fact_4_mult))
    self.play(GrowArrow(arrow_4_left),
              GrowArrow(arrow_4_right))

    fact_3_left = TexMobject("3").move_to(fact_4_right.get_center() + DOWN*1 + LEFT).set_color(GREEN)
    fact_3_right = TexMobject("2!").move_to(fact_4_right.get_center() + DOWN*1 + RIGHT).set_color(BLUE)
    fact_3_mult = TexMobject("\\cdot").move_to(fact_4_right.get_center() + DOWN*1).scale(2)
    arrow_3_left = left_arrow.copy().shift(RIGHT*2 + UP*.25)
    arrow_3_right = right_arrow.copy().shift(RIGHT*2 + UP*.25)

    self.play(Write(fact_3_left),
              Write(fact_3_right),
              Write(fact_3_mult))
    self.play(GrowArrow(arrow_3_left),
              GrowArrow(arrow_3_right))

    fact_2_left = TexMobject("2").move_to(fact_3_right.get_center() + DOWN*1 + LEFT).set_color(GREEN)
    fact_2_right = TexMobject("1!").move_to(fact_3_right.get_center() + DOWN*1 + RIGHT).set_color(BLUE)
    fact_2_mult = TexMobject("\\cdot").move_to(fact_3_right.get_center() + DOWN*1).scale(2)
    arrow_2_left = left_arrow.copy().shift(RIGHT*3 + DOWN*.75)
    arrow_2_right = right_arrow.copy().shift(RIGHT*3 + DOWN*.75)

    self.play(Write(fact_2_left),
              Write(fact_2_right),
              Write(fact_2_mult))
    self.play(GrowArrow(arrow_2_left),
              GrowArrow(arrow_2_right))

    fact_1_left = TexMobject("1").move_to(fact_2_right.get_center() + DOWN*1 + LEFT).set_color(GREEN)
    fact_1_right = TexMobject("0!").move_to(fact_2_right.get_center() + DOWN*1 + RIGHT).set_color(BLUE)
    fact_1_mult = TexMobject("\\cdot").move_to(fact_2_right.get_center() + DOWN*1).scale(2)
    arrow_1_left = left_arrow.copy().shift(RIGHT*4 + DOWN*1.75)
    arrow_1_right = right_arrow.copy().shift(RIGHT*4 + DOWN*1.75)

    self.play(Write(fact_1_left),
              Write(fact_1_right),
              Write(fact_1_mult))
    self.play(GrowArrow(arrow_1_left),
              GrowArrow(arrow_1_right))

    fact_0_left = TexMobject("1").move_to(fact_1_right.get_center() + DOWN*1 + LEFT).set_color(GREEN)
    arrow_0_left = left_arrow.copy().shift(RIGHT*5 + DOWN*2.75)
    self.play(Write(fact_0_left))
    self.play(GrowArrow(arrow_0_left))


    self.wait(7)

    # zero fact transform
    fact_zero_group = VGroup(fact_1_right, fact_0_left, arrow_0_left)
    fact_zero_final = TexMobject("1").move_to(fact_2_right.get_center() + DOWN*1 + RIGHT).set_color(RED)
    self.play(ReplacementTransform(fact_zero_group, fact_zero_final))
    self.wait()
    ## Fact one transform
    fact_one_group = VGroup(fact_1_left, fact_2_right, arrow_1_left, arrow_1_right, fact_1_mult, fact_zero_final)
    fact_one_final = TexMobject("1").move_to(fact_3_right.get_center() + DOWN*1 + RIGHT).set_color(RED)
    self.play(ReplacementTransform(fact_one_group, fact_one_final))
    self.wait()
    ## Fact two transform
    fact_two_group = VGroup(fact_2_left, fact_3_right, arrow_2_left, arrow_2_right, fact_2_mult, fact_one_final)
    fact_two_final = TexMobject("2").move_to(fact_4_right.get_center() + DOWN*1 + RIGHT).set_color(RED)
    self.play(ReplacementTransform(fact_two_group, fact_two_final))
    self.wait()
    ## Fact three transform
    fact_three_group = VGroup(fact_3_left, fact_4_right, arrow_3_left, arrow_3_right, fact_3_mult, fact_two_final)
    fact_three_final = TexMobject("6").move_to(fact_5_right.get_center() + DOWN*1 + RIGHT).set_color(RED)
    self.play(ReplacementTransform(fact_three_group, fact_three_final))
    self.wait()
    ## Fact four transform
    fact_four_group = VGroup(fact_4_left, fact_5_right, arrow_4_left, arrow_4_right, fact_4_mult, fact_three_final)
    fact_four_final = TexMobject("24").move_to(UP*2+RIGHT).set_color(RED)
    self.play(ReplacementTransform(fact_four_group, fact_four_final))
    self.wait()
    ## Fact five transform
    fact_five_group = VGroup(fact_5_left, fact_5_top, arrow_5_left, arrow_5_right, fact_5_mult, fact_four_final)
    fact_five_final = TexMobject("120").move_to(UP*3).set_color(RED)
    self.play(ReplacementTransform(fact_five_group, fact_five_final))
    self.play(fact_five_final.scale, 2,
              rate_func = there_and_back)
    self.wait(7)

class ZevedClosing(ThreeDScene):
    def construct(self):
        arc1 = AnnularSector(start_angle=TAU/8)
        arc1.set_color(BLUE)
        arc2 = AnnularSector(start_angle=5*PI/4)
        arc2.set_colors_by_radial_gradient(inner_color=PURPLE)
        zeved=TextMobject("Zev", "ed")
        zeved.set_color_by_tex_to_color_map({
            "Zev": BLUE,
            "ed": PURPLE
        })

        zeved_wrapper = VGroup(arc1, arc2, zeved)
        zeved_wrapper.scale(1.75)

        self.play(FadeInFrom(arc1, TOP), FadeInFrom(arc2, BOTTOM))
        self.play(Write(zeved), run_time=3.0)
        
        self.wait(12)
        self.set_camera_orientation(phi=0,gamma=0)
        self.move_camera(phi=PI/2)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()


NEW_ROW_SHIFT = 0.5
ROW_VERT = 0.5*DOWN
class MergeSort(Scene):
  def construct(self):
    # 5, 4, 6, 1, 2, 7, 3
    WIDTH = 0.25
    HEIGHT_FACTOR = 0.25

    merge_sort = TextMobject("Merge Sort").move_to(UP*3.5 + LEFT*5.7).scale(0.8)
    self.play(ShowCreation(merge_sort), run_time = 0.5)

    five = Rectangle(height = 5*HEIGHT_FACTOR, width = WIDTH).move_to(LEFT*1.5)
    four = Rectangle(height = 4*HEIGHT_FACTOR, width = WIDTH).move_to(LEFT*1)
    six = Rectangle(height = 6*HEIGHT_FACTOR, width = WIDTH).move_to(LEFT*0.5)
    one = Rectangle(height = 1*HEIGHT_FACTOR, width = WIDTH)
    two = Rectangle(height = 2*HEIGHT_FACTOR, width = WIDTH).move_to(RIGHT*0.5)
    seven = Rectangle(height = 7*HEIGHT_FACTOR, width = WIDTH).move_to(RIGHT*1)
    three = Rectangle(height = 3*HEIGHT_FACTOR, width = WIDTH).move_to(RIGHT*1.5)

    rectangles = [five, four, six, one, two, seven, three]
    rectangles_group = VGroup(*rectangles)
    for rect in rectangles:
      rect.align_to(four,BOTTOM)
      self.play(FadeInFrom(rect, DOWN),
                run_time = 0.4,
                rate_func = linear)

    self.play(rectangles_group.shift, UP*2)
    self.draw_sec(rectangles)
    self.draw_third(rectangles)
    self.draw_fourth(rectangles)
    self.draw_fifth(rectangles)
    self.draw_sixth(rectangles)
    self.draw_seventh(rectangles)

    self.play(rectangles_group.move_to, ORIGIN)
    self.wait()

  def draw_sec(self, rects):
    ## MOVE TO THIRD ROW
    for i in range(4):
      self.play(rects[i].shift, ROW_VERT + LEFT*1,
      run_time = NEW_ROW_SHIFT)
    for i in range(4, 7):
      self.play(rects[i].shift, ROW_VERT + RIGHT*1,
      run_time = NEW_ROW_SHIFT)

  def draw_third(self, rects):
    ## MOVE TO THIRD ROW

    for i in range(2):
      self.play(rects[i].shift, ROW_VERT + LEFT*2,
      run_time = NEW_ROW_SHIFT)

    for i in range(2,4):
      self.play(rects[i].shift, ROW_VERT + LEFT*0.75,
      run_time = NEW_ROW_SHIFT)

    for i in range(4,6):
      self.play(rects[i].shift, ROW_VERT + RIGHT*0.75, run_time = NEW_ROW_SHIFT)

    self.play(rects[6].shift, ROW_VERT + RIGHT*2, run_time = NEW_ROW_SHIFT)

  def draw_fourth(self, rects):
    ## MOVE TO THIRD ROW
    self.play(rects[0].shift, ROW_VERT + LEFT*2, run_time = NEW_ROW_SHIFT)
    self.play(rects[1].shift, ROW_VERT + LEFT*1, run_time = NEW_ROW_SHIFT)
    self.play(rects[2].shift, ROW_VERT + LEFT*1, run_time = NEW_ROW_SHIFT)
    self.play(rects[3].shift, ROW_VERT, run_time = NEW_ROW_SHIFT)
    self.play(rects[4].shift, ROW_VERT, run_time = NEW_ROW_SHIFT)
    self.play(rects[5].shift, ROW_VERT + RIGHT*1, run_time = NEW_ROW_SHIFT)
    self.play(rects[6].shift, ROW_VERT + RIGHT*1, run_time = NEW_ROW_SHIFT)

  def draw_fifth(self, rects):
    # START MAKING COMPARISONS
    ## 1,2
    self.play(rects[0].set_color, BLUE,
              rects[1].set_color, BLUE,
              run_time = 1,
              rate_func = there_and_back)

    self.play(rects[0].shift, ROW_VERT + RIGHT*2.5,
              rects[1].shift, ROW_VERT + RIGHT*0.5)

    ## 3, 4
    self.play(rects[2].set_color, BLUE,
          rects[3].set_color, BLUE,
          run_time = 1,
          rate_func = there_and_back)

    self.play(rects[2].shift, ROW_VERT + RIGHT*1.5,
              rects[3].shift, ROW_VERT + LEFT*0.5)

    ## 5, 6
    self.play(rects[4].set_color, BLUE,
          rects[5].set_color, BLUE,
          run_time = 1,
          rate_func = there_and_back)

    self.play(rects[4].shift, ROW_VERT,
              rects[5].shift, ROW_VERT + LEFT)
    
    ## 7
    self.play(rects[6].set_color, BLUE,
          run_time = 1,
          rate_func = there_and_back)

    self.play(rects[6].shift, ROW_VERT + LEFT)

  def draw_sixth(self, rects):
    SHIFT_DOWN = DOWN*1.5
    self.play(rects[1].set_color, BLUE,
              rects[3].set_color, BLUE,
              run_time = 1,
              rate_func = there_and_back)
    self.play(rects[3].shift, SHIFT_DOWN)
  
    self.play(rects[1].set_color, BLUE,
              rects[2].set_color, BLUE,
              run_time = 1,
              rate_func = there_and_back)

    self.play(rects[1].shift, SHIFT_DOWN + RIGHT*2.75)

    self.play(rects[2].set_color, BLUE,
          rects[0].set_color, BLUE,
          run_time = 1,
          rate_func = there_and_back)
    
    self.play(rects[0].shift, SHIFT_DOWN + RIGHT*2.75)
    self.play(rects[2].shift, SHIFT_DOWN + RIGHT*1)

    self.play(rects[4].set_color, BLUE,
              rects[6].set_color, BLUE,
              run_time = 1,
              rate_func = there_and_back)
    
    self.play(rects[4].shift, SHIFT_DOWN + LEFT)

    self.play(rects[5].set_color, BLUE,
          rects[6].set_color, BLUE,
          run_time = 1,
          rate_func = there_and_back)
    
    self.play(rects[6].shift, SHIFT_DOWN + LEFT*2.75)
    self.play(rects[5].shift, SHIFT_DOWN + LEFT*0.5)

  def draw_seventh(self, rects):
    SHIFT_DOWN = DOWN*1.5
    ## SORT 1
    self.play(rects[3].set_color, BLUE,
      rects[4].set_color, BLUE,
      run_time = 1,
      rate_func = there_and_back)
    
    self.play(rects[3].shift, SHIFT_DOWN + RIGHT)

    ## SORT 2
    self.play(rects[4].set_color, BLUE,
      rects[1].set_color, BLUE,
      run_time = 1,
      rate_func = there_and_back)
    
    self.play(rects[4].shift, SHIFT_DOWN + LEFT*2)

    ## SORT 3
    self.play(rects[6].set_color, BLUE,
      rects[1].set_color, BLUE,
      run_time = 1,
      rate_func = there_and_back)
    
    self.play(rects[6].shift, SHIFT_DOWN + LEFT*2)

    ## SORT 4
    self.play(rects[5].set_color, BLUE,
      rects[1].set_color, BLUE,
      run_time = 1,
      rate_func = there_and_back)
    
    self.play(rects[1].shift, SHIFT_DOWN + RIGHT*2)

    self.play(rects[5].set_color, BLUE,
      rects[0].set_color, BLUE,
      run_time = 1,
      rate_func = there_and_back)
    
    self.play(rects[0].shift, SHIFT_DOWN + RIGHT*2)

    self.play(rects[5].set_color, BLUE,
      rects[2].set_color, BLUE,
      run_time = 1,
      rate_func = there_and_back)
    
    self.play(rects[2].shift, SHIFT_DOWN + RIGHT*2)
    self.play(rects[5].shift, SHIFT_DOWN + LEFT*0.5)