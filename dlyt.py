from kivymd.app import MDApp
#from kivymd.uix.button 
from kivy.lang import Builder 
from pytubefix import YouTube
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty
import webbrowser
import kivy
from kivymd.uix.screen import MDScreen
#do loading of kv file here to avoid root error
#https://pictogrammers.com/library/mdi/
#relearn multithreading or async so the download can be quick
"""
Note: putting things in <is a rule>: meaning dont display it to the app yet just desiging what goes inside it
until you call it with its name with out the <>
TASK:
~ CREATE A BUTTON TO SWITCH FROM AUDIO TO VIDEO FORMAT 
~ CREATE SNACKBAR TO TELL WHEN FILE FINISHES TO DOWNLOad
~ TEST
"""

KV = """
#MENU SECTION
<MDTopAppBar>:
    type: "small"
    pos_hint: {"center_x": .5, "center_y": .95}

    MDTopAppBarLeadingButtonContainer:

        MDActionTopAppBarButton:
            icon: "menu"                    
            on_release: app.open_nav()#get logic to grab id in navigation class



    MDTopAppBarTitle:
        text: "DOWNLOADER"
        halign: "center"

    MDTopAppBarTrailingButtonContainer:

        #MDActionTopAppBarButton:
           # icon: "download"
            #on_release: app.download_mp3()
            #download function for button go here
#MAIN 
Downloader:
    md_bg_color: self.theme_cls.backgroundColor
    MDTopAppBar:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen: #all contents go here
            
                #MDButton: make the download button outside right of text field
                #    pos_hint:{"center_x":.2}
                MDTextField:
                    id:linker
                    #mode: "filled"
                    size_hint_x:None
                    width:"240dp"
                    pos_hint:{"center_x":.5,"center_y":.5}
                    on_text_validate:app.download_mp3(linker.text)
                    

                    MDTextFieldHintText:
                        text: "https://youtu.be/UEO0alk23kick"

                    MDTextFieldHelperText:
                        text: "Type link here"
                        mode: "persistent"

                    #MDTextFieldTrailingIcon:
                    #    icon: "download"


        MDNavigationDrawer:
            id: nav_drawer
            radius: 0, dp(16), dp(16), 0

            MDNavigationDrawerMenu:

                MDNavigationDrawerLabel:
                    text: "Menu"

                MDNavigationDrawerItem:
                    MDButton:
                        pos_hint:{"center_y":.5}
                        on_release:app.instagram()
                        
                        MDButtonIcon:
                            icon:"instagram"

                    MDNavigationDrawerItemText:
                        text: "instagram"

                    
                MDNavigationDrawerDivider:


                MDNavigationDrawerItem:
                    MDButton:
                        pos_hint:{"center_y":.5}
                        on_release:app.twitter()
                        
                        MDButtonIcon:
                            icon:"twitter"

                    MDNavigationDrawerItemText:
                        text: "twitter"

                    
                MDNavigationDrawerDivider:

                MDNavigationDrawerItem:
                    
                    MDButton:
                        pos_hint:{"center_y":.5}
                        on_release:app.github()
                        
                        MDButtonIcon:
                            icon:"github"
                    

                    MDNavigationDrawerItemText:
                        text: "github"
                    
                MDNavigationDrawerDivider:

                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "cash"

                    MDNavigationDrawerItemText:
                        text: "support me ->$dwolf94"

                    
                MDNavigationDrawerDivider:
                    MDNavigationDrawerItem:
"""


class Downloader(MDScreen):
    ...

class DownerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete:"Orange"
        return Builder.load_string(KV)
    def open_nav(self):
        self.root.ids.nav_drawer.set_state("toggle")

    def download_mp3(self,link):
        try:
            yt = YouTube(link)
            audio = yt.streams.get_audio_only().download()
        except Exception as e:
            print(e)

    #SOCIAL SECTION------------------------------------------------
    def instagram(self):
       webbrowser.open("https://www.instagram.com/d.wolf_/")

    def twitter(self):
       webbrowser.open("x.com/D_W01F")

    def github(self):
        webbrowser.open("https://github.com/nightwing25")

    def threads(self):
        pass #add threads link

    def support_me(self):
       ...
    #def trouble_shoot(self):
    #    print(self.root.ids)

if __name__ == "__main__":
    DownerApp().run()
