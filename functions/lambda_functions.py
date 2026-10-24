my_lambda = lambda x: x*2
print(my_lambda(5))

x=lambda a, b: a + b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n
my_doubler = myfunc(2)
print(my_doubler(11))

words = ['cat', 'window', 'defenestrate']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)