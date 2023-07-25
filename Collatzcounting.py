while True:
 x=int(input('ENTER NO.:'))
 print ('----------------')
 while x>0:
  if x%2==0:
   x = x/2
  elif x>1:
   x = 3*x + 1
  else:
   break
   print (x)
