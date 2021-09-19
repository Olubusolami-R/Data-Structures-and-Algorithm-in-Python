def is_unique(input_str):
  if(len(input_str)==1):
    return True
  d=dict()
  for i in input_str:
    if i in d:
      d[i]+=1
    else:
      d[i]=1
  for i in d:
    if d[i]!=1:
      return False
  return True
  