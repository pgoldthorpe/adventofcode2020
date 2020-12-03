import AOC
import time

def main():
  start = time.time()
  data = AOC.Advent(2020,3).input_data
  repeats = int( 7 * len(data) / len(data[0]) //1 + 1 )
  matrix = [line.replace('#','1').replace('.','0') * repeats for line in data]
  matrix = [[int(value) for value in row] for row in matrix]

  s1, s2, s3, s4, s5 = 0, 0, 0, 0, 0
  for i in range(len(matrix)):
    s1 += matrix[i][i]   # Right 1, down 1.
    s2 += matrix[i][3*i] # Right 3, down 1. (Part 1)
    s3 += matrix[i][5*i] # Right 5, down 1.
    s4 += matrix[i][7*i] # Right 7, down 1.

  for i in range( int(len(matrix)/2//1) ):
    s5 += matrix[2*i][i] # Right 1, down 2.

  print("The solution to problem 1 is: {}".format(s2))
  print("The solution to problem 2 is: {}".format(s1*s2*s3*s4*s5))
  print('Completed in {} seconds.'.format(time.time() - start)) # 0.241 seconds

main()