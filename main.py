from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout


def parse_number(text):
    return float(text.replace(",", "."))


class AleLaskuri(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=40, spacing=30, **kwargs)

        self.otsikko = Label(text="ALELASKURI", font_size=140, bold=True)

        input_row = BoxLayout(orientation="horizontal", spacing=25)

        self.prosentti_input = TextInput(font_size=100, hint_text="%", multiline=False)
        self.hinta_input = TextInput(font_size=100, hint_text="€", multiline=False)

        input_row.add_widget(self.prosentti_input)
        input_row.add_widget(self.hinta_input)

        self.nappi = Button(text="LASKE", font_size=110, size_hint=(0.6, None), height=160)
        self.nappi.bind(on_press=self.laske)

        nappi_row = AnchorLayout(anchor_x="center")
        nappi_row.add_widget(self.nappi)

        self.tulos = Label(text="", font_size=200, bold=True)

        self.add_widget(self.otsikko)
        self.add_widget(input_row)
        self.add_widget(nappi_row)
        self.add_widget(self.tulos)

    def laske(self, instance):
        try:
            p = parse_number(self.prosentti_input.text)
            h = parse_number(self.hinta_input.text)

            uusi = h - (h * p / 100)

            self.tulos.text = f"{uusi:.2f} €"
            self.nappi.text = f"-{int(p)}%"
        except:
            self.tulos.text = "—"


class AleApp(App):
    def build(self):
        return AleLaskuri()


if __name__ == "__main__":
    AleApp().run()
