from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase

KV = '''
# Menu item in the DrawerList list.
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

                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)  
                                    
                                

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer      
    

<MyFiles>
    rows: 7

    
    MDLabel:
        text:'Услуги по оценке имущества'
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        text_align: "justify"
        bold: 700
        valign:"top"
        row_height: 40
        
  
    MDLabel:
        text: ' Консалтинговая группа «Апхилл» оказывает услуги по оценке имущества на всей территории РФ. Компания начала оказывать профессиональные услуги экспертизы и оценки недвижимости с 2009 года, а позже расширила спектр услуг, добавив оценку оборудования, бизнеса, ценных бумаг и нематериальных активов. С самого начала основным критерием для отчетов об оценке являлась точная рыночная цена и максимальное качество проведения независимой оценки. '
        pos_hint: {"center_x": .5, "center_y": .5} 
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        halign:"justify"
        padding_x: 20
        adaptive_height: True   
    MDLabel:
        text: 'В крупных городах страны услуги независимого оценщика в Москве или в Санкт-Петербурге всегда востребованы, вне зависимости от состояния экономики и рынка недвижимости в стране. '   
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1      
        halign:"justify"
        padding_x: 20
        adaptive_height: True
    MDLabel:
        text:'Услуги независимой оценки в Москве чаще всего заказывают в случаях:'
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1      
        halign:"justify"
        padding_x: 20
        adaptive_height: True  

    MDLabel:
        text:' - оформления сделок купли-продажи;\\n - передачи имущества в аренду;\\n - оформления имущества в наследство или дарение;\\n - оформления имущества как залога при получении банковского кредита;\\n - приобретения имущества в качестве инвестиции;\\n - решения имущественных споров в суде;\\n - раздела имущества;\\n - оформления страховки.'
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1    
        padding_x: 20
        padding_y: 10 
        adaptive_height: True   
    MDLabel:
        text:'При этом по своему существу любое имущество возможно разбить на несколько типов:'
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1      
        halign:"justify"
        padding_x: 20
        adaptive_height: True  
    
    MDLabel:
        text:' - материальное и нематериальное;\\n - движимое и недвижимое.'
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1    
        padding_x: 20
        padding_y: 10
        adaptive_height: True  
<Shared>
    
    cols: 4 
    rows: 7
    row_force_default: True
    row_default_height: 25
    
    MDLabel:
        text: 'Площадь коммерческой недвижимости'
        size_hint_x: None
        width: 250
        halign:"center"
        border_width: 10
        border_color: [1,0,0,1]
        text_size: 250, 80
        padding_y: 10   
             
    MDLabel:
        size_hint_y: None
        text: 'Стоимость услуг'
        width: 250
        text_size: 250, 80
        padding_y: 30
        row_height: 80
        valign:"center"
        height:80
        
    MDLabel:
        text: 'Оценка арендной ставки'
        size_hint_x: None
        width: 250
        text_size: 250, 80
        padding_y: 10
    MDLabel:
        text: 'Срок оказания услуг'
        width: 250
        text_size: 250, 80
        padding_y: 10
       
       #-------------2
    MDLabel:
        text: 'Hello 3'
        size_hint_x: None
        width: 250
        halign:"center"
        border_width: 10
        border_color: [1,0,0,1]
        
        
    MDLabel:
        text: 'World 3'
        width: 250
        
    MDLabel:
        text: 'Hello 4'
        size_hint_x: None
        width: 250
        halign:"center"
        
    MDLabel:
        text: 'World 3'
        width: 250
        
        
<Starred>
    rows: 13
 
    MDLabel:
        text:'О компании'
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        text_align: "justify"
        bold: 700
        valign:"top"
        row_height: 40

    MDLabel:
        text: 'Консалтинговая группа «Апхилл» — комплексный центр оценки всех видов имущества. '
        pos_hint: {"center_x": .5, "center_y": .5} 
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        halign:"justify"
        padding_x: 20
        adaptive_height: True  
        
    MDLabel:
        text: 'С 2009 года оценщики компании оказывают услуги по определению стоимости недвижимости, в том числе коммерческой, земельных участков, транспортных средств, бизнеса и активов, сервитутов и обременений, а также нематериальных активов. '   
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1      
        halign:"justify"
        padding_x: 20
        adaptive_height: True
    MDLabel:
        text:'Мы не угадываем, а точно знаем формулу безупречного отчета, предлагая нашим клиентам и партнерам оптимальные сроки и стоимость выполнения работы.'
        theme_text_color: "Custom"
        text_color: 0.85, 0.37, 0, 1    
        halign:"justify"
        padding_x: 20
        bold: 700
        adaptive_height: True  
    MDLabel:
        text:'Все процессы в компании точно сформулированы и строго соответствуют законодательству РФ и актуальным стандартам, принятым в отрасли. Качество наших отчетов базируется на квалифицированных расчетах, обоснованных методиках и надлежащей оценке каждого отдельного вида имущества.'
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1      
        halign:"justify"
        padding_x: 20
        adaptive_height: True  
    MDLabel:
        text:'Надежность'
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        text_align: "justify"
        bold: 700
        valign:"top"
        row_height: 40
    MDLabel:
        text:'Нам доверяют лидеры банковского рынка и крупные государственные структуры. В качестве эксперта-оценщика мы рекомендованы не только Арбитражным судом г. Москвы, но и региональными судами различной юрисдикции.'
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1      
        halign:"justify"
        padding_x: 20
        adaptive_height: True  
    
    MDLabel:
        text:' - 97% клиентов, обратившихся к нам, довольны качеством оказанных услуг.\\n Около 70% наших текущих проектов — заказы постоянных корпоративных клиентов и обращения по рекомендациям. \\n В нашем портфеле проекты для более чем 150 российских и зарубежных банков.'
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1    
        padding_x: 20
        padding_y: 10
        adaptive_height: True  
    MDLabel:
        text:'Цель'
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        text_align: "justify"
        bold: 700
        valign:"top"
        row_height: 40
    MDLabel:
        text:'Глобальной целью нашей работы является рост и развитие профессионального рынка оценки в России.'
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1      
        halign:"justify"
        padding_x: 20
        adaptive_height: True 
    MDLabel:
        text:'Ценности'
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        text_align: "justify"
        bold: 700
        valign:"top"
        row_height: 40
    MDLabel:
        text:' - Стабильно высокое качество отчетов при оптимальной цене для клиента.\\n - Компетентность специалистов и богатый управленческий опыт руководителей проектов.\\n - Проактивный подход к бизнес-процессам и внутренней структуре компании.'
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1    
        padding_x: 20
        padding_y: 10
        adaptive_height: True  
    MDLabel:
        text:'Консалтинговая группа «Апхилл» — Ценим бесценное.'
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        text_align: "justify"
        bold: 700
        valign:"top"
        row_height: 40
<Recent>
    
    MDLabel:
        text: 'Недавние'
        pos_hint: {"center_x": .5, "center_y": .5} 
        
<AnotherShared>
    
    MDLabel:
        text: 'Еще одна шара'
        pos_hint: {"center_x": .5, "center_y": .5} 
        
        
'''


class MyLabel(BoxLayout, MDLabel):
    pass


class MyTab(BoxLayout, MDTabsBase):
    pass


class MyFiles(GridLayout, MDTabsBase):
    pass


class Shared(GridLayout, MDTabsBase):
    pass


class Starred(GridLayout, MDTabsBase):
    pass


class Recent(BoxLayout, MDTabsBase):
    pass


class AnotherShared(BoxLayout, MDTabsBase):
    pass


class Tab(MDFloatLayout, MDTabsBase):
    pass


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


class TabMetadata:
    def __init__(self, iconName, title, textContent):
        self.iconName = iconName
        self.title = title
        self.textContent = textContent


class Aphill(MDApp):
    title = "Независимая оценочная компания «Апхилл»"
    by_who = "info@uphill.ru"

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        # Что надо сделать
        # 1. Настройти обображение текста (шрифт, цвет, смещение и т.д.)
        # 2. Отобразить таблицу в одной из вкладок

        #  ------- MENU ----------
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",

        }


        # Это отрисовка меню
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

        #     ------ TABs --------

        # Тут отдельные классы потому что для содержимого каждой табы есть свой объект в разметке
        applicationTabs = [
            # MyTab(icon="folder", title="ANYTHING"),
            MyFiles(icon="folder", title="Услуги"),
            Shared(icon="star", title="Цена"),
            Starred(icon="star", title="О компании"),
            Recent(icon="account-multiple", title="Партнёры и клиенты"),
            AnotherShared(icon="checkbox-marked", title="Контакты")]


        # Это отрисовка таб
        for tab in applicationTabs:
            # tab.add_widget(MyLabel(text="GEGEGEGEG", halign="left"))
            self.root.ids.tabs.add_widget(tab)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        # U can do some stuff for a tab with specific title
        if (instance_tab.title == 'Recent'):
            print("PING")


Aphill().run()
