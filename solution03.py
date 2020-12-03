import AOC
import time

def main():
  start = time.time()
  data = AOC.Advent(2020,3).input_data
  matrix = [line.replace('#','1').replace('.','0') for line in data]
  matrix = [[int(value) for value in row] for row in matrix]
  
  def slope(horizontal, vertical):
    trees = 0
    for i in range( int( len(matrix) / vertical // 1 ) ):
      trees += matrix[vertical * i][horizontal * i % len(matrix[0])]
    return trees

  if __name__ == "__main__":
    print("The solution to problem 1 is: {}".format(slope(3,1)))
    print("The solution to problem 2 is: {}".format(slope(1,1) * slope(3,1) * slope(5,1) * slope(7,1) * slope(1,2)))
    print('Completed in {} seconds.'.format(time.time() - start))

main()