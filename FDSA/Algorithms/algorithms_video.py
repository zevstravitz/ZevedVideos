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

class OOOpeningQuote(OpeningQuote):
    CONFIG = {
        "quote" : [
            "An algorithm must be ", 
            "seen", " to be ", "believed."
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
        "author" : "Donald Knuth"
    }
   

class GoalofVideo(Scene):
    def construct(self):
        goals = TextMobject("Goal: gain intuition for ", "analyzing algorithms")
        goals.set_color_by_tex_to_color_map({
            "analyzing algorithms": BLUE,
        })
        self.play(ShowCreation(goals),
                run_time = 3)
        self.wait(8)

class Algorithms(Scene):
    def construct(self):
        algorithms = TextMobject("Algorithms")
        algorithms.scale(2)
        algorithms.set_color_by_gradient(BLUE, PURPLE)

        self.play(Write(algorithms))

        dfs = TextMobject("Depth First Search").move_to(UP*1.8+RIGHT*3).scale(0.7)
        merge = TextMobject("Merge Sort").move_to(DOWN+RIGHT*2)
        dijk = TextMobject("Dijkstra's Algorithm").move_to(UP*3+LEFT*3).scale(1.2)
        kruskal = TextMobject("Kruskal's Algorithm").move_to(RIGHT*3.5 + DOWN*3)
        heap = TextMobject("Heap Sort").move_to(LEFT*3+DOWN).scale(1.4)
        tree = TextMobject("Tree Traversals").move_to(DOWN*2+LEFT*1)

        algs_list = [dfs, merge, dijk, kruskal, heap, tree]
        for alg in algs_list:
            self.play(Write(alg), run_time = 1, rate_func = linear)

        self.wait(3)


class GuessingGameIntro(Scene):
    def construct(self):
        guessing_game_title = TextMobject("A Simple Guessing Game")
        guessing_game_title.move_to(UP*3)
        guessing_game_title.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(guessing_game_title),
                  run_time = 2)
        self.wait(1)

        LOC = LEFT*6
        points = []
        for i in range(50):
            curr = Dot(LOC)
            curr.set_color(RED)
            curr.scale(0.7)
            
            points.append(curr)
            LOC += RIGHT*0.25
            #### SET THE BLUE DOT
            if i==40: points[22].set_color(BLUE)
        
        points_group = VGroup(*points)
        points_group.move_to(ORIGIN)
        self.play(FadeInFromDown(points_group),
                  run_time = 5)
        
        self.wait(3)

        
        ## Random guessing
        intro_guesses = [points[10], points[45], points[18],
                          points[34], points[25], points[21], points[22]]
        arrows = [Arrow(start=LEFT, end=RIGHT).move_to(intro_guesses[0].get_center() + UP),
                  Arrow(start=RIGHT, end=LEFT).move_to(intro_guesses[1].get_center() + UP),
                  Arrow(start=LEFT, end=RIGHT).move_to(intro_guesses[2].get_center() + UP),
                  Arrow(start=RIGHT, end=LEFT).move_to(intro_guesses[3].get_center() + UP),
                  Arrow(start=RIGHT, end=LEFT).move_to(intro_guesses[4].get_center() + UP),
                  Arrow(start=LEFT, end=RIGHT).move_to(intro_guesses[5].get_center() + UP)]
        
        for arrow in arrows: arrow.scale(0.7) 

        for i in range(len(intro_guesses)):
            if i == len(intro_guesses)-1:
                self.play(intro_guesses[i].scale, 4,
                          intro_guesses[i].set_color, GREEN,
                          run_time = 1.5,
                          rate_func = there_and_back_with_pause)
            else:
                self.play(intro_guesses[i].scale, 3,
                          intro_guesses[i].set_color, WHITE,
                          run_time = 1.5,
                          rate_func = there_and_back)
                self.play(ShowCreation(arrows[i]),
                          run_time = 0.5,
                          rate_func=there_and_back)
        self.wait(4)

class GuessingGameRandom(Scene):
    def construct(self):
        guessing_game_title = TextMobject("Random Guessing")
        guessing_game_title.move_to(UP*3)
        guessing_game_title.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(guessing_game_title),
                  run_time = 1)
        self.wait(1)

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
                  run_time = 1)
        
        ## Random guessing
        random_guesses = [points[20], points[6], points[45],
                          points[2], points[18]]
        arrows = [Arrow(start=LEFT, end=RIGHT).move_to(random_guesses[0].get_center() + UP),
                  Arrow(start=LEFT, end=RIGHT).move_to(random_guesses[1].get_center() + UP),
                  Arrow(start=RIGHT, end=LEFT).move_to(random_guesses[2].get_center() + UP),
                  Arrow(start=LEFT, end=RIGHT).move_to(random_guesses[3].get_center() + UP),
                  Arrow(start=LEFT, end=RIGHT).move_to(random_guesses[4].get_center() + UP)]
        
        for arrow in arrows: arrow.scale(0.7) 

        for i in range(len(random_guesses)):
            self.play(random_guesses[i].scale, 3,
                      random_guesses[i].set_color, WHITE,
                      run_time = 1.5,
                      rate_func = there_and_back)
            self.play(ShowCreation(arrows[i]),
                      run_time = 0.5,
                      rate_func=there_and_back)
        self.wait(4)

class GuessingGameLinear(Scene):
    def construct(self):
        guessing_game_title = TextMobject("Linear Search")
        guessing_game_title.move_to(UP*3)
        guessing_game_title.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(guessing_game_title),
                  run_time = 2)
        self.wait(1)

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

        self.wait()

        ## Random guessing
        lin_guesses = []
        for i in range(40): lin_guesses.append(points[i])
        arrows = []
        for i in range(39): arrows.append(Arrow(start=LEFT, end=RIGHT).move_to(lin_guesses[i].get_center() + UP))
        
        for arrow in arrows: arrow.scale(0.7) 
        
        for i in range(len(lin_guesses)):
            if i == 0:
                self.play(lin_guesses[i].scale, 3,
                          lin_guesses[i].set_color, WHITE,
                          run_time = 0.1,
                          rate_func = there_and_back)
                self.play(ShowCreation(arrows[i]),
                          run_time = 0.05,
                          rate_func=there_and_back)
            if i == len(lin_guesses)-1:
                self.play(lin_guesses[i].scale, 4,
                          lin_guesses[i].set_color, GREEN,
                          run_time = 0.1,
                          rate_func = there_and_back_with_pause)
            else:
                if i != len(arrows)-1:
                    self.play(lin_guesses[i].scale, 3,
                            lin_guesses[i].set_color, WHITE,
                            ReplacementTransform(arrows[i],arrows[i+1], run_time = 2),
                            run_time = 0.25,
                            rate_func = there_and_back)
        self.wait(4)

class GuessingGameBinary(Scene):
    def construct(self):
        guessing_game_title = TextMobject("Binary Search")
        guessing_game_title.move_to(UP*3)
        guessing_game_title.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(guessing_game_title),
                  run_time = 2)
        self.wait(1)

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

class NoteHere(Scene):
    def construct(self):
        note = TextMobject("Note", ": Our strategy affected the number of guesses")
        note.set_color_by_tex_to_color_map({"Note": BLUE})
        self.play(Write(note),
                  run_time = 6)
        self.wait(4)

class PrimitiveOperations(Scene):
    def construct(self):
        title = TextMobject("Primitive Operations")
        title.move_to(UP*3.5)
        title.set_color_by_gradient(BLUE, PURPLE)

        self.play(FadeInFrom(title, TOP),
                  run_time = 3)
        self.wait(3)

        definition = TextMobject("Primitive Operation",": any operation that corresponds to \\\\",
                          " a low-level instruction that runs in constant time.")
        definition.set_color_by_tex_to_color_map({"Primitive Operation": BLUE})
        definition.move_to(UP*2.5)
        self.play(Write(definition),
                  run_time = 5)

        self.wait(5)

        examples_title = TextMobject("Examples",":")
        examples_title.set_color_by_tex_to_color_map({"Examples": BLUE})
        examples_title.move_to(UP*1+ LEFT*5)
        self.play(Write(examples_title),
                  run_time = 2)

        assigning = TextMobject("Assigning"," a value to a variable").move_to(LEFT*4)
        indexing = TextMobject("Indexing"," into an array").move_to(LEFT*4 + DOWN)
        comparing = TextMobject("Comparing"," two numbers").move_to(LEFT*4 + DOWN*2)
        adding = TextMobject("Adding"," two numbers").move_to(RIGHT*4)
        calling = TextMobject("Calling"," a method").move_to(RIGHT*4 + DOWN)
        returning = TextMobject("Returning"," from a method").move_to(RIGHT*4 + DOWN*2)

        assigning.set_color_by_tex_to_color_map({"Assigning": PURPLE})
        indexing.set_color_by_tex_to_color_map({"Indexing": PURPLE})
        comparing.set_color_by_tex_to_color_map({"Comparing": PURPLE})
        adding.set_color_by_tex_to_color_map({"Adding": PURPLE})
        calling.set_color_by_tex_to_color_map({"Calling": PURPLE})
        returning.set_color_by_tex_to_color_map({"Returning": PURPLE})

        assigning.align_to(indexing, LEFT)
        comparing.align_to(assigning, LEFT)
        adding.align_to(calling, LEFT)
        returning.align_to(adding, LEFT)


        prims = VGroup(assigning, indexing, comparing, adding, calling, returning)
        prims.scale(0.8)
        prims.move_to(ORIGIN + DOWN)
        
        self.play(Write(assigning))
        self.play(Write(indexing))
        self.play(Write(comparing))
        self.play(Write(adding))
        self.play(Write(calling))
        self.play(Write(returning))
        
        self.wait(6)

class PrimOpsTime(Scene):
    def construct(self):
        who_cares = TextMobject("Who cares about primitive operations anyways?")
        is_related = TextMobject("Primitive operations take ", "time")
        is_related.set_color_by_tex_to_color_map({"time": BLUE})
        self.play(FadeInFromDown(who_cares))
        self.wait(3)
        self.play(who_cares.shift, UP*3,
                  run_time = 2)
        
        self.play(Write(is_related), run_time = 2)
        
        self.wait(6)



class GuessisPrim(Scene):
    def construct(self):
        line = TextMobject("Guess" ," = ", "1 Primitive Operation")
        line.set_color_by_tex_to_color_map({
            "Guess": PURPLE,
            "1 Primitive Operation" : BLUE
        })
        self.play(Write(line))
        self.wait(8)

class KeyIdea(Scene):
    def construct(self):
        title = TextMobject("K", "e","y", "\\ I", "d", "e", "a")
        title.move_to(UP*3)
        title.set_color_by_tex_to_color_map({
            "K": RED_B,
            "e" : YELLOW_B,
            "y" : GREEN_B,
            "\\ I" : BLUE_B,
            "d" : ORANGE,
            "e" : PINK,
            "a" : PURPLE_B
        })
        self.play(Write(title))
        self.wait(3)
        key_idea = TextMobject("How does the number of primitive operations \\\\",
                                "relate to the size of our input?")

        self.play(Write(key_idea), run_time = 5, rate_func = linear)

        self.wait(8)

class BigO(Scene):
    def construct(self):
        title = TextMobject("Big O Notation")
        title.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(title))

        self.play(title.shift, UP*3,
                  run_time = 2)
        self.wait(3)

        definition = TextMobject("Big O notation refers to the \\\\",
                                 "limiting", " behavior of a function.")
        definition.move_to(UP)
        definition.set_color_by_tex_to_color_map({"limiting": BLUE})
        self.play(Write(definition))

        self.wait(8)


class BigOGraph(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 50,
        "x_axis_width": 9,
        "x_tick_frequency": 50,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$n$",
        "y_min": 0,
        "y_max": 50,
        "y_axis_height": 6,
        "y_tick_frequency": 2,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$O(log(n))$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):
        self.setup_axes(animate=True)
        num_dots = TextMobject("Number of dots")
        num_dots.move_to(DOWN*3)

        num_guesses = TextMobject("Number of guesses")
        num_guesses.move_to(LEFT*4.5 + UP*0.3)
        num_guesses.rotate(PI/2)

        self.play(Write(num_dots),
                    Write(num_guesses))

        self.wait(3)

        log_funct = self.get_graph(self.log, PINK)
        self.play(ShowCreation(log_funct))

        self.wait(5)

        plotted = [Dot(2.4 * DOWN + 2 * LEFT),
                   Dot(2.4 * DOWN + 2.4 * LEFT),
                   Dot(2.3 * DOWN + 2.2 * LEFT),
                   Dot(2.4 * DOWN + RIGHT),
                   Dot(2.4 * DOWN + 2 * RIGHT),
                   Dot(2.2 * DOWN + 2.4 * RIGHT),
                   Dot(2.4 * DOWN + 2.8 * LEFT),
                   Dot(2.2 * DOWN + 2.7 * RIGHT),
                   Dot(2.3 * DOWN + 2.9 * RIGHT),
                   Dot(2.28 * DOWN + 3.1 * RIGHT),
                   Dot(2.24 * DOWN + 3.2 * RIGHT),
                   Dot(2.18 * DOWN + 3.4 * RIGHT),
                   Dot(2.15 * DOWN + 3.7 * RIGHT),
                   Dot(2.13 * DOWN + 4 * RIGHT)
                   ]

        for i in plotted:
            self.play(FadeInFromLarge(i),
                      run_time = 0.5)

        self.wait(4)
        lines = self.get_vertical_lines_to_graph(log_funct, x_min=1,
                                        x_max=100, num_lines=1000,
                                        color=BLUE)
        self.play(FadeInFromDown(lines))
        self.wait(7)
        
        lin_funct = self.get_graph(self.linear, PINK)
        self.play(ShowCreation(lin_funct))
        quad_funct = self.get_graph(self.quadratic, PINK)
        self.play(ShowCreation(quad_funct))
        self.wait(4)


    # O(log(n))
    def log(self,x):
        return np.log(x)

    def linear(self, x):
        return x
    
    def quadratic(self, x):
        return x**2



class DropConstants(Scene):
    def construct(self):
        text = TextMobject("We only care about behavior at \\\\", "very large", " values of n")
        text.move_to(UP*2)
        text.set_color_by_tex_to_color_map({"very large": BLUE})

        a = TexMobject("a")
        logn = TexMobject("log(n)")
        plusb = TextMobject("+ ", "b")

        a.set_color(RED)
        plusb.set_color_by_tex_to_color_map({"b": BLUE})

        a.next_to(logn, LEFT)
        plusb.next_to(logn, RIGHT)

        self.play(Write(text),
                  run_time = 3)

        self.wait(2)
        self.play(Write(a),
                  Write(logn),
                  Write(plusb),
                  run_time = 2)

        self.wait(3)
        self.play(FadeOutAndShiftDown(a),
                  FadeOutAndShiftDown(plusb))

        self.wait(6)

class VisualizeLinear(Scene):
    def construct(self):
        LOC = LEFT*2
        points = []
        for i in range(5):
            curr = Dot(LOC)
            curr.set_color(RED)
            
            points.append(curr)
            LOC += RIGHT
            if i==3: points[3].set_color(BLUE)
            self.play(FadeInFromDown(points[i]),
                      run_time = 1)
        self.wait()

class Constant(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_axis_width": 9,
        "x_tick_frequency": 10,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$n$",
        "y_min": 0,
        "y_max": 10,
        "y_axis_height": 4,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$O(1)$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):
      self.setup_axes(animate=True)
      funct_label = TextMobject("Constant Time").set_color_by_gradient(BLUE, PURPLE)
      funct_label.move_to(UP*3.2)
      self.play(Write(funct_label))

      const_funct=self.get_graph(self.constant, PINK)
      self.play(ShowCreation(const_funct))
      self.wait(10)
    
    # O(1)
    def constant(self,x):
        return 2

class NLogN(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_axis_width": 9,
        "x_tick_frequency": 10,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$n$",
        "y_min": 0,
        "y_max": 10,
        "y_axis_height": 4,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$O(nlog(n))$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):
        self.setup_axes(animate=True)
        funct_label = TextMobject("nlog(n) Time").set_color_by_gradient(BLUE, PURPLE)
        funct_label.move_to(UP*3)
        self.play(Write(funct_label))
        log_funct=self.get_graph(self.log, PINK)
        self.play(ShowCreation(log_funct))
        self.wait(13)

    # O(nlogn)
    def log(self,x):
        return x*np.log(x)

class Linear(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_axis_width": 9,
        "x_tick_frequency": 10,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$n$",
        "y_min": 0,
        "y_max": 10,
        "y_axis_height": 4,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$O(n)$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):
      self.setup_axes(animate=True)
      funct_label = TextMobject("Linear Time").set_color_by_gradient(BLUE, PURPLE)
      funct_label.move_to(UP*3)
      self.play(Write(funct_label))
      lin_funct=self.get_graph(self.linear, PINK)
      self.play(ShowCreation(lin_funct))
      self.wait(6)

    # O(n)
    def linear(self,x):
        return x

class LinearTraversal(Scene):
    def construct(self):
        guessing_game_title = TextMobject("Linear Time")
        guessing_game_title.move_to(UP*3)
        guessing_game_title.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(guessing_game_title),
                  run_time = 1)

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
                  run_time = 1)

        ## Random guessing
        lin_guesses = []
        for i in range(40): lin_guesses.append(points[i])
        arrows = []
        for i in range(39): arrows.append(Arrow(start=LEFT, end=RIGHT).move_to(lin_guesses[i].get_center() + UP))
        
        for arrow in arrows: arrow.scale(0.7) 
        
        for i in range(len(lin_guesses)):
            if i == len(lin_guesses)-1:
                self.play(lin_guesses[i].scale, 4,
                          lin_guesses[i].set_color, GREEN,
                          run_time = 0.1,
                          rate_func = there_and_back_with_pause)
            else:
                self.play(lin_guesses[i].scale, 3,
                          lin_guesses[i].set_color, WHITE,
                          run_time = 0.3,
                          rate_func = there_and_back)

        self.wait(4)


class Quadratic(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_axis_width": 9,
        "x_tick_frequency": 10,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$n$",
        "y_min": 0,
        "y_max": 10,
        "y_axis_height": 4,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$O(n^2)$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):
      self.setup_axes(animate=True)
      funct_label = TextMobject("Quadratic Time").set_color_by_gradient(BLUE, PURPLE)
      funct_label.move_to(UP*3)
      quadratic_funct=self.get_graph(self.quadratic, PINK)
      self.play(ShowCreation(quadratic_funct),
                Write(funct_label))
      self.wait(10)
    # O(n)
    def quadratic(self,x):
        return x**2

class QuadraticTraversal(Scene):
    def construct(self):
        guessing_game_title = TextMobject("Quadratic Time")
        guessing_game_title.move_to(UP*3)
        guessing_game_title.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(guessing_game_title),
                  run_time = 1)

        LOC = LEFT*6
        points = []
        for i in range(10):
            for i in range(10):
                curr = Dot(LOC)
                curr.set_color(RED)
                curr.scale(0.7)
                
                points.append(curr)
                LOC += RIGHT*0.25
                if i==40: points[40].set_color(BLUE)
            LOC = LOC + DOWN*0.25 + LEFT*.25*10
        
        points_group = VGroup(*points)
        points_group.move_to(ORIGIN)

        braces_top = Brace(points_group,UP)
        bt_text = braces_top.get_text("n")
        braces_left = Brace(points_group,LEFT)
        bl_text = braces_left.get_text("n")

        self.play(FadeInFromDown(points_group),
                  FadeInFrom(braces_top, UP),
                  FadeInFrom(bt_text, RIGHT),
                  FadeInFrom(braces_left, LEFT),
                  FadeInFrom(bl_text, DOWN),
                  run_time = 1)

        ## Random guessing
        lin_guesses = []
        for i in range(20): lin_guesses.append(points[i])
        
        for i in range(len(lin_guesses)):
            if i == len(lin_guesses)-1:
                self.play(lin_guesses[i].scale, 4,
                          lin_guesses[i].set_color, GREEN,
                          run_time = 0.1,
                          rate_func = there_and_back_with_pause)
            if i == 40:
                brea
            else:
                self.play(lin_guesses[i].scale, 3,
                          lin_guesses[i].set_color, WHITE,
                          run_time = 0.3,
                          rate_func = there_and_back)

        self.wait(4)

class BigOFunctions(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 50,
        "x_axis_width": 9,
        "x_tick_frequency": 50,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$n$",
        "y_min": 0,
        "y_max": 50,
        "y_axis_height": 6,
        "y_tick_frequency": 2,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$y$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):
      big_o = TextMobject("Big O \\\\", "Functions")
      big_o.move_to(5.5*LEFT)

      self.setup_axes(animate=True)
      self.play(FadeInFrom(big_o, LEFT))

      const_funct=self.get_graph(self.constant, RED)
      lin_funct=self.get_graph(self.linear, PINK)
      log_funct=self.get_graph(self.logarithmic, BLUE)
      nlogn_funct=self.get_graph(self.nlogn, GREEN)
      quad_funct=self.get_graph(self.quadratic, YELLOW)
      cubic_funct=self.get_graph(self.cubic, MAROON_A)

      self.play(ShowCreation(const_funct),ShowCreation(lin_funct),
                ShowCreation(log_funct),ShowCreation(nlogn_funct),
                ShowCreation(quad_funct), ShowCreation(cubic_funct))
      
      self.wait(10)
    # O(1)
    def constant(self,x):
      return 1

    # O(n)
    def linear(self,x):
        return x

    # O(nlogn)
    def logarithmic(self,x):
        return np.log(x)

    def nlogn(self,x):
      return x*np.log(x)

    # O(n^2)
    def quadratic(self,x):
      return x**2

    def cubic(self,x):
      return x**3  

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