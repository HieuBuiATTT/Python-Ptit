import math 

def nguyento(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'NO'
    return 'YES' if n > 1 else 'NO'

def main():
    for t in range(int(input())):
        n = int(input())
        dem = 0
        for i in range(n):
            if math.gcd(n,i) == 1:
                dem += 1
        print(nguyento(dem))

if __name__ == "__main__":
    main()
