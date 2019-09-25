imei=input()[:15]
if len(imei)<15:
  print("Please enter a valid IMEI")
else:
  n=0
  do=[]
  si=[]
  temp=0
  temp1=0
  temptot=0
  for i in imei.split():

    if i.isdigit():
      for j in range(len(i)-1,0,-2):
        #print("j",int(imei[j]))
        n=int(imei[j])*2
        print("n",n)
        do.append(n)
        print("first do",do)
      for k in range(0,len(i)-1,2):
        o=imei(k)
        si.append(o)
  print("si",si)
  for i in (do):

    if i>9:
      print("i",i)
      k=do.index(i)
   
      temp=i%10
    
      i=i//10
    
      temp1=i
    
      temptot=temp+temp1
    
      do[k]=temptot
  print("do",do)
  vali=sum(do)
  vali1=sum(si)
  kal=vali+vali1
  print(kal)
  if kal%10==0:
    print("Valid one!")
  else:
    print("OOPS, Not a valid one!")












  
  

