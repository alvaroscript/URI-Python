def entrada():
    t1,t2,t3,t4 = map(int,input().split())
    return t1,t2,t3,t4

def total(t1,t2,t3,t4):
    return t1 + t2 + t3 + t4 - 3

def main():
    t1,t2,t3,t4 = entrada()
    print(total(t1,t2,t3,t4))

main()
