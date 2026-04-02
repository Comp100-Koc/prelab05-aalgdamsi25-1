def add_binary(a, b):
   a=a[2:][::-1]
   b=b[2:][::-1]
   
   total_a=0
   total_b=0
   for i in range(len(b)):
       total_b+= int(b[i])*(2**(i))
   for i in range(len(a)):
       total_a+= int(a[i])*(2**(i))

   converted=''
   i=8
   total=total_a+total_b
   if total==0:
       return "0b0"
   while total!=0:
       if total<(2**i):
           converted+='0'
           i-=1
       else:
           total-=(2**i)
           if total!=0:
               i-=1
           converted+='1'
           
   if i!=0:
       for i in range(i):
           converted+='0'
           
   return '0b'+converted[converted.find('1'):]
   

