#Just some notes on cool features that Python has

#              ******ARITHMETIC*******
#when you divide two numbers, even if they are integers which
#divide into a whole number, the result will be a float
divide = 4 / 2 #= 2.0


#               ******LISTS*******
#when writing long numbers, you can use underscores to represent commas
long_number = 14_000_000_000
print(long_number)

#multi dimensional array
list = [1, "hello world", 2, "butt",3,4,5]
list2 = [list, 2]

#list actions
list.append(3) #add new element to the end of list
list.insert(0, 69) #insert new element to specific index(and push right elements to the right)
del list[0] #delete specific element from list(and push right elements to the left)
prev_last_element = list.pop() #pop off last element from the list and return it
popped_element = list.pop(0) #you can also specify an index to pop off from
list.remove("hello world") #remove a specific value(as opposed to a specific index)
                           #note that this removes only the first occurance of the element in the list

list3 = [3,2,1]
#print(sorted(list3)) #sorted(string str) returns a sorted version of the list
                    #and does nothing to the original
list3.sort(reverse=True) #use .sort() to permanently sort the list
                        #use .sort(reverse = True) to sort in reverse order
list3.reverse() #reverse the order of the original list
len(list3) # length of list

list4 = [1,2,3,4]
#for num in list4:
  #print(num)

#print 0 to 4
for i in range(0, 5):
  print(i)









