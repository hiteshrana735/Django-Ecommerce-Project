import time

oldertime = time.time()
for i in range(1, 101):
    print(i, end="")

newtime = time.time()

a = 1
while a <= 100:
    print(a, end="")
    a += 1

time3 = time.time()

timetakenbyfor = newtime-oldertime
timetakenbywhile = time3-newtime

print(f"\nTime taken by the for loop is {round(timetakenbyfor, 5)} seconds")
print(f"\nTime taken by the while loop is {round(timetakenbywhile, 5)} seconds")