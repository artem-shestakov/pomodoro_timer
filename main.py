import rumps
from datetime import datetime


class Pomodoro(rumps.App):
    def __init__(self):
        super(Pomodoro, self).__init__("Pomodoro Timer", 
                                       icon='./icons/tomato.png',
                                       quit_button=None)
        self.start_button = rumps.MenuItem("{: <8}".format("Start"),
                                           callback=self.timer_start,
                                           icon='./icons/play-button.png')
        self.stop_button = rumps.MenuItem("Stop", callback=self.timer_stop,
                                          icon='./icons/stop.png')
        self.exit_button = rumps.MenuItem("Exit", callback=self.exit_app, 
                                          icon='./icons/logout.png')
        self.menu = [self.start_button, self.stop_button, rumps.separator,
                     self.exit_button]
        self.timer = rumps.Timer(self.timer_on, 1)
        self.timer_reset()

    def timer_start(self, sender):
        if sender.title.startswith("Start"):                    # Press Start
            self.timer.start_ = datetime.now()
            self.timer.end = 1500
            self.timer.pause = 0
            self.timer.total_pause = 0
            self.timer.start()
            sender.title = "Pause"
            sender.icon = './icons/pause.png'
        elif sender.title == "Continue":                        # Press Continue
            self.timer.pause = datetime.now() - self.timer.pause_time
            self.timer.pause = int(self.timer.pause.total_seconds())
            self.timer.total_pause += self.timer.pause
            self.timer.start()
            sender.title = "Pause"
            sender.icon = './icons/pause.png'
        else:                                                   # Press Pause
            self.timer.pause_time = datetime.now()
            sender.title = "Continue"
            sender.icon = './icons/play-button.png'
            self.timer.stop()

    def timer_stop(self, sender):
        self.timer.stop()
        self.title = ""
        self.start_button.title = "Start"
        self.start_button.icon = './icons/play-button.png'

    def timer_reset(self):
        self.timer.stop()
        self.timer.count = 0

    def timer_on(self, sender):
        time_left = datetime.now() - sender.start_
        time_left = time_left.total_seconds() - sender.total_pause
        print(time_left, sender.total_pause)
        mins = (sender.end - time_left) // 60
        secs = (sender.end - time_left) % 60
        if time_left > sender.end:
            rumps.notification("Pomodoro timer", "Time for break!", "")
            mins = 0
            secs = 0
        else:
            print("Waiting notification")
        sender.count += 1
        self.title = "{:0>2d}:{:0>2d}".format(int(mins), int(secs))

    # Close app function
    def exit_app(self, sender):
        rumps.quit_application(sender)


if __name__ == '__main__':
    Pomodoro().run()
