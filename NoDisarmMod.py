from memory import *
from memory.hooks import *
from memory.manager import TypeManager

#func = find_binary('server.so')[b'\x0F\x84\xB0\xF6\xFF\xFF\x8B'].get_ulong_long()
func = find_binary('server.so')[b'']
#func = find_binary('server.so').base+0x00C42915
#func.set_float(func, 0.0)
#1)0xeff46700 first main entry lets nudge it to our needed instruction
#func = hex(func.base+0x00C42915)
#val = func.set_ulong_long(0x00C42915, 16206362688278173161)
func.unprotect(0x00C42915)
val = func.get_ulong_long(0x00C42915)
val = func.set_ulong_long(16206362688278173161, 0x00C42915)
print(val)
#pre 16206484733919790095
#should be 16206362688278173161
#print(val)

#val = func.get_ulong_long(0x00C42915)
#print("PATCHED TO " + str(val))
#gg = func.get_ulong_long()
#print(gg)
#10775988008234550287 before patching
#if func == 10775988008234550287:
#    print("Found fists offsets and other shit, lets do magic")
#    find_binary('server.so')[b'\x0F\x84\xB0\xF6\xFF\xFF\x8B'].set_ulong_long(10775865962599461353)
