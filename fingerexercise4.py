number = 8

counter = 1

found_cube = 0
 

while counter ** 3 <= number:
      if counter **3 == number:
          print(counter)
          found_cube = 1

          break
      else:
        counter+=1


if(found_cube  == 0):
    print("error")
   

  


   
  
