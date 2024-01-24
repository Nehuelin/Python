from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.clock import Clock

def calculate_dps(damage_per_hit=None, attack_rate=None, damage_per_second=None):
    if damage_per_hit is not None and attack_rate is not None:
        dps = damage_per_hit / attack_rate
        return dps
    elif damage_per_hit is not None and damage_per_second is not None:
        attack_rate = damage_per_second / damage_per_hit
        return attack_rate
    elif attack_rate is not None and damage_per_second is not None:
        damage_per_hit = attack_rate * damage_per_second  
        return damage_per_hit
    else:
        return

class DPS_CalculatorApp(App):
    def build(self):
        self.title = "Calculadora de Daño POGGIES"
        self.layout = BoxLayout(orientation='vertical', padding=10)
        
        self.label_variation = Label(text="ELEGIR TIPO DE OPERACION")
        self.layout.add_widget(self.label_variation)

        self.spinner = Spinner(text="v v v LISTA DE OPERACIONES v v v", values=("1. Daño por Golpe y Velocidad de Ataque a DPS",
                                                                "2. Daño por Golpe y DPS a Velocidad de Ataque",
                                                                "3. Velocidad de Ataque y DPS a Daño por Golpe"))
        self.layout.add_widget(self.spinner)

        self.label_result = Label(text="Resultado:")
        self.layout.add_widget(self.label_result)

        self.text_input1 = TextInput(multiline=False, hint_text="Valor 1")
        self.layout.add_widget(self.text_input1)

        self.text_input2 = TextInput(multiline=False, hint_text="Valor 2")
        self.layout.add_widget(self.text_input2)

        self.calculate_button = Button(text="!!! CALCULAR !!!", on_press=self.calculate)
        self.layout.add_widget(self.calculate_button)

        self.copy_notice = Label(text="© Nehuel Adolfo Marcos", font_size=12, halign='center')
        self.layout.add_widget(self.copy_notice)

        self.spinner.bind(on_text=self.update_input_hints)
        Clock.schedule_interval(self.update_input_hints, 0.1)  # Update every 0.1 seconds

        # Initialize prev_variation attribute
        self.prev_variation = ""

        return self.layout

    def update_input_hints(self, dt):
        variation = self.spinner.text.split(".")[0].strip()

        if variation != self.prev_variation:
            self.text_input1.text = ""
            self.text_input2.text = ""

        if variation == "1":
            self.text_input1.hint_text = "Ingresar Daño por Golpe"
            self.text_input2.hint_text = "Ingresar Velocidad de Ataque (En Segundos)"
        elif variation == "2":
            self.text_input1.hint_text = "Ingresar Daño por Golpe"
            self.text_input2.hint_text = "Ingresar Daño por Segundo"
        elif variation == "3":
            self.text_input1.hint_text = "Ingresar Velocidad de Ataque (En Segundos)"
            self.text_input2.hint_text = "Ingresar Daño por Segundo"

        self.prev_variation = variation

    def calculate(self, instance):
        try:
            variation = self.spinner.text.split(".")[0].strip()
            value1 = float(self.text_input1.text)
            value2 = float(self.text_input2.text)

            if variation == "1":
                result = calculate_dps(damage_per_hit=value1, attack_rate=value2)
            elif variation == "2":
                result = calculate_dps(damage_per_hit=value1, damage_per_second=value2)
            elif variation == "3":
                result = calculate_dps(attack_rate=value1, damage_per_second=value2)
            else:
                result = "OPERACION INVALIDA"

            self.label_result.text = f"Resultado: {result}"
        except ValueError:
            self.label_result.text = "Datos Invalidos. Ingresar valores numericos."

if __name__ == "__main__":
    DPS_CalculatorApp().run()
    
    