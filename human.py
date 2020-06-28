import random
from time import sleep

def human_behavior(Driver):
    a,b,c,d,e,f = (random.randint(1, 5) for x in range(6))
    x,y = (random.randint(100,300) for x in range(2))
    z,v = (random.randint(100,1000) for x in range(2))
    sleep(c+d)
    Driver.execute_script(f"window.scrollTo(0, {x+z})")
    sleep(e+f)
    Driver.execute_script(f"window.scrollTo(0, {y+v})")
    sleep(d+c)
    Driver.execute_script(f"window.scrollTo(0, {y+z})")
    sleep(d+e)
    Driver.execute_script(f"window.scrollTo(0, {x+v})")
    sleep(a+b)
