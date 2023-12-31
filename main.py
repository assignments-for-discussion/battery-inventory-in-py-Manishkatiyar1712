
def count_batteries_by_health(present_capacities):
    h=e=f=0
    for i in present_capacities:
        a=(100*i)/120
        if a>80:
            h=h+1
        elif (a>=63 and a<=80):
            e=e+1
        else:
            f=f+1
    return {
    "healthy": h,
    "exchange": e,
    "failed": f
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 72]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
