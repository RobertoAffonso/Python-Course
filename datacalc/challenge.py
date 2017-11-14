# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks
import time

print("Time()")
print("Is it adjustable? %s" % time.get_clock_info('time').adjustable)
print("What function it uses during its implementation? " + time.get_clock_info('time').implementation)
print("Is it monotonic? %s" % time.get_clock_info('time').monotonic)
print("How precise it is? {}".format(time.get_clock_info('time').resolution))
print("")
print("#" * 50)
print("")

print(time.get_clock_info('perf_counter'))
print(time.get_clock_info('monotonic'))
print(time.get_clock_info('process_time'))



