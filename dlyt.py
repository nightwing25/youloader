from kivymd.app import MDApp
#from kivymd.uix.button 
from kivy.lang import Builder 
from pytube import YouTube
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty
import webbrowser
import kivy
from kivy.app import App

#from kivymd.uix.screen import MDScreenManager,MDscreen

"""
https://www.geeksforgeeks.org/download-instagram-reel-using-python/
for instagram downloader 
"""

"""
*created by:D.wolf
*simple youtube downlowder
"""



kv = "DL.kv"
class ContentNav(MDScrollView):
    screen_manager = ObjectProperty()
    nav = ObjectProperty()


class Test(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file(kv)
    def build(self):
        self.theme_cls.primary_pallete = "Pink"
        self.theme_cls.theme_style = "Dark"

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

    def github(self):
        webbrowser.open("https://github.com/nightwing25")

    

if __name__=="__main__":
    Test().run()




