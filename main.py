from cgitb import text
from email.mime import image
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class ConverterApp(MDApp):
    def flip(self):
        if self.state==0:
            self.state=1
            self.toolBar.title="Decimal to Binary"
            self.input.text="Enter a Decimal Number"
            self.converted.text=""
            self.label.text=""
        else:
            self.state=0
            self.toolBar.title="Binary to Decimal"
            self.input.text="Enter a Binary Number"
            self.converted.text=""
            self.label.text=""

        print("working....")
    def convert(self,args):
        if self.state==0:
            val=int(self.input.text,2)
            self.converted.text=str(val)
            self.label.text="In Decimal is:"
        else:
            val=bin(int(self.input.text))[2:]
            self.converted.text=val
            self.label.text="In Binary is:"
        print("converter working...")


    def build(self):
        self.state=0
        self.theme_cls.primary_palette="Teal"
        screen = MDScreen()
        #UI Widgets go here
        self.toolBar=MDToolbar(title="Binary to Decimal")
        self.toolBar.pos_hint={"top":1}
        self.toolBar.right_action_items=[
            ["rotate-3d-variant",lambda x: self.flip()]
        ]
        screen.add_widget(self.toolBar)

        # logo 
        screen.add_widget(Image(
            source="logo.png",
            pos_hint={"center_x":0.5,"center_y":0.7},
            ))


        # collect user input 
        self.input=MDTextField(
            text="Enter Binary Number",
            halign="center",
            size_hint=(0.8,1),
            pos_hint={"center_x":0.5,"center_y":0.45},
            font_size=22,
        )
        screen.add_widget(self.input)


        # labels 
        self.label=MDLabel(
            halign="center",
            pos_hint={"center_x":0.5,"center_y":0.35},
            font_size=22,
            theme_text_color="Secondary"
        )
        self.converted=MDLabel(
            halign="center",
            pos_hint={"center_x":0.5,"center_y":0.30},
            font_size=22,
            theme_text_color="Primary"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)


        # converter button 
        screen.add_widget(MDFillRoundFlatButton(
            text="Convert",
            font_size=17,
            pos_hint={"center_x":0.5,"center_y":0.20},
            on_press=self.convert
        ))
        # add copyright label 
        self.copyrightlabel=MDLabel(
            text="Eaglesoft.com.pk",
            halign="center",
            pos_hint={"center_x":0.5,"center_y":0.10},
            font_size=22,
        )
        screen.add_widget(self.copyrightlabel)

        
        return screen

if __name__ == '__main__':
    ConverterApp().run()