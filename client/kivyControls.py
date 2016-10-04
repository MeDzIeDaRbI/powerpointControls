import urllib

from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.network.urlrequest import UrlRequest



class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.row = 2
        self.add_widget(Label(text='Server'))
        self.username = TextInput(text='http://127.0.0.1:8000/',multiline=False)
        self.add_widget(self.username)

        self.nextB = Button(text="next")
        self.nextB.bind(on_press=self.sendNext)
        self.add_widget(self.nextB)

        self.prevB = Button(text="previous")
        self.prevB.bind(on_press=self.sendPrevious)
        self.add_widget(self.prevB)

    def sendNext(self,instance):
        params = urllib.urlencode({'action': 'next'})

        headers = {'Content-type': 'application/x-www-form-urlencoded',
               'Accept': 'text/plain'}
        url = self.username.text+ 'control/activ/'
        req = UrlRequest(url, on_success=self.bug_posted, req_body=params,
                     req_headers=headers)
    def sendPrevious(self,instance):
        params = urllib.urlencode({'action': 'previous'})

        headers = {'Content-type': 'application/x-www-form-urlencoded',
               'Accept': 'text/plain'}
        url = self.username.text + 'control/activ/'
        req = UrlRequest(url, on_success=self.bug_posted, req_body=params,
                     req_headers=headers)

    def bug_posted(self, req, result):
        print('Our bug is posted !')
        print(result)






class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()