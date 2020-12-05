import AOC
import time

data = AOC.Advent(2020,5).input_data

def main():
  def seat_number(id):
    row, col = id[:7], id[7:]
    row = int(row.replace('B','1').replace('F','0'), 2)
    col = int(col.replace('L','0').replace('R','1'), 2)
    return 8 * row + col

  x = {seat_number(line) for line in data}

  if __name__ == "__main__":
    print("The solution to problem 1 is: {}".format(max(x)))
    print("The solution to problem 2 is: {}".format( set(range(min(x), max(x)+1)) - x ))

start = time.time()
main()
print('Completed in {} seconds.'.format(time.time() - start))