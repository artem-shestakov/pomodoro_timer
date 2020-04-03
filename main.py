import rumps
import datetime


class Pomodoro(rumps.App):
    def __init__(self):
        super(Pomodoro, self).__init__("Pomodoro Timer", icon='./icons/tomato.png')
        self.menu = ["Start Timer", "Stop Timer", "Say hi"]
        self.timer = rumps.Timer(self.timer_on, 2)
        self.timer_reset()

    @rumps.clicked("Start Timer")
    def timer_start(self, sender):
        self.timer.count_start = datetime.datetime.now()
        self.timer.count = 0
        self.timer.end = 10
        self.timer.start()

    @rumps.clicked("Stop Timer")
    def timer_stop(self, sender):
        self.timer.stop()

    @rumps.clicked("Say hi")
    def hello(self, _):
        rumps.notification("t", "st", "m")

    def timer_reset(self):
        self.timer.stop()
        self.timer.count = 0

    def timer_on(self, sender):
        time_left = datetime.datetime.now() - sender.count_start
        print(time_left.total_seconds())
        #time_left = sender.end - sender.count
        if time_left.total_seconds() > 10:
            rumps.notification("Stop", "-_-", "Stop work")
        else:
            print("*")
#        sender.count += 2
        print(time_left)


if __name__ == '__main__':
    Pomodoro().run()
