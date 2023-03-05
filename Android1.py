from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar

# tr = Lang("en")
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
                                padding: "10dp"

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
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1


                                #Строка текста с Иконкой bank

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "bank"

                                    MDTextField:
                                        id: interest
                                        name: 'interest'
                                        #hint_text: tr._('Interest')+", %"
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'float'
                                        helper_text_mode: "on_focus"

                                    MDTextField:
                                        id: payment_type
                                        name: 'payment_type'
                                        hint_text: "Payment type"
                                        #text: tr._("annuity")
                                        on_focus: if self.focus: app.menu.open()
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1                                                


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
                                        helper_text: "Massage"
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1


                        Tab:
                            id: tab3
                            icon: 'book'
                            text: "Relations"

                             #наполнение контентом закладки Relations

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
                                        helper_text: "Massage"
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1                                        

                        Tab:
                            id: tab4
                            icon: 'group'
                            text: "Change"  

                            #Наполнение контентом закладки change
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
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                             #дизайн кнопки

                    MDRaisedButton:
                        id: button

                        pos_hint: {"center_x": .5, "center_y": .5}
                        on_release: app.menu.open()   
                        text: "Set theme"
                        #dark light theme
                        on_release: app.switch_theme_style()
                        pos_hint: {"center_x": .5}

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer


'''


# классы бокового навигационного меню

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

# класс закладок сверху

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class MDIconButton():
    pass


class MenuHeader(MDBoxLayout):
    '''An instance of the class that will be added to the menu header.'''


class LenabotApp(MDApp):
    # что то в этой части кода не так, появляется 2 титулки придумать как исправить

    title = "Elena your friend"
    by_who = "By RIFT"
    dialog = None
    lang = StringProperty('en')
    data_tables = None
    current_tab = 'tab1'
    payment_annuity = True
    menu = None  # for recreate menu on lang change

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "A100"
        self.data_for_calc_is_changed = True

        self.screen = Builder.load_string(KV)
        menu_items = [{"icon": "book", "text": "annuity"},
                      {"icon": "group", "text": "differentiated"}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()

        # Clock.schedule once(set item,0.5)

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Light"  # " Dark" #  " Light"
        self.theme_cls.primary_palette = "Blue"
        return self.screen

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Blue" if self.theme_cls.primary_palette == "Orange" else "Orange"
        )
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )

    #  def build(self):
    #  return Builder.load_string(KV)

    def menu_callback(self, text_item):
        print(text_item)

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
            "group": "Change",

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

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Share it:",
                type="custom",
                content_cls=ContentDialogSend(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="SEND", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()


class ContentDialogSend(BoxLayout):
    pass


LenabotApp().run()

# конец бокового меню-----------------------------------------------------------------------------


# кнопка---------------------------------------------------------------------------------------

