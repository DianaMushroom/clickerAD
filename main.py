from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

global n
n = 0
Window.size = (360,640)
Window.clearcolor = (255,255,255,0)
Window.title = ('Clicker')

class MyApp(App):
  global n 
  def __init__(self):
    super().__init__()
    self.nt = Label(text='Clicker',color = (0,0,0,1), font_size=45, font_name='Roboto-Bold.ttf')
    self.button = Button(background_color=(230/255,230/255,255/255,1), size_hint=(None, None), size=(200, 100), pos_hint={'center_x': 0.5})
    self.score = Label(text=f'Вы заработали {n} баллов', color = (0,0,0,1))

  def build(self):
    self.button.bind(on_press = self.action1, on_release=self.action2)
    box = BoxLayout(orientation='vertical')
    box.add_widget(self.nt)
    box.add_widget(self.button)
    box.add_widget(self.score)
    return(box)

  def action1(self,obj):
    self.button.background_color = (115/255,115/255,117/255,1)
  def action2(self,obj):
    global n
    n += 1
    strn = str(n)
    element = strn[len(strn)-1]
    if element in ['0', '5', '6', '7', '8', '9']:
      self.score.text = f'Вы заработали {n} баллов'
    elif element in ['2','3','4']:
      self.score.text = f'Вы заработали {n} балла'
    else:
      self.score.text = f'Вы заработали {n} балл'
    self.button.background_color = (230/255,230/255,255/255,1)
if __name__ == '__main__':
  MyApp().run()
    
    