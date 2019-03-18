class Clock(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.calibrate()

    def calibrate(self):
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        while self.minute < 0:
            self.minute += 60
            self.hour -= 1

        self.hour %= 24

    def __repr__(self):
        return('{:02d}:{:02d}'.format(self.hour, self.minute))

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.minute += minutes
        self.calibrate()
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        self.calibrate()
        return self