from kivymd.app import MDApp
#from kivymd.uix.button 
from kivy.lang import Builder 
from pytube import YouTube



"""
*created by:D.wolf
*simple youtube downlowder
"""

kv = """
MDScreen:

    MDLabel:
        id:label_text
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
        on_press:app.audio_func()


    MDRaisedButton:
        id:video
        text:"mp4 format"
        pos_hint:{"center_x":.69,"center_y":.4}
        on_press:app.video_func()




"""


class Test(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(kv)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "Pink"

        return self.screen

    def audio_func(self,*args):
        #mp3 func
        try:
            links = self.screen.ids.link.text
            yt = YouTube(links)
            audio = yt.streams.get_audio_only().download()
        except Exception as e:
            print(f"the problem could be {e}")
        print("done")

    def video_func(self,*args):
        #mp4 function
        try:
            links = self.screen.ids.link.text
            utube = YouTube(links)
            utube = utube.streams.get_highest_resolution().download()
        except Exception as e:
            print(f"the problem is {e}")
        print("finished")

    def res(self):
        print()


if __name__=="__main__":
    Test().run()


