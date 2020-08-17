def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  combine_dic = guests1
  for key in guests2:
    if key in guests1:
      pass
    else:
      combine_dic[key] = guests2[key] 
  return combine_dic
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
