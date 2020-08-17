def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  list_2 = []
  # reversing content of list1
  i = len(list1)-1
  while(i != -1):
    list_2.append(list1[i])
    i -= 1
    #adding and returning
  return list2+list_2


  # Followed by the elements of list1 in reverse order
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
