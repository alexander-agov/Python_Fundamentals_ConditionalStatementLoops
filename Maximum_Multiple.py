divisor = int(input())
boundary = int(input())
for n in range(boundary, divisor-1, -1):
    if n <= boundary and n % divisor == 0:
        print(n, end='')
        break


# for n in range(start, stop, step) excl. stop
# for n in range(start, stop) step = 1
# for n in range(stop) start = 0, step = 1