from datetime import datetime
from enum import Enum

class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12
    Undef = "Undefined"

class Date:
    month = Month.Undef
    day = -1
    year = -1.1
    def init(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
    def init():
        pass
    def __str__(self):
        return f"{self.month} {self.day},{self.year}"

class User:
    birthday = Date()
    username = ""
    fullName = ""
    firstName = ""
    pcMoney = -1
    
    def setBirthday(self, month, day, year):
        leapYear = False
        try:
            if isinstance(day, int):
                pass
            else:
                raise ValueError
        except ValueError:
            return ValueError("Day is not an integer")
        try:
            if isinstance(month, int):
                pass
            else:
                raise ValueError
        except ValueError:
            return ValueError("Month is not an integer")
        try:
            self.birthday.month = Month(month)
        except ValueError:
            return ValueError("Month out of range (month number has to be 0-12)")
        try:
            if year > datetime.today().year:
                raise ValueError
            else:
                self.birthday.year = year
        except ValueError:
            return ValueError("Year past current year")
        if year%4 == 0:
            leapYear = True
        if leapYear:
            daysInMonths = [31, 29, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]
        if not leapYear:
            daysInMonths = [31, 28, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]
        self.birthday.day = day
        if self.birthday.day > daysInMonths[month-1]:
            return ValueError("Too many days for month entered")
        file = open("userFile", "w")
        file.write(self.userFileReset())
    
    def setUserInfo(self, userinfo):
        while True:
            self.username = userinfo[0]
            self.firstName = (userinfo[0].split(" "))[0]
            try:
                self.pcMoney = userinfo[1]
                self.setBrithday(userinfo[2])
            finally:
                break

    def debug(self):
        print("(1) Username:", self.username)
        print("(2) Birthday:", self.birthday)

    def userFileReset(self):
        return f"{self.username}\n{self.pcMoney}\n{self.birthday}"