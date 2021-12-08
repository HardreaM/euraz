class Time:

    def __init__ (self):
        pass

    def set_time (self, hours, minutes, seconds):
        self.validate_time(hours, minutes, seconds)

    def validate_time (self, hours, minutes, seconds):
        if hours >= 0 and hours <= 23:
            self.__hours = hours
        else:
            raise ValueError()
        
        if minutes >= 0 and minutes <= 59:
            self.__minutes = minutes
        else:
            raise ValueError()

        if seconds >= 0 and seconds <= 59:
            self._seconds = seconds
        else:
            raise ValueError()

    def get_hours (self):
        return self.__hours

    def get_minutes (self):
        return self.__minutes

    def get_seconds (self):
        return self._seconds

    def to_pm_am (self, hours):
        if hours < 12:
            return str(hours) + ' a.m. '
        else:
            return str(hours) + ' p.m. '

    def print_full (self):
        print(str(self.get_hours()) + ' hours ' + str(self.get_minutes()) + ' minutes ' + str(self.get_seconds()) + ' seconds')

    def print_short (self):
        print(self.to_pm_am(self.get_hours()) + str(self.get_minutes()) + ' minutes ' + str(self.get_seconds()) + ' seconds')

time1 = Time()
time1.set_time(14, 8, 8)
time1.print_short()
time2 = Time()
time2.set_time(22, 34, 54)