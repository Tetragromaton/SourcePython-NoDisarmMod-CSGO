from memory import *
from memory.hooks import *
from memory.manager import TypeManager


func = find_binary('server.so')[b'']
#For Linux, version 1.37.4.4 CSGO
OffsetNudge = 0x00C44F55
(func + OffsetNudge).unprotect(8)
val = func.get_ulong_long(OffsetNudge)
print("Pre patch value is " + str(val))
if val != 16206484733919790095:
    print("Punch disarm offset not found. Unable to load or this instruction already patched.")
else:
    val = func.set_ulong_long(16206362688278173161, OffsetNudge)
    print("Successfully patched bytes. Enjoy !")
