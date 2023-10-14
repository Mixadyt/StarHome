import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        # Создаем контейнер вертикального расположения
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Создаем кнопку и добавляем действие по щелчку
        button = Button(text='Нажми меня!')
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)

        # Создаем метку для отображения текста
        self.label = Label(text='Текст')
        layout.add_widget(self.label)

        return layout

    def on_button_press(self, instance):
        self.label.text = 'Кнопка нажата!'


if __name__ == '__main__':
    MyApp().run()
