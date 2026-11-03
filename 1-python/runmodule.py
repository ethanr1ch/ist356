import mymodule

print(mymodule.country)

import mymodule as mm

print(mm.country)

mm.say_hi("Ethan")

from mymodule import say_hi

say_hi("Ethan")