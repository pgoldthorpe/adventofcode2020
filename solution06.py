import AOC
import time

AOC.Advent(2020,6)
with open('input/input06.txt') as f:
    data = f.readlines()
data = ''.join(data).split('\n\n')

def main():
  
  def count(group:str) -> int:
    s = set('a b c d e f g h i j k l m n o p q r s t u v w x y z'.split())
    for question in group.split():
        s = s.intersection(set(question))
    return len(s)

  if __name__ == "__main__":
    print("The solution to problem 1 is: {}".format(sum((len(set(i.replace('\n',''))) for i in data))))
    print("The solution to problem 2 is: {}".format(sum(count(group) for group in data)))

start = time.time()
main()
print('Completed in {} seconds.'.format(time.time() - start))