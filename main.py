import rumps
import datetime


class Pomodoro(rumps.App):
    def __init__(self):
        super(Pomodoro, self).__init__("Pomodoro Timer", icon='./icons/tomato.png')
        #self.start_button = rumps.MenuItem("Start Timer")
        #self.stop_button = rumps.MenuItem("Stop Timer")
        #self.menu = ["Start Timer", "Stop Timer", "Say hi"]
        self.timer = rumps.Timer(self.timer_on, 1)
        self.timer_reset()

    @rumps.clicked("Start Timer")
    def timer_start(self, sender):
        self.timer.count_start = datetime.datetime.now()
        self.timer.count = 0
        self.timer.end = 15
        self.timer.start()

    @rumps.clicked("Stop Timer")
    def timer_stop(self, sender):
        self.timer.stop()
        self.title = ""

    def timer_reset(self):
        self.timer.stop()
        self.timer.count = 0

    def timer_on(self, sender):
        self.menu[0] = "Continue"
        time_left = sender.end - sender.count
        mins = time_left // 60
        secs = time_left - (mins * 60)
        if time_left < 0:
            rumps.notification("Pomodoro timer", "Time for break!", "")
        else:
            print("Waiting notification")
        sender.count += 1
        self.title = "{:0>2d}:{:0>2d}".format(mins, secs)

if __name__ == '__main__':
    Pomodoro().run()
