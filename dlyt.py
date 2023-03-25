
from kivymd.app import MDApp
#from kivymd.uix.button 
from kivy.lang import Builder 


"""
^create a textfield in the middle next to the texfield put icon button for the choose path function
^download video or audio to dl folder by default 

"""

kv = """
MDScreen:

    MDLabel:
        text:"Youtube Downloader"
        halign:"center"
        font_style:"H3"
        pos_hint:{"center_x":.5,"center_y":.75}

        
    MDTextField:
        id:link
        hint_text:"your link"
        helper_text:"e.g:https://youtu.be/IGD547Bnjf"
        pos_hint: {"center_x":.5,"center_y":.5}
        size_hint_x: .5

    MDFloatingActionButton:
        icon:"folder"
        md_bg_color:app.theme_cls.primary_color
        pos_hint:{"center_x":.79,"center_y":.5}

    MDRaisedButton:
        id:audio
        text:"mp3 format"
        pos_hint:{"center_x":.3,"center_y":.4}

    MDRaisedButton:
        id:video
        text:"mp4 format"
        pos_hint:{"center_x":.69,"center_y":.4}




"""


class Test(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(kv)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "Pink"

        return self.screen

    def audio_func(self):
        pass #mp3 dowmnload

    def video_func():
        pass #mp4 function


        
Test().run()


