import rpyc
conn = rpyc.classic.connect("localhost")

rlist = conn.modules.builtins.list((0,1,2,3,4,5,6,7,8,9)) #remote list












# USING MODULES TO EXCHANGE WITH THE OTHER EXECUTABLE

"""rsys = conn.modules.sys
print ('hello world', file = conn.modules.sys.stdout) #printing something in an other executable

# USING BULLETINS TO OPEN AND READ OTHER FILES

f = conn.builtins.open('C:/Users/ArthSpheres/Documents/Popup-master/All_tests/reading_test.txt')
f.read()

# EXECUTING and EVAL methods are importing library

conn.execute('import math')
#print(conn.eval('2*math.pi'), file = conn.modules.sys.stdout)

# TELEPORTING FUNCTIONS

def square(x):
    return x**2

fn = conn.teleport(square)
fn(2)
conn.eval('square(3)')

conn.execute('import sys')
version = conn.teleport(lambda: print(sys.version_info))
version()"""