#Ryan Crop, Time of day python
import time
current = time.time()

local_time = time.localtime(current)
print(local_time)
hour = local_time.tm_hour

if hour > 5 & hour< 11:
    print("Hello and good mourning.")
elif hour >= 11 & hour <= 16:
    print("Hello, you should really be outside because its a great afternoon")
elif hour > 16 & hour < 21:
    print("Hello I hope your having a great  evening but you should be heading to bed soon.")
else:
    print("Man! It's to early for this, go to bed! And have a good night!")