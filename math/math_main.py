from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
import math

Window.clearcolor = (.87, 0.34, 0.3, 0.3)
btn_color = (0.98, 0.31, 0.8, 1)

class Container(BoxLayout):
    pass

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        self.btn_1 = Button(text="Арифметическая \n      прогрессия", size_hint=(0.7, 0.3), pos_hint=({'center_x': 0.5}), font_size=13, on_press = self.math_1)
        self.btn_1.background_color = btn_color
        self.btn_2 = Button(text="Геометрическая \n      прогрессия", size_hint=(0.7, 0.3), pos_hint=({'center_x': 0.5}), font_size=13, on_press = self.math_2)
        self.btn_2.background_color = btn_color
        bl.add_widget( Label(text="Добро пожаловать", font_size=20) )
        bl.add_widget(self.btn_1)
        bl.add_widget(self.btn_2)
        self.add_widget(bl)
    def math_1(self, *args):
        self.manager.current = 'arithmetic_menu'
        self.manager.transition.direction = 'left'
    def math_2(self, *args):
        self.manager.current = 'geometric_menu'
        self.manager.transition.direction = 'right'

class ArithmeticMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        bl.add_widget(Button(text="Найти a1", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_a1))
        bl.add_widget(Button(text="Найти d", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_d))
        bl.add_widget(Button(text="Найти n", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_n))
        bl.add_widget(Button(text="Найти an", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_an))
        bl.add_widget(Button(text="Найти Sn", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_Sn))
        self.add_widget(bl)
    def find_an(self, *args):
        self.manager.current = 'find_an'
        self.manager.transition.direction = 'right'
    def find_a1(self, *args):
        self.manager.current = 'find_a1'
        self.manager.transition.direction = 'right'
    def find_d(self, *args):
        self.manager.current = 'find_d'
        self.manager.transition.direction = 'right'
    def find_n(self, *args):
        self.manager.current = 'find_n'
        self.manager.transition.direction = 'right'
    def find_Sn(self, *args):
        self.manager.current = 'find_Sn'
        self.manager.transition.direction = 'right'

class GeometricMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        bl.add_widget(Button(text="Найти b1", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_b1))
        bl.add_widget(Button(text="Найти q", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_q))
        bl.add_widget(Button(text="Найти n", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_b_n))
        bl.add_widget(Button(text="Найти bn", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_bn))
        bl.add_widget(Button(text="Найти Sn", size_hint=(0.7, 0.4), pos_hint={'center_x': 0.5}, on_press = self.find_bSn))
        self.add_widget(bl)
    def find_b1(self, *args):
        self.manager.current = 'find_b1'
        self.manager.transition.direction = 'right'
    def find_bn(self, *args):
        self.manager.current = 'find_bn'
        self.manager.transition.direction = 'right'
    def find_q(self, *args):
        self.manager.current = 'find_q'
        self.manager.transition.direction = 'right'
    def find_b_n(self, *args):
        self.manager.current = 'find_b_n'
        self.manager.transition.direction = 'right'
    def find_bSn(self, *args):
        self.manager.current = 'find_bSn'
        self.manager.transition.direction = 'right'

class Find_an(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти an", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите a1") )
        self.a1 = Label(text="0")
        gl.add_widget( self.a1 )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите d") )
        self.d = Label(text="0")
        gl.add_widget( self.d )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите n") )
        self.n = Label(text="0")
        gl.add_widget( self.n )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18, pos_hint={'center_x': 0.5}) )
        self.fin = Label(text="0", font_size=18, pos_hint={'center_x': 0.5})
        result.add_widget( self.fin )
        # result.add_widget( Button(text="Назад", font_size=15, size_hint=(0.6, 1), on_press = self.back) )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'right'
    
    def update_label(self):
        if self.input_id == 1:
            self.a1.text = self.formula
        elif self.input_id == 2:
            self.d.text = self.formula
        else:
            self.n.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.total = str(float(self.a1.text) + (float(self.n.text) - 1) * float(self.d.text))
        self.fin.text = self.total
        print(self.total)

class Find_Sn(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти Sn", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите a1") )
        self.a1 = Label(text="0")
        gl.add_widget( self.a1 )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите d") )
        self.d = Label(text="0")
        gl.add_widget( self.d )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите n") )
        self.n = Label(text="0")
        gl.add_widget( self.n )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18, pos_hint={'center_x': 0.5}) )
        self.fin = Label(text="0", font_size=18, pos_hint={'center_x': 0.5})
        result.add_widget( self.fin )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'right'
    
    def update_label(self):
        if self.input_id == 1:
            self.a1.text = self.formula
        elif self.input_id == 2:
            self.d.text = self.formula
        else:
            self.n.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.total_1 = float(self.a1.text) * 2 + (float(self.n.text) - 1) * float(self.d.text)
        self.total_2 = float(self.total_1) * float(self.n.text)
        self.total = str(float(self.total_2) / 2)
        self.fin.text = self.total
        print(self.total)

class Find_a1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти a1", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите an") )
        self.an = Label(text="0")
        gl.add_widget( self.an )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите d") )
        self.d = Label(text="0")
        gl.add_widget( self.d )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите n") )
        self.n = Label(text="0")
        gl.add_widget( self.n )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18, pos_hint={'center_x': 0.5}) )
        self.fin = Label(text="0", font_size=18, pos_hint={'center_x': 0.5})
        result.add_widget( self.fin )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'right'
    
    def update_label(self):
        if self.input_id == 1:
            self.an.text = self.formula
        elif self.input_id == 2:
            self.d.text = self.formula
        else:
            self.n.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.total = str(float(self.an.text) - float(self.d.text) * (float(self.n.text) - 1))
        self.fin.text = self.total
        print(self.total)

class Find_n(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти n", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите an") )
        self.an = Label(text="0")
        gl.add_widget( self.an )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите d") )
        self.d = Label(text="0")
        gl.add_widget( self.d )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите a1") )
        self.a1 = Label(text="0")
        gl.add_widget( self.a1 )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18, pos_hint={'center_x': 0.5}) )
        self.fin = Label(text="0", font_size=18, pos_hint={'center_x': 0.5})
        result.add_widget( self.fin )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'right'
    
    def update_label(self):
        if self.input_id == 1:
            self.an.text = self.formula
        elif self.input_id == 2:
            self.d.text = self.formula
        else:
            self.a1.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.total = str(((float(self.an.text) - float(self.a1.text)) / float(self.d.text) + 1))
        self.fin.text = self.total
        print(self.total)

class Find_d(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти d", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите an") )
        self.an = Label(text="0")
        gl.add_widget( self.an )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите n") )
        self.n = Label(text="0")
        gl.add_widget( self.n )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите a1") )
        self.a1 = Label(text="0")
        gl.add_widget( self.a1 )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18, pos_hint={'center_x': 0.5}) )
        self.fin = Label(text="0", font_size=18, pos_hint={'center_x': 0.5})
        result.add_widget( self.fin )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'right'
    
    def update_label(self):
        if self.input_id == 1:
            self.an.text = self.formula
        elif self.input_id == 2:
            self.n.text = self.formula
        else:
            self.a1.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.total = str((float(self.an.text) - float(self.a1.text)) / (float(self.n.text) - 1))
        self.fin.text = self.total
        print(self.total)

class Find_bn(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти bn", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите b1") )
        self.b1 = Label(text="0")
        gl.add_widget( self.b1 )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите q") )
        self.q = Label(text="0")
        gl.add_widget( self.q )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите n") )
        self.n = Label(text="0")
        gl.add_widget( self.n )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18) )
        self.fin = Label(text="0", font_size=18)
        result.add_widget( self.fin )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'left'
    def update_label(self):
        if self.input_id == 1:
            self.b1.text = self.formula
        elif self.input_id == 2:
            self.q.text = self.formula
        else:
            self.n.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.extent = float(self.q.text) ** (float(self.n.text) - 1)
        self.total = str(float(self.b1.text) * self.extent)
        self.fin.text = self.total
        print(self.total)

class Find_b1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти b1", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите bn") )
        self.bn = Label(text="0")
        gl.add_widget( self.bn )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите q") )
        self.q = Label(text="0")
        gl.add_widget( self.q )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите n") )
        self.n = Label(text="0")
        gl.add_widget( self.n )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18) )
        self.fin = Label(text="0", font_size=18)
        result.add_widget( self.fin )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'left'
    def update_label(self):
        if self.input_id == 1:
            self.bn.text = self.formula
        elif self.input_id == 2:
            self.q.text = self.formula
        else:
            self.n.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.extent = float(self.q.text) ** (float(self.n.text) - 1)
        self.total = str(float(self.bn.text) / self.extent)
        self.fin.text = self.total
        print(self.total)

class Find_bSn(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти Sn", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите b1") )
        self.b1 = Label(text="0")
        gl.add_widget( self.b1 )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите q") )
        self.q = Label(text="0")
        gl.add_widget( self.q )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите n") )
        self.n = Label(text="0")
        gl.add_widget( self.n )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18) )
        self.fin = Label(text="0", font_size=18)
        result.add_widget( self.fin )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'left'
    def update_label(self):
        if self.input_id == 1:
            self.b1.text = self.formula
        elif self.input_id == 2:
            self.q.text = self.formula
        else:
            self.n.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.extent = float(self.q.text) ** float(self.n.text)
        self.total_1 = 1 - self.extent
        self.total_2 = float(self.b1.text) * self.total_1
        self.total_3 = 1 - int(self.q.text)
        self.total = str(self.total_2 / self.total_3)
        self.fin.text = self.total
        print(self.total)

class Find_q(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти q", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите b1") )
        self.b1 = Label(text="0")
        gl.add_widget( self.b1 )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите bn") )
        self.bn = Label(text="0")
        gl.add_widget( self.bn )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите n") )
        self.n = Label(text="0")
        gl.add_widget( self.n )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18) )
        self.fin = Label(text="0", font_size=18)
        result.add_widget( self.fin )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'left'
    def update_label(self):
        if self.input_id == 1:
            self.b1.text = self.formula
        elif self.input_id == 2:
            self.bn.text = self.formula
        else:
            self.n.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.total = str((float(self.bn.text) / float(self.b1.text)) ** (1/(float(self.n.text) - 1)))
        self.fin.text = self.total
        print(self.total)

class Find_b_n(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = "0"
        self.input_id = 0
        self.formula = ""
        
        bl = BoxLayout(orientation = 'vertical', padding=25, spacing=3)
        
        lbl1 = Label(text="Найти n", size_hint=(1, .1), font_size=25)
        
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .2))
        gl.add_widget( Label(text="Введите b1") )
        self.b1 = Label(text="0")
        gl.add_widget( self.b1 )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input1) )

        gl.add_widget( Label(text="Введите bn") )
        self.bn = Label(text="0")
        gl.add_widget( self.bn )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input2) )

        gl.add_widget( Label(text="Введите q") )
        self.q = Label(text="0")
        gl.add_widget( self.q )
        gl.add_widget( Button(text="+", size_hint=(0.4, 0.4), on_press = self.input3) )

        cl = GridLayout(cols=3, padding=30, size_hint=(1, .6))
        cl.add_widget( Button(text="7", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="8", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="9", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="4", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="5", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="6", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="1", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="2", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="3", size_hint=(0.2, 0.2), on_press = self.add_number) )

        cl.add_widget( Button(text="-", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text="0", size_hint=(0.2, 0.2), on_press = self.add_number) )
        cl.add_widget( Button(text=".", size_hint=(0.2, 0.2), on_press = self.add_number) )
        btn = Button(text='Начать', size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.result)
        btn.background_color = btn_color
        result = GridLayout(cols=1, padding=25, size_hint=(1, .1))
        # result.add_widget( Label(text="Итого:", font_size=18) )
        self.fin = Label(text="0", font_size=18)
        result.add_widget( self.fin )
        bl.add_widget(lbl1)
        bl.add_widget(gl)
        bl.add_widget(cl)
        bl.add_widget(btn)
        bl.add_widget(result)
        bl.add_widget( Button(text="Назад", font_size=15, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5}, on_press = self.back) )
        self.add_widget(bl)
    def back(self, *args):
        self.manager.current = 'main_menu'
        self.manager.transition.direction = 'left'
    def update_label(self):
        if self.input_id == 1:
            self.b1.text = self.formula
        elif self.input_id == 2:
            self.bn.text = self.formula
        else:
            self.q.text = self.formula

    def add_number(self, instance):
        
        self.formula += str(instance.text)
        self.update_label()

    def input1(self, instance):
        self.formula = ""
        self.input_id = 1

    def input2(self, instance):
        self.formula = ""
        self.input_id = 2

    def input3(self, instance):
        self.formula = ""
        self.input_id = 3

    def result(self, instance):
        self.total_1 = float(self.bn.text) / float(self.b1.text)
        self.total_2 = math.log(self.total_1, float(self.q.text))
        self.total_3 = self.total_2 + 1
        self.total = str(self.total_3)
        self.fin.text = self.total
        print(self.total)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(ArithmeticMenu(name='arithmetic_menu'))
        sm.add_widget(GeometricMenu(name='geometric_menu'))
        sm.add_widget(Find_an(name='find_an'))
        sm.add_widget(Find_Sn(name='find_Sn'))
        sm.add_widget(Find_a1(name='find_a1'))
        sm.add_widget(Find_n(name='find_n'))
        sm.add_widget(Find_d(name='find_d'))
        sm.add_widget(Find_bn(name='find_bn'))
        sm.add_widget(Find_b1(name='find_b1'))
        sm.add_widget(Find_bSn(name='find_bSn'))
        sm.add_widget(Find_q(name='find_q'))
        sm.add_widget(Find_b_n(name='find_b_n'))
        return sm
        return Container()
app = MyApp()
app.run()

print('Привет Айдемир!')
print('Здравствуйте Владислав!')