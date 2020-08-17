def format_address(address_string):
  # Declare variables
  house_no = ''
  street_name = ''
  new_string = ''


  # Separate the address string into parts
  new_string = address_string.split()

  # Traverse through the address parts
  for i in new_string:
    # Determine if the address part is the
    # house number or part of the street name
    if i.isnumeric():
      house_no = i
    else:
      street_name += i+' '
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_no,street_name)
  
  
'''
  Output
  
  house number 123 on street named Main Street 
  house number 1001 on street named 1st Ave 
  house number 55 on street named North Center Drive 

'''
