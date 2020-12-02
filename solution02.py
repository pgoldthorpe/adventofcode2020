import AOC
data = AOC.Advent(2020,2).input_data

def main():

  def pw(password, letter, start, end):
    return start <= password.count(letter) <= end

  def pw2(password, letter, start, end):
    return bool(password[end-1] == letter) ^ bool(password[start-1] == letter)
  
  part1 = 0
  part2 = 0

  for line in data:
    a, password = line.split(':')
    password = password.strip()
    a, letter = a.split(' ')
    start, end = [int(i) for i in a.split('-')]
    part1 += pw(password, letter, start, end)
    part2 += pw2(password, letter, start, end)

  print("The solution to problem 1 is: {}".format(part1))
  print("The solution to problem 2 is: {}".format(part2))

main()