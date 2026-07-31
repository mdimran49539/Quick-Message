# quick_message_kivymd.py
# Professional Mobile Messaging App - KivyMD Version
# Ready for APK build with Buildozer

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
)
from kivymd.uix.list import (
    MDList,
    OneLineAvatarIconListItem,
    TwoLineAvatarIconListItem,
    ThreeLineAvatarIconListItem,
    IconLeftWidget,
    IconRightWidget,
    OneLineListItem,
)
from kivymd.uix.button import (
    MDFloatingActionButton,
    MDIconButton,
    MDRaisedButton,
    MDFlatButton,
)
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.progressbar import MDProgressBar
from kivymd.toast import toast
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty

# ==================== Language Dictionaries ====================
LANGUAGES = {
    "English": {
        "chats": "Chats",
        "search": "Search",
        "settings": "Settings",
        "theme": "Theme",
        "profile": "Profile",
        "username": "Username",
        "name": "Name",
        "language": "Language",
        "dark": "Dark Mode",
        "light": "Light Mode",
        "logout": "Log Out",
        "new_chat": "New Chat",
        "type_message": "Type a message...",
        "online": "online",
        "last_seen": "last seen recently",
        "calls": "Calls",
        "contacts": "Contacts",
        "saved": "Saved Messages",
        "edit_profile": "Edit Profile",
        "save": "Save",
        "cancel": "Cancel",
        "audio_call": "Audio Call",
        "video_call": "Video Call",
        "menu": "Menu",
        "home": "Home",
        "select_chat": "Select a chat to start messaging",
        "no_messages": "No messages yet",
        "send": "Send",
    },
    "বাংলা": {
        "chats": "চ্যাট",
        "search": "খুঁজুন",
        "settings": "সেটিংস",
        "theme": "থিম",
        "profile": "প্রোফাইল",
        "username": "ইউজারনেম",
        "name": "নাম",
        "language": "ভাষা",
        "dark": "ডার্ক মোড",
        "light": "লাইট মোড",
        "logout": "লগ আউট",
        "new_chat": "নতুন চ্যাট",
        "type_message": "মেসেজ লিখুন...",
        "online": "অনলাইন",
        "last_seen": "সম্প্রতি দেখা গেছে",
        "calls": "কল",
        "contacts": "কন্টাক্টস",
        "saved": "সেভড মেসেজ",
        "edit_profile": "প্রোফাইল এডিট",
        "save": "সেভ",
        "cancel": "বাতিল",
        "audio_call": "অডিও কল",
        "video_call": "ভিডিও কল",
        "menu": "মেনু",
        "home": "হোম",
        "select_chat": "মেসেজ শুরু করতে একটি চ্যাট সিলেক্ট করুন",
        "no_messages": "এখনো কোনো মেসেজ নেই",
        "send": "পাঠান",
    },
    "हिन्दी": {
        "chats": "चैट्स",
        "search": "खोजें",
        "settings": "सेटिंग्स",
        "theme": "थीम",
        "profile": "प्रोफ़ाइल",
        "username": "यूज़रनेम",
        "name": "नाम",
        "language": "भाषा",
        "dark": "डार्क मोड",
        "light": "लाइट मोड",
        "logout": "लॉग आउट",
        "new_chat": "नई चैट",
        "type_message": "संदेश लिखें...",
        "online": "ऑनलाइन",
        "last_seen": "हाल ही में देखा गया",
        "calls": "कॉल्स",
        "contacts": "संपर्क",
        "saved": "सेव्ड मैसेज",
        "edit_profile": "प्रोफ़ाइल संपादित करें",
        "save": "सेव",
        "cancel": "रद्द करें",
        "audio_call": "ऑडियो कॉल",
        "video_call": "वीडियो कॉल",
        "menu": "मेनू",
        "home": "होम",
        "select_chat": "मैसेजिंग शुरू करने के लिए चैट चुनें",
        "no_messages": "अभी कोई संदेश नहीं",
        "send": "भेजें",
    },
    "中文": {
        "chats": "聊天",
        "search": "搜索",
        "settings": "设置",
        "theme": "主题",
        "profile": "个人资料",
        "username": "用户名",
        "name": "姓名",
        "language": "语言",
        "dark": "深色模式",
        "light": "浅色模式",
        "logout": "退出登录",
        "new_chat": "新聊天",
        "type_message": "输入消息...",
        "online": "在线",
        "last_seen": "最近在线",
        "calls": "通话",
        "contacts": "联系人",
        "saved": "收藏的消息",
        "edit_profile": "编辑资料",
        "save": "保存",
        "cancel": "取消",
        "audio_call": "语音通话",
        "video_call": "视频通话",
        "menu": "菜单",
        "home": "首页",
        "select_chat": "选择聊天开始对话",
        "no_messages": "暂无消息",
        "send": "发送",
    },
    "العربية": {
        "chats": "الدردشات",
        "search": "بحث",
        "settings": "الإعدادات",
        "theme": "المظهر",
        "profile": "الملف الشخصي",
        "username": "اسم المستخدم",
        "name": "الاسم",
        "language": "اللغة",
        "dark": "الوضع الداكن",
        "light": "الوضع الفاتح",
        "logout": "تسجيل الخروج",
        "new_chat": "دردشة جديدة",
        "type_message": "اكتب رسالة...",
        "online": "متصل",
        "last_seen": "آخر ظهور مؤخراً",
        "calls": "المكالمات",
        "contacts": "جهات الاتصال",
        "saved": "الرسائل المحفوظة",
        "edit_profile": "تعديل الملف",
        "save": "حفظ",
        "cancel": "إلغاء",
        "audio_call": "مكالمة صوتية",
        "video_call": "مكالمة فيديو",
        "menu": "القائمة",
        "home": "الرئيسية",
        "select_chat": "اختر محادثة لبدء المراسلة",
        "no_messages": "لا توجد رسائل",
        "send": "إرسال",
    },
    "Français": {
        "chats": "Discussions",
        "search": "Rechercher",
        "settings": "Paramètres",
        "theme": "Thème",
        "profile": "Profil",
        "username": "Nom d'utilisateur",
        "name": "Nom",
        "language": "Langue",
        "dark": "Mode sombre",
        "light": "Mode clair",
        "logout": "Se déconnecter",
        "new_chat": "Nouvelle discussion",
        "type_message": "Écrire un message...",
        "online": "en ligne",
        "last_seen": "vu récemment",
        "calls": "Appels",
        "contacts": "Contacts",
        "saved": "Messages enregistrés",
        "edit_profile": "Modifier le profil",
        "save": "Enregistrer",
        "cancel": "Annuler",
        "audio_call": "Appel audio",
        "video_call": "Appel vidéo",
        "menu": "Menu",
        "home": "Accueil",
        "select_chat": "Sélectionnez une discussion",
        "no_messages": "Aucun message",
        "send": "Envoyer",
    },
    "Русский": {
        "chats": "Чаты",
        "search": "Поиск",
        "settings": "Настройки",
        "theme": "Тема",
        "profile": "Профиль",
        "username": "Имя пользователя",
        "name": "Имя",
        "language": "Язык",
        "dark": "Тёмная тема",
        "light": "Светлая тема",
        "logout": "Выйти",
        "new_chat": "Новый чат",
        "type_message": "Написать сообщение...",
        "online": "в сети",
        "last_seen": "был(а) недавно",
        "calls": "Звонки",
        "contacts": "Контакты",
        "saved": "Избранное",
        "edit_profile": "Редактировать профиль",
        "save": "Сохранить",
        "cancel": "Отмена",
        "audio_call": "Аудиозвонок",
        "video_call": "Видеозвонок",
        "menu": "Меню",
        "home": "Главная",
        "select_chat": "Выберите чат",
        "no_messages": "Нет сообщений",
        "send": "Отправить",
    },
}

SAMPLE_CHATS = [
    {
        "name": "Alice",
        "last": "Hey, how are you?",
        "time": "10:45",
        "unread": 2,
        "online": True,
        "avatar": "A",
    },
    {
        "name": "Bob",
        "last": "See you tomorrow!",
        "time": "09:30",
        "unread": 0,
        "online": False,
        "avatar": "B",
    },
    {
        "name": "Charlie",
        "last": "Photo 📷",
        "time": "Yesterday",
        "unread": 1,
        "online": True,
        "avatar": "C",
    },
    {
        "name": "Diana",
        "last": "Thanks 😊",
        "time": "Yesterday",
        "unread": 0,
        "online": False,
        "avatar": "D",
    },
    {
        "name": "Team Group",
        "last": "Meeting at 5 PM",
        "time": "Mon",
        "unread": 5,
        "online": False,
        "avatar": "T",
    },
    {
        "name": "Saved Messages",
        "last": "Important note",
        "time": "Sun",
        "unread": 0,
        "online": False,
        "avatar": "💾",
    },
]


KV = """
#:import dp kivy.metrics.dp

<SplashScreen>:
    md_bg_color: app.theme_cls.bg_dark if app.theme_cls.theme_style == "Dark" else app.theme_cls.bg_light

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(40)

        MDBoxLayout:
            size_hint_y: None
            height: dp(180)
            Widget:
            MDIcon:
                icon: "message-text"
                font_size: "90sp"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                pos_hint: {"center_x": 0.5}
            Widget:

        MDLabel:
            text: "Quick Message"
            font_style: "H4"
            bold: True
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]

        MDLabel:
            text: "Connecting..."
            font_style: "Body1"
            theme_text_color: "Secondary"
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]

        Widget:
            size_hint_y: 0.3

        MDProgressBar:
            id: progress
            value: 0
            size_hint_x: 0.7
            pos_hint: {"center_x": 0.5}
            color: app.theme_cls.primary_color


<ChatListItem>:
    on_release: app.open_chat(root.chat_data)

    IconLeftWidget:
        icon: "account-circle"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color

    IconRightWidget:
        id: badge_icon
        icon: ""
        theme_text_color: "Custom"
        text_color: 0.16, 0.67, 0.93, 1


<MainScreen>:
    MDNavigationLayout:
        id: nav_layout

        MDScreenManager:
            id: screen_manager

            # ========== HOME SCREEN ==========
            MDScreen:
                name: "home"

                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        id: top_bar
                        title: app.t("chats")
                        elevation: 4
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                        right_action_items: [["magnify", lambda x: app.show_search()], ["dots-vertical", lambda x: app.show_menu()]]

                    MDBottomNavigation:
                        id: bottom_nav
                        panel_color: app.theme_cls.bg_dark if app.theme_cls.theme_style == "Dark" else app.theme_cls.bg_light
                        selected_color_background: app.theme_cls.primary_color
                        text_color_active: 1, 1, 1, 1

                        MDBottomNavigationItem:
                            name: "chats"
                            text: app.t("chats")
                            icon: "message-text"

                            MDBoxLayout:
                                orientation: "vertical"
                                MDScrollView:
                                    MDList:
                                        id: chat_list

                        MDBottomNavigationItem:
                            name: "calls"
                            text: app.t("calls")
                            icon: "phone"

                            MDBoxLayout:
                                orientation: "vertical"
                                MDLabel:
                                    text: app.t("calls") + " (Mock)"
                                    halign: "center"
                                    font_style: "H5"

                        MDBottomNavigationItem:
                            name: "contacts"
                            text: app.t("contacts")
                            icon: "account-group"

                            MDBoxLayout:
                                orientation: "vertical"
                                MDLabel:
                                    text: app.t("contacts") + " (Mock)"
                                    halign: "center"
                                    font_style: "H5"

                        MDBottomNavigationItem:
                            name: "settings"
                            text: app.t("settings")
                            icon: "cog"
                            on_tab_press: app.open_settings_screen()

                            MDBoxLayout:
                                orientation: "vertical"
                                MDLabel:
                                    text: app.t("settings")
                                    halign: "center"

                    MDFloatingActionButton:
                        icon: "message-plus"
                        pos_hint: {"right": 0.95, "y": 0.12}
                        on_release: app.new_chat()
                        md_bg_color: app.theme_cls.primary_color

            # ========== CHAT SCREEN ==========
            MDScreen:
                name: "chat"

                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        id: chat_top_bar
                        title: ""
                        elevation: 4
                        left_action_items: [["arrow-left", lambda x: app.go_back()]]
                        right_action_items: [["phone", lambda x: app.mock_call("audio")], ["video", lambda x: app.mock_call("video")]]

                    MDScrollView:
                        id: messages_scroll
                        MDBoxLayout:
                            id: messages_box
                            orientation: "vertical"
                            adaptive_height: True
                            padding: dp(10)
                            spacing: dp(8)

                    MDBoxLayout:
                        size_hint_y: None
                        height: dp(60)
                        padding: [dp(8), dp(8)]
                        spacing: dp(8)

                        MDTextField:
                            id: msg_input
                            hint_text: app.t("type_message")
                            mode: "round"
                            size_hint_x: 0.85
                            multiline: False
                            on_text_validate: app.send_message()

                        MDIconButton:
                            icon: "send"
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                            on_release: app.send_message()

        # ========== NAVIGATION DRAWER ==========
        MDNavigationDrawer:
            id: nav_drawer
            radius: [0, 16, 16, 0]

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: app.user_name
                    text: app.user_username
                    spacing: dp(4)
                    padding: [dp(12), 0, 0, dp(56)]

                OneLineAvatarIconListItem:
                    text: app.t("profile")
                    on_release: app.open_profile()
                    IconLeftWidget:
                        icon: "account"

                OneLineAvatarIconListItem:
                    text: app.t("settings")
                    on_release: app.open_settings_screen()
                    IconLeftWidget:
                        icon: "cog"

                OneLineAvatarIconListItem:
                    text: app.t("theme")
                    on_release: app.toggle_theme()
                    IconLeftWidget:
                        icon: "theme-light-dark"

                OneLineAvatarIconListItem:
                    text: app.t("language")
                    on_release: app.open_language()
                    IconLeftWidget:
                        icon: "translate"

                OneLineAvatarIconListItem:
                    text: app.t("calls")
                    on_release: app.mock_toast(app.t("calls"))
                    IconLeftWidget:
                        icon: "phone"

                OneLineAvatarIconListItem:
                    text: app.t("contacts")
                    on_release: app.mock_toast(app.t("contacts"))
                    IconLeftWidget:
                        icon: "account-group"

                OneLineAvatarIconListItem:
                    text: app.t("saved")
                    on_release: app.open_saved()
                    IconLeftWidget:
                        icon: "bookmark"

                OneLineAvatarIconListItem:
                    text: app.t("logout")
                    on_release: app.logout()
                    IconLeftWidget:
                        icon: "logout"
"""


class ChatListItem(ThreeLineAvatarIconListItem):
    chat_data = ObjectProperty(None)


class SplashScreen(MDScreen):
    def on_enter(self):
        Clock.schedule_once(self.start_progress, 0.3)

    def start_progress(self, dt):
        self.ids.progress.value = 0
        self.anim_progress = 0
        Clock.schedule_interval(self.update_progress, 0.02)

    def update_progress(self, dt):
        self.anim_progress += 2
        self.ids.progress.value = self.anim_progress
        if self.anim_progress >= 100:
            Clock.unschedule(self.update_progress)
            self.manager.current = "main"


class MainScreen(MDScreen):
    pass


class QuickMessageApp(MDApp):
    current_lang = StringProperty("English")
    user_name = StringProperty("You")
    user_username = StringProperty("@quickuser")
    dark_mode = BooleanProperty(True)
    selected_chat = ObjectProperty(None, allownone=True)

    def t(self, key):
        return LANGUAGES.get(self.current_lang, LANGUAGES["English"]).get(key, key)

    def build(self):
        self.title = "Quick Message"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.material_style = "M3"

        Builder.load_string(KV)

        self.sm = MDScreenManager()
        self.splash = SplashScreen(name="splash")
        self.main = MainScreen(name="main")
        self.sm.add_widget(self.splash)
        self.sm.add_widget(self.main)

        return self.sm

    def on_start(self):
        Clock.schedule_once(self.build_chat_list, 0.5)

    def build_chat_list(self, *args):
        try:
            chat_list = self.main.ids.chat_list
            chat_list.clear_widgets()
            for chat in SAMPLE_CHATS:
                item = ChatListItem(
                    text=chat["name"],
                    secondary_text=chat["last"][:40],
                    tertiary_text=chat["time"],
                    chat_data=chat,
                )
                if chat["unread"] > 0:
                    badge_num = min(chat["unread"], 9)
                    item.ids.badge_icon.icon = f"numeric-{badge_num}-circle"
                chat_list.add_widget(item)
        except Exception as e:
            print("build_chat_list error:", e)

    def open_chat(self, chat):
        self.selected_chat = chat
        self.main.ids.screen_manager.current = "chat"
        self.main.ids.chat_top_bar.title = chat["name"]

        messages_box = self.main.ids.messages_box
        messages_box.clear_widgets()

        mock_msgs = [
            ("left", "Hello! 👋"),
            ("right", "Hi there! How are you?"),
            ("left", "I'm good, thanks. Working on a new project."),
            ("right", "Sounds interesting! Tell me more."),
            ("left", chat.get("last", "Okay")),
        ]
        for side, text in mock_msgs:
            self.add_message(text, side)

    def add_message(self, text, side="right"):
        messages_box = self.main.ids.messages_box

        bubble_color = (0.16, 0.67, 0.93, 1) if side == "right" else (0.2, 0.25, 0.3, 1)

        card = MDCard(
            size_hint_y=None,
            padding=dp(12),
            radius=[
                dp(16),
                dp(16),
                dp(4) if side == "right" else dp(16),
                dp(16) if side == "right" else dp(4),
            ],
            md_bg_color=bubble_color,
            orientation="vertical",
            adaptive_height=True,
        )

        label = MDLabel(
            text=text,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            adaptive_height=True,
            size_hint_y=None,
        )
        card.add_widget(label)
        card.height = max(label.texture_size[1] + dp(24), dp(48))

        container = MDBoxLayout(
            size_hint_y=None, height=card.height + dp(4), adaptive_height=True
        )
        if side == "right":
            container.add_widget(MDLabel(size_hint_x=0.25))
            container.add_widget(card)
        else:
            container.add_widget(card)
            container.add_widget(MDLabel(size_hint_x=0.25))

        messages_box.add_widget(container)
        Clock.schedule_once(
            lambda dt: setattr(self.main.ids.messages_scroll, "scroll_y", 0), 0.1
        )

    def send_message(self):
        text = self.main.ids.msg_input.text.strip()
        if text and self.selected_chat:
            self.add_message(text, "right")
            self.main.ids.msg_input.text = ""
            Clock.schedule_once(
                lambda dt: self.add_message("Got it! 👍", "left"), 0.8
            )

    def go_back(self):
        self.main.ids.screen_manager.current = "home"
        self.selected_chat = None

    def new_chat(self):
        toast(self.t("new_chat") + " (Mock)")

    def show_search(self):
        toast(self.t("search") + " (coming soon)")

    def show_menu(self):
        toast("More options")

    def mock_toast(self, text):
        self.main.ids.nav_drawer.set_state("close")
        toast(text + " (Mock)")

    def open_profile(self):
        self.main.ids.nav_drawer.set_state("close")

        content = MDBoxLayout(
            orientation="vertical",
            spacing=dp(15),
            padding=dp(20),
            adaptive_height=True,
        )
        name_field = MDTextField(text=self.user_name, hint_text=self.t("name"))
        user_field = MDTextField(
            text=self.user_username, hint_text=self.t("username")
        )
        content.add_widget(name_field)
        content.add_widget(user_field)

        def save(*args):
            self.user_name = name_field.text
            self.user_username = user_field.text
            dialog.dismiss()
            toast("Profile updated")

        dialog = MDDialog(
            title=self.t("edit_profile"),
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text=self.t("cancel"), on_release=lambda x: dialog.dismiss()
                ),
                MDRaisedButton(text=self.t("save"), on_release=save),
            ],
        )
        dialog.open()

    def open_settings_screen(self):
        self.main.ids.nav_drawer.set_state("close")
        toast(
            self.t("settings")
            + "\n• Notifications\n• Privacy\n• Data & Storage"
        )

    def toggle_theme(self):
        self.main.ids.nav_drawer.set_state("close")
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            self.dark_mode = False
        else:
            self.theme_cls.theme_style = "Dark"
            self.dark_mode = True
        toast(self.t("dark") if self.dark_mode else self.t("light"))

    def open_language(self):
        self.main.ids.nav_drawer.set_state("close")

        content = MDBoxLayout(
            orientation="vertical", adaptive_height=True, spacing=dp(5)
        )
        for lang in LANGUAGES.keys():
            item = OneLineListItem(
                text=lang, on_release=lambda x, l=lang: self.change_language(l)
            )
            content.add_widget(item)

        self.lang_dialog = MDDialog(
            title=self.t("language"),
            type="custom",
            content_cls=content,
            size_hint=(0.85, None),
            height=dp(420),
        )
        self.lang_dialog.open()

    def change_language(self, lang):
        self.current_lang = lang
        self.lang_dialog.dismiss()
        self.main.ids.top_bar.title = self.t("chats")
        self.main.ids.msg_input.hint_text = self.t("type_message")
        toast(f"Language: {lang}")
        self.build_chat_list()

    def open_saved(self):
        self.main.ids.nav_drawer.set_state("close")
        self.open_chat(
            {
                "name": "Saved Messages",
                "last": "Important note",
                "online": False,
            }
        )

    def mock_call(self, call_type):
        if not self.selected_chat:
            toast("Select a chat first")
            return
        title = (
            self.t("audio_call") if call_type == "audio" else self.t("video_call")
        )
        toast(f"{title} with {self.selected_chat['name']}\n(Mock feature)")

    def logout(self):
        self.main.ids.nav_drawer.set_state("close")

        def confirm(btn):
            dialog.dismiss()
            self.stop()

        dialog = MDDialog(
            title=self.t("logout"),
            text="Are you sure?",
            buttons=[
                MDFlatButton(
                    text=self.t("cancel"), on_release=lambda x: dialog.dismiss()
                ),
                MDRaisedButton(text=self.t("logout"), on_release=confirm),
            ],
        )
        dialog.open()


if __name__ == "__main__":
    QuickMessageApp().run()
