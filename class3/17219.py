import sys

N,M = map(int, sys.stdin.readline().strip().split())
address_password = {}

i = 0
while i < N:
    address, password = map(str, sys.stdin.readline().strip().split())
    address_password[address] = password
    i += 1
    
j = 0 
while j < M:
    address = sys.stdin.readline().strip()
    try:
        print(address_password[address])
    except KeyError:
        continue
    j += 1