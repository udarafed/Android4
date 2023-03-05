from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
#tr = Lang("en")
# from kivy.utils import tr
# кв файл типо cSS

KV = '''
# https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts
# Menu item in the DrawerList list.
#:import tr kivy.utils.get_color_from_hex
# https://github.com/tito/kivy-gettext-example
# this import for multilingual support

<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:

        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [['star-outline', lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: (0, 0, 0, 1)
    
                    MDTabs:
                        id: tabs
                        on_ref_press: app.on_ref_press(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: (0.1, 0.1, 0.1, 1)
    
                        Tab:
                            id: tab1
                            icon: 'chat-question'
                            text: "Quest"
                            
                            #наполнение контентом закладки Quest
                        
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "300dp"
                        
                                BoxLayout:
                                    orientation: 'horizontal'
    
                                    MDIconButton:
                                       # icon: "calendar-month"
                                        icon: "eye-off"
                                         
                                    MDTextField:
                                        hint_text: "Round mode"
                                        mode: "round"
                                        max_text_length: 15
                                        helper_text: "Massage"
                                                                                
                        
                            
                        Tab:
                            id: tab2
                            icon: 'robot-love'
                            text: "Robot"
                            
                            #наполнение закладки Robot
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "300dp"
                        
                                BoxLayout:
                                    orientation: 'horizontal'
    
                                    MDIconButton:
                                       
                                        icon: "clock-time-five-outline"
                                         
                                    MDTextField:
                                        hint_text: "Round mode"
                                        mode: "round"
                                        max_text_length: 15
                                        helper_text: "Massage"
                                       # hint_text: tr._('Months')
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'int'
                                        helper_text_mode: "on_focus"
                            
                            
                        Tab:
                            id: tab3
                            icon: 'book'
                            text: "Relations"
                        Tab:
                            id: tab4
                            icon: 'group'
                            text: "Change"                           


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

'''





#классы бокового навигационного меню

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

# класс закладок сверху

#класс закладок сверху

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MDIconButton():
    pass

class LenabotApp(MDApp):
    title = "Elena your friend"
    by_who = "By RIFT"

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):

        icons_item_menu_lines = {
            "bag-personal": "Bag",
            "account": "Profile",
            "star": "Progress",
            "shopping": "Shop",
            "mower-bag-on": "Help us",
            "shield-sun": "Dark\Light",
            "help": "Help",
        }
        icons_item_menu_tabs = {
            "chat-question": "Quest",
            "robot-love": "Relations",
            "book": "Progress",
            "group":"Change",

        }

        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )

        # To auto generate tabs
#        for icon_name, name_tab in icons_item_menu_tabs.items():
#            self.root.ids.tabs.add_widget(Tab(icon= icon_name,title=f" {name_tab}"))



    # tab_switch #on_tab_switch

    def on_ref_press(
            self,
            instance_tabs,
            instance_tab_label,
            instance_tab,
            instance_tab_bar,
            instance_carousel,
    ):
        '''
        The method will be called when the ``on_ref_press`` event
        occurs when you, for example, use markup text for tabs.

        :param instance_tabs: <kivymd.uix.tab.MDTabs object>
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>
        :param instance_tab: <__main__.Tab object>
        :param instance_tab_bar: <kivymd.uix.tab.MDTabsBar object>
        :param instance_carousel: <kivymd.uix.tab.MDTabsCarousel object>
        '''

    def on_star_click(self):
        pass


LenabotApp().run()

# конец бокового меню-----------------------------------------------------------------------------


# кнопка---------------------------------------------------------------------------------------

