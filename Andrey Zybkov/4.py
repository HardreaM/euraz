class Date:

    def __init__ (self, day, month, year):
        self.validate_day(day)
        self.validate_month(month)
        self.validate_year(year)

    def validate_day (self, day):
        if day <= 31 and day >= 1:
            if day < 10:        
                self.__day = '0' + str(day)
            else:
                self.__day = str(day)
        else:
            raise ValueError()

    def validate_month (self, month):
        if month <= 12 and month >= 1:
            if month < 10:
                self.__month = '0' + str(month)
            else:
                self.__month = month
        else:
            raise ValueError()

    def validate_year (self, year):
        if str(type(year)) == '<class \'int\'>':
            self.__year = year
        else:
            raise ValueError()

    def to_month(self, month):
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентябр', 'октября', 'ноября', 'декабря']
        return months[month-1]

    def full_view (self):
        print(str(self.__day) + ' ' + str(self.to_month(int(self.__month))) + ' ' + str(self.__year) + ' года')

    def short_view (self):
        print(str(self.__day) + '.' + str(self.__month) + '.' + str(self.__year))

date1 = Date(1, 1, 2001)
date1.short_view()
date1.full_view()