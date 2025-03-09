from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        Window.size = (300, 500)
        self.icon = 'calculator.png'
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation='vertical')
        self.solution = TextInput(
            multiline=False, readonly=True, halign='right', font_size=55
        )
        
        main_layout.add_widget(self.solution)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
            ['=']
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
            
        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == 'C':
            # Очистить виджет решения
            self.solution.text = ''
        elif button_text == '=':
            # Вычислить результат
            try:
                solution = str(eval(current))
                self.solution.text = solution
            except Exception:
                self.solution.text = 'Ошибка'
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Не добавляем два оператора подряд
                return
            elif current == '' and button_text in self.operators:
                # Первая кнопка не может быть оператором
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
            self.last_was_operator = button_text in self.operators
            self.last_button = button_text
            
if __name__ == '__main__':
    CalculatorApp().run()
