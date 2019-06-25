from weekday import Weekday
from station import Station
from schedule import Schedule

# 测试代码
if __name__ == "__main__":
    sun_schedule = Schedule()
    sun_schedule.add('2019-06-23 16:00', '2019-06-23 17:00', '大国风云')
    sun_schedule.add('2019-06-23 17:05', '2019-06-23 17:50', '新闻30分')
    station = Station("CCTV1")
    station.add(Weekday.Sun, sun_schedule)
    print('Test is done.')
