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
            "Computer Science is no more about",
            "computers \\\\",
            "than astronomy is about", "telescopes."
        ],
        "highlighted_quote_terms": {
          "computers" : BLUE,
          "telescopes": PURPLE
        },
        "fade_in_kwargs": {
            "lag_ratio": 0.5,
            "rate_func": linear,
            "run_time": 3,
        },
        "author" : "Edsger W.Dijkstra"
    }

class GoalofVideo(Scene):
  def construct(self):
    goals = TextMobject("Goal: gain intuition for how ", "objects",
                        " work \\\\",
                        "and why they are useful in programming.")
    goals.set_color_by_tex_to_color_map({
      "objects": BLUE
    })
    self.play(ShowCreation(goals),
              run_time = 3)
    self.wait(6)

class WhatIsAnObject(Scene):
  def construct(self):
    # circle = Circle()
    # circle.set_color(BLUE)
    # self.play(ShowCreation(circle),
    #           run_time = 3)
    #self.wait()

    question = TextMobject("What is an Object?")
    self.play(Write(question),
              run_time = 1)
    self.wait(1.5)
    object_def = TextMobject("Object: ", "Instance", " of a class")
    object_def.set_color_by_tex_to_color_map({"Instance": BLUE})
    self.play(question.shift, UP,
              ShowCreation(object_def),
              run_time = 2)
    self.wait(1)
    class_def = TextMobject("Class: ", "Template" ," for constructing objects")
    class_def.set_color_by_tex_to_color_map({"Template": RED})
    class_def.move_to(DOWN)
    self.play(ShowCreation(class_def),
              run_time = 2)
    self.wait(2)

    class_cyc = TextMobject("Class")
    class_cyc.move_to(UP).set_color(BLUE)
    object_cyc = TextMobject("Object")
    object_cyc.move_to(DOWN).set_color(RED)

    c_to_o = Arrow(start = class_cyc.get_center() + LEFT,
                    end = object_cyc.get_center() + LEFT, path_arc = PI)
    c_to_o_label = TextMobject("Template for \\\\ constructing an")
    c_to_o_label.next_to(c_to_o, LEFT)
    o_to_c = Arrow(start = object_cyc.get_center() + RIGHT,
                    end = class_cyc.get_center() + RIGHT, path_arc = PI)
    o_to_c_label = TextMobject("Instance of a")
    o_to_c_label.next_to(o_to_c, RIGHT)

    class_obj_def = VGroup(object_def, class_def)
    class_obj_cycle = VGroup(class_cyc, object_cyc, c_to_o, c_to_o_label,
                            o_to_c, o_to_c_label)
    class_obj_cycle.scale(1)

    self.play(FadeOutAndShift(question, UP),
              ReplacementTransform(class_obj_def, class_obj_cycle),
              run_time = 2)

    self.wait(10)

    instances_def = TextMobject("Instance = Object (For Now)")
    self.play(FadeOut(class_obj_cycle),
              ShowCreation(instances_def))
    self.wait(10)

class ClassComponents(Scene):
  def construct(self):
    class_components = TextMobject("Class Components")
    class_components.move_to(UP*2)

    fields_title = TextMobject("Fields")
    fields_title.set_color_by_tex_to_color_map({"Fields": GREEN})
    fields_def = TextMobject(": State of object")
    
    methods_title = TextMobject("Methods")
    methods_title.set_color_by_tex_to_color_map({"Methods": RED})
    methods_title.move_to(DOWN)
    methods_def = TextMobject(": Behavior of object")
    
    fields_meth=VGroup(fields_title, methods_title)
    fields_meth.shift(LEFT)
    
    fields_def.next_to(fields_title, RIGHT)
    methods_def.next_to(methods_title, RIGHT)

    braces= Brace(fields_meth, LEFT)
    class_text = braces.get_text("Class")
    class_text.set_color_by_tex_to_color_map({"Class": BLUE})

    self.play(Write(class_components),
              Write(fields_title), Write(methods_title),
              FadeInFrom(class_text, UP),
              FadeInFrom(braces, DOWN),
              run_time = 4)
    self.wait(2)
    self.play(Write(fields_def),
              run_time = 3)
    self.play(Write(methods_def),
          run_time = 3)   
    
    self.wait(7)

class IntroScene(Scene):
  def construct(self):
    intro = TextMobject("So...what is Object-oriented Programming?")
    intro.set_color_by_gradient(BLUE, PURPLE)
    self.play(GrowFromCenter(intro))
    self.wait(5)

    class_text = TextMobject("Class")
    class_text_box = SurroundingRectangle(class_text)
    class_text_box.scale(3)
    class_text_box.set_color(BLUE)
    class_wrapper = VGroup(class_text, class_text_box)

    self.play(Transform(intro, class_text),
              FadeIn(class_text_box),
              run_time = 3,
              rate_func = linear)
    
    self.wait(3)
    
    object_text = TextMobject("Object").move_to(RIGHT*2)
    object_text_box = SurroundingRectangle(object_text)
    object_text_box.scale(3)
    object_text_box.set_color(BLUE)
    object_wrapper = VGroup(object_text, object_text_box)

    self.play(class_wrapper.shift, LEFT*2,
              FadeInFrom(object_wrapper, RIGHT),
              run_time = 2)
    
    self.wait()

class RectangleExample(Scene):
  def construct(self):
    # rect_example_text_up = rect_example_text.copy()
    # rect_example_text_up.move_to(UP*3)
    # self.play(Transform(rect_example_text, rect_example_text_up))

    rect = Rectangle(color=PINK)
    rect.set_fill(PINK, opacity=0.5)
    rect2 = Rectangle(color=PINK)
    rect2.move_to(LEFT*4)

    self.play(DrawBorderThenFill(rect))
    self.wait(2)
    self.play(ReplacementTransform(rect, rect2))

    rect_example_text = TextMobject("A Rectangle Object")
    rect_example_text.move_to(UP*3)
    rect_example_text.set_color_by_gradient(BLUE, PURPLE)
    self.play(FadeIn(rect_example_text))
    self.wait(3)

    self.change_fields(rect2)

  def change_fields(self, rect2):
    rect_length_text = TexMobject("Length = ")
    rect_length_text.shift(UP)
    rect_width_text = TexMobject("Width = ")
    rect_color_text = TexMobject("Color = ")
    rect_color_text.shift(DOWN)

    l_and_w = VGroup(rect_length_text, rect_width_text)
    attributes = VGroup(rect_length_text, rect_width_text, rect_color_text)
    attributes.shift(RIGHT*2)
    braces = Brace(attributes,LEFT)

    # Fill in the values in the brackets
    self.play(GrowFromEdge(braces, DOWN), FadeInFromDown(l_and_w))
    self.wait(2)
    self.play(FadeInFrom(rect_color_text, DOWN))
    self.wait(3)


    changing_length = DecimalNumber(
            2.0,
            num_decimal_places=1
    )

    changing_width = DecimalNumber(
        4.0,
        num_decimal_places=1
    )

    color1 = TextMobject("PINK")
    color2 = TextMobject("GREEN")

    changing_length.add_updater(lambda rect_length: rect_length.next_to(rect_length_text))
    changing_length.add_updater(lambda rect_length: rect_length.set_value(rect2.get_height()))
    self.add(changing_length)

    changing_width.add_updater(lambda rect_angle: rect_angle.next_to(rect_width_text, RIGHT))
    changing_width.add_updater(lambda rect_angle: rect_angle.set_value(rect2.get_width()))
    self.add(changing_width)

    color1.next_to(rect_color_text, RIGHT)
    color2.next_to(rect_color_text, RIGHT)
    self.add(color1)

    # Changing Length Animation Play
    self.play(rect2.stretch_to_fit_height, 4.0,
              run_time=3,
              rate_func=there_and_back)
    self.wait(1.5)

    # Changing Width Animation Play
    self.play(rect2.stretch_to_fit_width, 2.0,
              run_time=3,
              rate_func=there_and_back)
    self.wait(1.5)

    # Changing Color Animation Play
    # new_color = Rectangle(color=GREEN)
    # new_color.move_to(LEFT*4)
    self.play(Transform(color1, color2),
              rect2.set_color, GREEN,
              run_time=2)

    self.wait(8)

    fields_and_braces_wrapper = VGroup(color1,
                                       attributes, braces
                                       )

    set_length_funct = TexMobject("set\\_length(\\textit{length})")
    set_width_funct = TexMobject("set\\_width(\\textit{width})").shift(DOWN)
    set_color_funct = TexMobject("set\\_color(\\textit{color})").shift(DOWN*2)

    methods_wrapper = VGroup(set_length_funct, set_width_funct, set_color_funct)
    methods_wrapper.shift(RIGHT*2.8 + DOWN)
    methods_braces = Brace(methods_wrapper,LEFT)

    fields_text_title = TextMobject("Fields").next_to(braces, LEFT).shift(UP)
    methods_text_title = TextMobject("Methods").next_to(methods_braces, LEFT)
    self.play(fields_and_braces_wrapper.shift, UP,
              Write(fields_text_title),
              Write(methods_text_title),
              GrowFromEdge(methods_braces, DOWN),
              FadeInFrom(methods_wrapper, BOTTOM),
              rect2.shift, DOWN,
              run_time=3)
    self.wait(7)

    # Length Function Call
    set_length_with_num = TexMobject("set\\_length(4.0)")
    set_length_with_num.move_to(rect2.get_center() + 2.4*UP)
    
    self.play(Write(set_length_with_num))
    self.play(set_length_with_num.scale, 1.25,
              rate_func = there_and_back,
              run_time = 0.5)
    self.wait()
    self.play(rect2.stretch_to_fit_height, 4.0,
              run_time = 2)

    self.wait(3)

    # Width Function Call
    set_width_with_num = TexMobject("set\\_width(2.0)")
    set_width_with_num.move_to(rect2.get_center() + 2.4*UP)

    self.play(ReplacementTransform(set_length_with_num, set_width_with_num))
    self.play(set_width_with_num.scale, 1.25,
              rate_func = there_and_back,
              run_time = 0.5)
    self.wait()
    red_color = TextMobject("PINK").next_to(rect_color_text, RIGHT)
    self.play(rect2.stretch_to_fit_width, 2.0,
              run_time = 2)

    self.wait()

    # Color Function Call
    set_color_with_num = TextMobject("set\\_color(``PINK'')")
    set_color_with_num.move_to(rect2.get_center() + 2.4*UP)

    self.play(ReplacementTransform(set_width_with_num, set_color_with_num))
    self.play(set_color_with_num.scale, 1.25,
              rate_func = there_and_back,
              run_time = 0.5)
    self.wait()
    self.play(rect2.set_color, PINK,
              Transform(color1, red_color),
              run_time = 2)
    self.play(FadeOutAndShift(set_color_with_num, UP),
              rect2.shift, UP,
              run_time = 1)
    self.wait(6)

    get_length_funct = TexMobject("get\\_length()")
    get_width_funct = TexMobject("get\\_width()").shift(DOWN)
    get_color_funct = TexMobject("get\\_color()").shift(DOWN*2)

    getter_wrapper = VGroup(get_length_funct, get_width_funct, get_color_funct)
    getter_wrapper.shift(RIGHT*2.3 + DOWN)
    self.play(ReplacementTransform(methods_wrapper, getter_wrapper),
              run_time = 2)
    self.wait()
    
    get_length_result = TexMobject("\\Rightarrow 4.0").next_to(get_length_funct, RIGHT)
    get_width_result = TexMobject("\\Rightarrow 2.0").next_to(get_width_funct, RIGHT)
    get_color_result = TexMobject("\\Rightarrow PINK").next_to(get_color_funct)

    getters = [get_length_funct, get_width_funct, get_color_funct]
    getter_results = [get_length_result, get_width_result, get_color_result]
    for getter_index in range(len(getters)):
      self.play(getters[getter_index].scale, 1.25,
                rate_func = there_and_back,
                run_time = 0.5)
      self.play(FadeIn(getter_results[getter_index]), run_time = 1)
      self.wait()

    self.wait(3)

class ShoppingCart(Scene):
  def construct(self):
    # self.show_headfirst()
    shopping_cart_text = TextMobject("A Shopping Cart Object").move_to(3*UP)

    # Alarm Clock Drawing
    shoppingcart_body = Polygon(UP*0.5 + LEFT,
                                UP*0.8 + RIGHT,
                                DOWN*0.5 + RIGHT,
                                DOWN*0.5 + LEFT,
                                color = PURPLE)
    wheel_1 = Circle(radius=0.1).shift(LEFT*0.5 + DOWN*0.8)
    wheel_2 = Circle(radius=0.1).shift(RIGHT*0.6 + DOWN*0.8)
    handle = Line(start = UP*0.8 + RIGHT, end = UP + RIGHT*1.1)
    shopping_cart = VGroup(shoppingcart_body, wheel_1, wheel_2, handle)

    self.play(GrowFromEdge(shopping_cart, BOTTOM))
    self.wait(1)
    self.play(shopping_cart.shift, RIGHT*5.5 + UP*2.5,
              run_time = 2
    )
    self.play(FadeInFrom(shopping_cart_text, TOP))
    self.wait(0.5)

    #Title of Table
    fields_title = TextMobject("Fields").shift(LEFT*2 + UP*2)
    method_title = TextMobject("Methods").shift(RIGHT*2 + UP*2)

    title_wrapper = VGroup(fields_title, method_title)
    self.play(Write(title_wrapper),
              run_time=1)
    self.wait()

    # Contents of Table
    fields_wrapper = Rectangle(height = 4.5, width = 4.0).move_to(LEFT*2 + DOWN)
    fields_wrapper.set_fill(BLUE, opacity=0.5)
    method_wrapper = Rectangle(height = 4.5, width = 4.0).move_to(RIGHT*2 + DOWN)
    method_wrapper.set_fill(PURPLE, opacity=0.5)

    fieldmethod_wrapper = VGroup(fields_wrapper, method_wrapper)
    self.play(DrawBorderThenFill(fieldmethod_wrapper),
              run_time=1)
    self.wait()
    
    # FILL IN TABLE
    self.fill_in_table()

  def fill_in_table(self):
    # Filling in Fields
    freq = TexMobject("cart\\_items").shift(LEFT*2 + UP*0.5)
    self.play(Write(freq))
    self.wait(2)

    # Filling in Methods
    add_item = TexMobject("add\\_item(\\textit{item})").shift(RIGHT*2 + UP*0.5)
    add_item.scale(0.75)
    self.play(Write(add_item))
    self.wait()
    remove_item = TexMobject("remove\\_item(\\textit{item})").shift(RIGHT*2 + DOWN*0.5)
    remove_item.scale(0.75)
    self.play(Write(remove_item))
    self.wait()
    check_out = TexMobject("check\\_out()").shift(RIGHT*2 + DOWN*1.5)
    check_out.scale(0.75)
    self.play(Write(check_out))
    self.wait()
    is_full = TexMobject("is\\_full()").shift(RIGHT*2 + DOWN*2.5)
    is_full.scale(0.75)
    self.play(Write(is_full))
    self.wait()

    get_items = TexMobject("get\\_items()").shift(RIGHT*2 + UP*0.5)
    do_group = VGroup(add_item, remove_item, check_out, is_full)
    self.play(Transform(do_group, get_items))
    self.wait(3)

class FieldsMethods(Scene):
  def construct(self):
    # self.show_headfirst()
    radio_clock_text = TextMobject("A Radio Object").move_to(3*UP)

    # Alarm Clock Drawing
    radio_body = Rectangle(height=1.0, width=2.0, color = PURPLE)
    knob = Circle(radius=0.25).shift(LEFT*0.5)
    antenna = Line(start = RIGHT*0.5 + UP*0.5, end = RIGHT*0.5 + UP)
    dial = Dot(point = RIGHT*0.5)
    
    radio = VGroup(radio_body, knob, antenna, dial)

    self.play(GrowFromEdge(radio, BOTTOM))
    self.wait(1)
    self.play(radio.shift, RIGHT*5.5 + UP*2.5,
              run_time = 2
    )
    self.play(FadeInFrom(radio_clock_text, TOP))
    self.wait(0.5)

    #Title of Table
    fields_title = TextMobject("Fields").shift(LEFT*2 + UP*2)
    method_title = TextMobject("Methods").shift(RIGHT*2 + UP*2)

    title_wrapper = VGroup(fields_title, method_title)
    self.play(Write(title_wrapper),
              run_time=1)
    self.wait()

    # Contents of Table
    fields_wrapper = Rectangle(height = 4.5, width = 4.0).move_to(LEFT*2 + DOWN)
    fields_wrapper.set_fill(RED, opacity=0.5)
    method_wrapper = Rectangle(height = 4.5, width = 4.0).move_to(RIGHT*2 + DOWN)
    method_wrapper.set_fill(BLUE, opacity=0.5)

    fieldmethod_wrapper = VGroup(fields_wrapper, method_wrapper)
    self.play(DrawBorderThenFill(fieldmethod_wrapper),
              run_time=1)
    self.wait()
    
    # FILL IN TABLE
    self.fill_in_table()

  def fill_in_table(self):
    # Filling in Fields
    freq = TextMobject("Frequency").shift(LEFT*2 + UP*0.5)
    self.play(Write(freq))
    self.wait(2)
    mode = TextMobject("Mode").shift(LEFT*2 + DOWN*0.5)
    self.play(Write(mode))
    self.wait(2)
    volume = TextMobject("Volume").shift(LEFT*2 + DOWN*1.5)
    self.play(Write(volume))
    self.wait(4)

    # Filling in Methods
    set_freq = TexMobject("set\\_frequency(\\textit{freq})").shift(RIGHT*2 + UP*0.5)
    set_freq.scale(0.8)
    self.play(Write(set_freq))
    self.wait(2)
    set_mode = TexMobject("set\\_mode(\\textit{mode})").shift(RIGHT*2 + DOWN*0.5)
    set_mode.scale(0.8)
    self.play(Write(set_mode))
    self.wait(2)
    set_volume = TexMobject("set\\_volume(\\textit{volume})").shift(RIGHT*2 + DOWN*1.5)
    set_volume.scale(0.8)
    self.play(Write(set_volume))
    self.wait(3)
    get_frequency= TexMobject("get\\_frequency()").shift(RIGHT*2 + UP*0.5)
    get_mode = TexMobject("get\\_mode()").shift(RIGHT*2 + DOWN*0.5)
    get_volume = TexMobject("get\\_volume()").shift(RIGHT*2 + DOWN*1.5)

    set_group = VGroup(set_freq, set_mode, set_volume)
    get_group = VGroup(get_frequency, get_mode, get_volume)
    self.play(Transform(set_group, get_group))
    self.wait(3)

  def show_headfirst(self):
    cover = ImageMobject("headfirst")
    self.play(ShowCreation(cover))

class StickManExample(Scene):
  def construct(self):
    person_label = TextMobject("A (Bad) Drawing of You").shift(UP*3)

    head = Circle(radius=0.5).shift(UP*1.5)
    body = Line(start=UP, end = DOWN)
    left_arm = Line(start=ORIGIN, end=LEFT + UP)
    right_arm = Line(start=ORIGIN, end=RIGHT + UP)
    left_leg = Line(start=DOWN, end=LEFT + DOWN*2)
    right_leg = Line(start=DOWN, end=RIGHT + DOWN*2)

    person_drawing = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)

    self.play(Write(person_label),
              ShowCreation(person_drawing),
              run_time = 2)

    self.wait(3)
    person_arrows_labels = TextMobject("Your ``Fields''").shift(UP*3)
    self.play(Transform(person_label, person_arrows_labels))
    age = TextMobject("Age").shift(RIGHT*3.5 + UP*1.5)
    age_arrow = Arrow(start=RIGHT+UP, end=RIGHT*3 + UP*1.5)
    self.play(ShowCreation(age_arrow),
              Write(age))

    name = TextMobject("Name").shift(RIGHT*3.5 + DOWN*1.5)
    name_arrow = Arrow(start=RIGHT+DOWN, end=RIGHT*3 + DOWN*1.5)
    self.play(ShowCreation(name_arrow),
              Write(name))

    birthday = TextMobject("Birthday").shift(LEFT*4 + UP*1.5)
    birthday_arrow = Arrow(start=LEFT+UP, end=LEFT*3 + UP*1.5)
    self.play(ShowCreation(birthday_arrow),
              Write(birthday))

    height = TextMobject("Height").shift(LEFT*4 + DOWN*1.5)
    height_arrow = Arrow(start=LEFT+DOWN, end=LEFT*3 + DOWN*1.5)
    self.play(ShowCreation(height_arrow),
              Write(height))

    self.wait(2)

    you_wrapper = VGroup(person_arrows_labels, age, age_arrow,
                        name, name_arrow,
                        birthday, birthday_arrow,
                        height, height_arrow,
                        person_drawing, person_label)
                    
    abstraction_big = TextMobject("Abstraction").scale(4)
    abstraction_big.set_color_by_gradient(RED, BLUE)
    self.play(Transform(you_wrapper, abstraction_big))
    self.wait(4)

class EssenceOfOOProgramming(Scene):
  def construct(self):
    essence = TexMobject()

    self.play(Write(essence),
              run_time=4,
              rate_func=linear)
 

class Inheritance(Scene):
  def construct(self):
    inheritance_title = TextMobject("Inheritance")
    inheritance_title.set_color_by_gradient(BLUE, PURPLE)
    self.play(Write(inheritance_title),
              inheritance_title.scale, 2,
              inheritance_title.shift, UP*3,
              run_time = 3)
    #inheritance_title.shift(UP*3)

    rectangles_class_shape = Rectangle(height=1.0, width=2.0, color = RED)
    rectangle_label = TextMobject("Rectangle")
    rectangle_label.scale(0.5)

    rectangles_class = VGroup(rectangles_class_shape, rectangle_label)
    rectangles_class.scale(2)

    self.play(FadeInFromLarge(rectangles_class),
              run_time = 3)

    square_class_shape = Square(side_length=1.0, color = BLUE)
    square_label = TextMobject("Square")
    square_label.scale(0.5)

    squares_class = VGroup(square_class_shape, square_label)
    squares_class.scale(1.8).move_to(DOWN*2)

    self.play(inheritance_title.scale, 0.8,
              rectangles_class.scale, 0.9,
              rectangles_class.shift, UP*1,
              FadeInFromDown(squares_class),
              run_time = 2)

    self.wait(8)

    square_to_rect_arrow = Arrow(start=DOWN, end=UP*0.1)
    square_to_rect_label = TextMobject("Inherits")
    square_to_rect_label.next_to(square_to_rect_arrow)
    square_to_rect_group = VGroup(square_to_rect_arrow, square_to_rect_label)
    self.play(GrowArrow(square_to_rect_arrow),
              Write(square_to_rect_label))
    self.wait(6)

    square_and_rect_classes = VGroup(rectangles_class,
                                      squares_class,
                                      square_to_rect_group)
    self.play(square_and_rect_classes.scale, 0.75,
              square_and_rect_classes.shift, DOWN*1.25,
              run_time = 3)

    self.wait()

    shifting = [2, 0.6, 0.8, 1.5]
    parallelogram_class_shape = Polygon(UP*shifting[0] + LEFT*shifting[1], UP*shifting[0] + RIGHT*shifting[2],
                                        RIGHT*shifting[1] + UP*shifting[3], LEFT*shifting[2] + UP*shifting[3])
    parallelogram_class_shape.set_color(GREEN)
    parallelogram_label = TextMobject("Parallelogram")
    parallelogram_label.scale(0.4).move_to(parallelogram_class_shape.get_center())

    parallelograms_class = VGroup(parallelogram_class_shape, parallelogram_label)
    parallelograms_class.scale(1.6)

    rect_to_par_arrow = square_to_rect_arrow = Arrow(start=UP*0, end=UP*1.5)
    rect_to_par_label = TextMobject("Inherits").scale(0.6)
    rect_to_par_label.next_to(rect_to_par_arrow)
    rect_to_par_group = VGroup(rect_to_par_arrow, rect_to_par_label)

    self.play(parallelogram_class_shape.shift, UP,
              FadeInFrom(parallelograms_class, UP),
              GrowArrow(square_to_rect_arrow),
              Write(rect_to_par_label))

    self.wait(4)
    
    new_rect_to_par_arrow = square_to_rect_arrow = Arrow(start=RIGHT*1.5,
                                                          end=parallelogram_class_shape.get_center() + DOWN*0.5,
                                                          stroke_width = 3)
    new_rect_to_par_label = TextMobject("Inherits").scale(0.7)
    new_rect_to_par_label.next_to(new_rect_to_par_arrow)
    new_rect_to_par_group = VGroup(new_rect_to_par_arrow, new_rect_to_par_label)

    rho_to_par_arrow = square_to_rect_arrow = Arrow(start=DOWN*0.3 + LEFT*2, end=UP*1.2 + LEFT*0.1,
                                                    stroke_width = 3)
    rho_to_par_label = TextMobject("Inherits").scale(0.7)
    rho_to_par_label.next_to(rho_to_par_arrow, LEFT)
    rho_to_par_group = VGroup(rho_to_par_arrow, rho_to_par_label)

    rhombus_class_shape = Polygon(UP*1.25, RIGHT*0.7, DOWN*1.25, LEFT*0.7)
    rhombus_class_shape.rotate(PI/4)
    rhombus_class_shape.set_color(ORANGE)
    rhombus_label = TextMobject("Rhombus").scale(0.5)
    rhombus_label.move_to(rhombus_class_shape.get_center())
    rhombus_class = VGroup(rhombus_class_shape, rhombus_label)
    rhombus_class.move_to(DOWN*1+LEFT*2)

    self.play(square_and_rect_classes.shift, RIGHT*2.5,
              Transform(rect_to_par_group, new_rect_to_par_group),
              Write(rho_to_par_group),
              FadeIn(rhombus_class),
              run_time = 3)

    self.wait()

class RelevantParts(ThreeDScene):
  def construct(self):
    relevant_parts = TextMobject("Write relevant Fields and Methods")
    relevant_parts.move_to(UP*3)
    rectangle = Rectangle()
    rectangle.set_color_by_gradient(BLUE, PURPLE)
    self.play(Write(relevant_parts),
              ShowCreation(rectangle),
              run_time = 5)
    
    self.wait()
    self.play(FadeOut(relevant_parts))
    self.set_camera_orientation(phi=0,gamma=0)
    
    self.move_camera(phi=PI/2, theta=0, run_time = 5, rate_func = there_and_back)
    # self.begin_ambient_camera_rotation(rate=0.1)
    self.wait(3)


class ClassCode(Scene):
  def construct(self):
    class_def = TextMobject("class Rectangle")
    class_def.set_color_by_tex_to_color_map({
            "class": YELLOW,
            "Rectangle": GREEN
        })

    self.play(Write(class_def),
              run_time = 2)
    self.wait()

class WriteClass(Scene):
  def construct(self):
    class_def = TexMobject("class", "\\ Radio:")
    class_def.move_to(UP*3 + LEFT*5)
    class_def.set_color_by_tex_to_color_map({"class" : BLUE, "Radio" : GREEN })
    
    constructor = TexMobject("def", "\\ \\_\\_init\\_\\_", "(", 
                            "self", "," "frequency", ",", "mode", ",", "volume", "):")
    constructor.move_to(UP*2 + LEFT)
    constructor.set_color_by_tex_to_color_map(
      {"def" : BLUE,
      "\\ \\_\\_init\\_\\_" : "#edeeaa",
      "self" : BLUE_C,
      "frequency" : BLUE_C,
      "mode" : BLUE_C,
      "volume" : BLUE_C,
      })

    freq =  TexMobject("self", ".frequency = frequency")
    freq.move_to(UP + LEFT*1.5)
    freq.set_color_by_tex_to_color_map({"self" : BLUE})
    mode =  TexMobject("self", ".mode = mode")
    mode.move_to(LEFT*2.6)
    mode.set_color_by_tex_to_color_map({"self" : BLUE})
    volume =  TexMobject("self", ".volume = volume")
    volume.move_to(DOWN + LEFT*2.1)
    volume.set_color_by_tex_to_color_map({"self" : BLUE})
    
    lines = [class_def, constructor, freq, mode, volume]

    for line in lines:
      self.play(Write(line),
                run_time = 2)
      self.wait()

    self.wait()