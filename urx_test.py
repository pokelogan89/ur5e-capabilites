import urx
from time import sleep

ur5 = urx.Robot("192.168.1.102")
ur5.set_tcp((38.62,-29.04,147,0,0,0))
ur5.set_payload(1.6,(1,1,63))
sleep(.2)

a = 1.2
v = .25
print(ur5.x,ur5.y,ur5.z)
#ur5.movel((-.415,-.350,-.100,.156,-3.133,-.057),a,v)
#ur5.movel((-.415,.250,-.100,.156,-3.133,-.057),a,v)
quit()