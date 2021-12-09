def sum (number,number1):
  sum = number+number1
  return sum

print (sum(1,4))
# Or 
results = sum (2,5)
print (results)

def first ():
  def second ():
    print('hello')
  second()
first()