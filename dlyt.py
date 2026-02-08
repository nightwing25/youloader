from kivymd.app import MDApp
#from kivymd.uix.button import MDButton
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
~ CREATE SNACKBAR TO TELL WHEN FILE FINISHES TO DOWNLOAD
~ TEST
~ ADD WORKS TO THE VIDEO FUNCTION BY USING THE VIDEO CHIP TO DOWNLOAD
~ GIVE INFO DURING DOWNLOADS UNDER THE CHIPS 
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

<CommonLabel@MDLabel>
    adaptive_size: True
    theme_text_color: "Custom"
    #text_color: "#e6e9df"


<CommonAssistChip@MDChip>
    # Custom attribute.
    text: ""
    icon: ""

    # Chip attribute.
    type: "assist"
    theme_bg_color: "Custom"
    md_bg_color: "#2a3127"
    theme_line_color: "Custom"
    line_color: "grey"
    theme_elevation_level: "Custom"
    elevation_level: 1
    theme_shadow_softness: "Custom"
    shadow_softness: 2

    MDChipLeadingIcon:
        icon: root.icon
        #theme_text_color: "Custom"
        #text_color: "#68896c"
        #text_color: "#363636"

    MDChipText:
        text: root.text
        #theme_text_color: "Custom"
        #text_color: "#e6e9df"
        #text_color: "#363636"
#MAIN 
Downloader:
    md_bg_color: self.theme_cls.backgroundColor
    MDTopAppBar:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen: #all contents go here
            
                MDTextField:
                    id:linker
                    #mode: "filled"
                    size_hint_x:None
                    width:"240dp"
                    pos_hint:{"center_x":.5,"center_y":.5}
                    #on_text_validate:app.download_mp3(linker.text)
                    

                    MDTextFieldHintText:
                        text: "https://youtu.be/UEO0alk23kick"

                    MDTextFieldHelperText:
                        text: "Type link here"
                        mode: "persistent"

                    #MDTextFieldTrailingIcon:
                    #    icon: "download"

                MDBoxLayout:
                    adaptive_size: True
                    pos_hint: {"center_x": .5,"center_y":.4}
                    spacing: "12dp"
                    padding: 0, "24dp", 0, 0

                    CommonAssistChip:
                        text: "audio-only"
                        icon: "music"
                        on_press:app.download_mp3(linker.text)


                    CommonAssistChip:
                        text: "video+audio"
                        icon: "video-box"
                        on_press:app.video_download(linker.text)

                MDLabel:
                    id:process
                    text: ""
                    halign: "center"
                    pos_hint: {"center_x": .5,"center_y":.3}
                    


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

                    
                #MDNavigationDrawerDivider:
                 #   MDNavigationDrawerItem:
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
        self.root.ids.process.text = ""
        try:
            yt = YouTube(link,on_complete_callback=self.audio_completed)
            audio = yt.streams.get_audio_only().download()
            self.root.ids.process.text = ""
            self.root.ids.process.text = "Downloading audio file"
        except Exception as e:
            print(e)
            self.root.ids.process.text = str(e)

    def audio_completed(self):
        self.root.ids.process = ""
        self.root.ids.process = "audio downloaded"

    def video_download(self,link):
        try:
            yt = YouTube(link,on_complete_callback=self.video_completed)
            video = yt.streams.get_highest_resolution().download()
            self.root.ids.process.text = ""
            self.root.ids.process.text = "Downloading video file"
        except Exception as e:
            print(e)
            print(self.root.ids)
            self.root.ids.process.text = str(e)
    def video_completed(self,stream,file_path):
        self.root.ids.process.text = ''
        self.root.ids.process.text = 'video downloaded'
            


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
