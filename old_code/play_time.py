import time
import calendar

print "time.time():",time.time()
print "time.localtime(time.time()):",time.localtime(time.time())
print "time.asctime(time.localtime(time.time())):",time.asctime(time.localtime(time.time()))

cal=calendar.month(2016,1)
print cal

cal2=calendar.calendar(2016)
print cal2


