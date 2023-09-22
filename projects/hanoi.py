# ip = initial peg
# fp = final peg
# ap = auxilary peg
def hanoi(n,ip,ap,fp):
    if n == 1 :
        print("move disk 1 from rod {} to rod {}".format(ip,fp))
        return
    hanoi(n-1,ip,fp,ap)
    print("move disk {} from {} to {}".format(n,ip,fp))
    hanoi(n-1,ap,ip,fp)
n = int(input("enter height of tower : "))
hanoi(n,"A","B","C")


