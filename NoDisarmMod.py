from memory import *
from memory.hooks import *
from memory.manager import TypeManager


func = find_binary('server.so')[b'']
#For Linux, version 1.37.4.3 CSGO
OffsetNudge = 0x00C44E85
(func + OffsetNudge).unprotect(8)
val = func.get_ulong_long(OffsetNudge)
print("Pre patch value is " + str(val))
if val != 12747720220099249167:
    print("Punch disarm offset not found. Unable to load or this instruction already patched.")
else:
    val = func.set_ulong_long(12747598174457632233, OffsetNudge)
    print("Successfully patched bytes. Enjoy !")
