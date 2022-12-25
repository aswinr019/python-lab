class Time:


    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    def __add__(self,other):

          second = self.__second + other.__second

          r = second % 60
          q = int( second / 60 )

          second = r
          minute = q


          minute += self.__minute + other.__minute
          r = minute % 60
          q = int( minute / 60 )

          minute = r
          hour = q


          hour +=  self.__hour + other.__hour

          return Time(hour,minute,second)



h1 = int(input("Enter first hour : "))
m1 = int(input("Enter first minute : "))
s1 = int(input("Enter first second : "))
h2 = int (input("Enter second hour : "))
m2 = int(input("Enter second minute : "))
s2 = int(input("Enter second second : "))

time1 = Time(h1,m1,s1)
time2 = Time(h2,m2,s2)

time3 = time1+time2

print("Sum of times is : ",Time.get_hour(time3),Time.get_minute(time3),Time.get_second(time3))
          
