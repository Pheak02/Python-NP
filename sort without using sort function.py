# 3. Write a sorting function without using the list.sort function
initial_list = [ 12,13,5,34,5,1,2,3,-6,7,90,67,102]
new_list = []
while initial_list:
    minimum = initial_list[0]
    for i  in initial_list:
            if minimum < i:
                minimum = i
    # new_list.insert(0,minimum) 
    new_list.append(minimum) 
    initial_list.remove(minimum)
print( new_list)
