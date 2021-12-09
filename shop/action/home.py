from products.models import ToDoList 
def hai (request,products,to) :
  text1 = request.GET
  name = text1.get ("name")
  print (name)
  hello = 'hello'
  
  list1 = ToDoList(name=str(name))
  list1.save()
    
  if name == "a":
    hello= ' hai'
  data = {'products':products,'text':name,'hello':hello,'to':to}
  return data
 
