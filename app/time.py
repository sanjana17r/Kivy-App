import kivy
from kivy.clock import Clock
import mysql.connector
import webbrowser
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Label, Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox

conn = mysql.connector.connect(
   user='root', password='rachiniki2014', host='localhost', database='books')



class P(FloatLayout):
    def done(self):
        P.done.k = int(self.nom.text)
        P.done.l = int(self.nom1.text)

    def sho():
        P.sho.h = P.done.k
        P.sho.m = P.done.l



class Choose(Screen):

    def show_popup(self):
        show = P()
        popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))
        popupWindow.open()       


def on_enter(value):
    print('User pressed enter in', value,value.text)
    k = str(value)
    k = k.split()
    k = k[3][:-1]
    id = k[:]
    cursor = conn.cursor()
    sql = '''insert into books.altt (task,start)  values(%s,%s); '''

    cursor.execute(sql,(value.text,'yes'))
    conn.commit()

#########All the days ################




class day1(Screen):

    def clr(self):
        sql = ''' TRUNCATE TABLE books.altt; '''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    global sql
    sql = '''select task from books.altt where number = (%s); '''

    
    def aff(self):
        try:
            P.sho()
            s = P.sho.h
            e = P.sho.m
        except:
            s = 9
            e = 23       
        i = 1 
        for w in range(s,e+1):
            label = Label(text = str(w))
            self.ids.grid.add_widget(label)

            cursor = conn.cursor()
            cursor.execute(sql,(i,))
            ka = str(cursor.fetchall())[3:-4]
            conn.commit()


            text = TextInput(multiline = False,text = ka)
            #text.id = 'line'
            #print(text.text)
            text.bind(on_text_validate=on_enter)
            self.ids.grid.add_widget(text)
            i+=1

            self.active = CheckBox(active = False) 
            self.ids.grid.add_widget(self.active) 

        
       
class day2(day1):
    
    pass
class day3(day1):
    pass
class day4(day1):
    pass
class day5(day1):
    pass
class day6(day1):
    pass
class day7(day1):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("ttable.kv")
class MyApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()