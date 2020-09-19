def function():
	result = 0
	even_list = []
	list =[3,4,2,5,10,7,8]
	for item in list:
		if item % 2 == 0 :
			even_list.append(item)
	if even_list == None:
		return -1
	else:
	    for i in even_list:
	        if i > result:
	        	result = i
	return result
		
				
print(function())









#my_list = [3, 5, 7, 2, 8, 4, 10]

# initialize 'largest' with -1
largest = -1

# iterate over the list
#for x in my_list:
    # check if x is even
    #if x % 2 == 0:
        # check if x is greater than largest
        #if largest < x:
           # largest = x

#if largest == -1:
   # print("No Even Number")
#else:
   # print("Largest Even Number: " + str(largest))


def function():
	result = 0

	list =[3,4,2,5,10,7,8]

	for i in list:
	        if i > result:
	        	result = i
	return result
		
				
print(function())







   

