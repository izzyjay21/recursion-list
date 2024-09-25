def total_sum(list):
 length = len(list)
 if length == 1:
  return  list[0]
 return list[0]+ total_sum(list[1:])

list = [8,5,4,3,8,3]
print(total_sum(list))

