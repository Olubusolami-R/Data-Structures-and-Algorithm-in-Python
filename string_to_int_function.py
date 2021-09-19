def str_to_int(input_str):
  is_negative=False

  num=0

  if input_str[0]=='-':
    is_negative= True
    input_str=input_str[1:]

  count=len(input_str)-1

  for i in range(len(input_str)):
    temp=ord(input_str[i])-48
    num+=(temp*(10**count))
    count-=1
    
  if is_negative==True:
    num=num*(-1)
  
  return num