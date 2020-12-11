# [x] define a function that creates a fibonacci sequence where the length is equal to the integer passed as an arg.


# [x] define a function that returns the the number in the fib sequence at the index of the integer passed as an argument.  


# [x] define a function that creates a Lucas sequence where the length is equal to the integer passed as an argument
# [x] define a function that returns a value from a lucas sequence at the index of the argument passed. 
# [] define a function that returns the Nth value of either a fibonacci || Lucas sequence passing an integer as the required arg and passing optional arguments that deciced the sequence defaulting to fibbonacci

# def fib_num(n):
#   '''function returns a list of fibonaci values up to the length of the argument `n`
#   '''
#   first = 0
#   second = 1
#   initial = first
#   counter = 2

#   while counter <= n:
#     initial = first + second 
#     second = first
#     first = initial
#     counter += 1


#   # [2, 1, 3, 4, 7]
#   return first


def fibbonacci(n):
  """fn returns Nth fibbonaci value
     value lives at index n-1
  """
  seq = [0, 1]

  while len(seq) <= n:
    seq.append(seq[len(seq)-1] + seq[len(seq) - 2])
  return seq[n-1]
 
 

def lucas(n):
  """ fn returns Nth lucas number
      value lives at index n-1
  """
  seq = [2, 1]

  while len(seq) <= n:
    seq.append(seq[len(seq)-1] + seq[len(seq) - 2])
  return seq[n-1]
  

def sum_series(n, first = 0, second = 1):
  """fn returns nth value of given sequence
     defaults to fibbonacci values. 
  """
  seq = [first, second]

  while len(seq) <= n:
    seq.append(seq[len(seq)-1] + seq[len(seq) - 2])
  return seq[n-1]