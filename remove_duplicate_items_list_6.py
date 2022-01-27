def my_function(x):
  return list(dict.fromkeys(x))

list = my_function(["Mike", "Emma", "Emma", "Kelly", "Mike", "Brad"])
print(list)