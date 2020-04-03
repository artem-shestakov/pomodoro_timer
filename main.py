import rumps


class Pomodoro(rumps.App):
    def __init__(self):
        super(Pomodoro, self).__init__("Pomodoro Timer", icon='./icons/tomato.png')
        self.menu = ["Start Timer", "Stop Timer", "Say hi"]


if __name__ == '__main__':
    Pomodoro().run()
