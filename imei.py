imei=input()[:15]
if len(imei)<15 or len(imei)>15:
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
      for j in range(len(i)-1,-2,-2):
        #print("j",int(imei[j]))
        #print("j",j)
        n=int(imei[j])
        #print("n",n)
        do.append(n)
        #print("first do",do)
  for j in imei.split():
    if j.isdigit():
      for k in range(1,len(i)-1,2):
        #print("k",k)
        p=int(imei[k])*2
        si.append(p)
  print("si",do)
  for i in (si):
    if i>9:
     # print("i",i)
      k=si.index(i)   
      temp=i%10    
      i=i//10    
      temp1=i
      temptot=temp+temp1    
      si[k]=temptot
  print("do",si)
  vali=sum(do)
  vali1=sum(si)
  kal=vali+vali1
  print(kal)
  if kal%10==0:
    print("Valid one!")
  else:
    print("OOPS, Not a valid one!")
