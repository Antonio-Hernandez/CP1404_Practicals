from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class ListNames(App):
    status_name = StringProperty()

    def build(self):
        self.title = 'Dynamic Widgets Names'
        self.root = Builder.load_file('list_names.kv')
        self.create_widgets()
        return self.root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Antonio', 'Toni', 'AJ', 'Jose']

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            # temp_label.bind(on_release=self.press_entry)
            self.root.ids.names_box.add_widget(temp_label)

    # def press_entry(self, instance):
    #     name = instance.text
    #     self.status_name = "This is {}".format(name)


ListNames().run()
