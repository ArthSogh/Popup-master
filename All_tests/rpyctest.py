from multiprocessing import Pool
import time
import math

N = 10000

def cube(x):
    return math.sqrt(x)

if __name__ == "__main__":
    # first way, using multiprocessing
    start_time = time.perf_counter()
    with Pool() as pool:
      result = pool.map(cube, range(10,N))
    finish_time = time.perf_counter()
    print("Program finished in {} seconds - using multiprocessing".format(finish_time-start_time))
    print("---")
    # second way, serial computation
    start_time = time.perf_counter()
    result = []
    for x in range(10,N):
      result.append(cube(x))
    finish_time = time.perf_counter()
    print("Program finished in {} seconds".format(finish_time-start_time))

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