
def count_batteries_by_health(present_capacities,b):
    h=e=f=0
    for i in present_capacities:
        a=(100*i)/b
        if a>80:
            h=h+1
        elif (a>=63 and a<=80):
            e=e+1
        else:
            f=f+1
    d= {
    "healthy": h,
    "exchange": e,
    "failed": f
  }
    return(d)


def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities =[]
    while(True):
        a=int(input("capacity(for ending enter 0):"))
        
        if a==0:
            break
        else:
            present_capacities.append(a)
            continue
    b=int(input("enter rated capacity: "))
    counts = count_batteries_by_health(present_capacities,b)
    for i in counts:
        print(i,counts[i])
  
    print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()
