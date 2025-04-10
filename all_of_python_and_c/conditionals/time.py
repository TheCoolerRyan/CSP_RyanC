#Ryan Crop, How to get time of day

import time
# gmtime(0) is the first instense
#print(time.gmtime(0))

#curent time in secondes sense the first time 1970
#print(time.time())

#curre3nt time in seconds sense gmtime
current = time.time()

#Day date hour minute seconds year
now = time.ctime(current)
print(now)

#Get just the hour
local_time = time.localtime(current)
print(local_time)
hour = local_time.tm_hour
minute = local_time.tm_min
print(hour)