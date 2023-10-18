
def count_batteries_by_health(present_capacities):
  healthy=exchange=failed=0
  ratedcapacity=120
  for i in present_capacities:
    soh=(i/ratedcapacity)*100

    if soh>80:
      healthy+=1
    elif soh>=63 and soh<=80:
      exchange+=1
    elif soh<63:
      failed+=1
  return {
    "healthy": healthy,
    "exchange": exchange,
    "failed": failed
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
