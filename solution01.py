import AOC
AOC.Advent(2020,1)

def main():
  with open('input/input01.txt') as f:
    expense = [int(i) for i in f.read().splitlines()]
  
  def loopsum(looplist, val=2020) -> int:
    for index, item1 in enumerate(looplist):
      for item2 in looplist[index:]:
        if item1 + item2 == val:
          return item1, item2

  def loopsum2(looplist, val=2020) -> int:
    for idx1, item1 in enumerate(looplist):
      for idx2, item2 in enumerate(looplist[idx1:]):
        for item3 in looplist[idx2:]:
          if item1 + item2 + item3 == val:
            return item1, item2, item3


  if __name__ == "__main__":
    item1, item2 = loopsum(expense)
    print("The solution to problem 1 is: {}".format(item1*item2))

    item1, item2, item3 = loopsum2(expense)
    print("The solution to problem 2 is: {}".format(item1*item2*item3))


main()
