

 # abcdef

  


my_str = "abcdefg"
result = ""
for char in my_str:
    if  my_str.index(char) % 2 == 0:
        result += char

print(result)
 