import random
s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2="abcdefghijklmnopqrstuvwxyz"
str=raw_input("Enter your string : ")
a = [0] * 26
def ceaser( n): 
	result=''
	for i in str:
		if(i.isupper()):
			ind=(s1.find(i)+n)%26
			result=result+s1[ind]
		else:
			ind=(s2.find(i)+n)%26
			result=result+s2[ind]
	print(result)
def mono(): 
	result=''
	for i in str:
		ind=s1.find(i)
		if (a[ind]==0):
			nn=0
			flag=True
			while(flag):
				nn=random.randrange(1,26)
				if(nn in a):
					continue
				flag=False
			a[ind]=nn
		ind=(ind+a[ind])%26
		result=result+s1[ind]
	print(result)

print('Ceaser cipher output')
ceaser(3)

num=input("Enter your number : ")
print('Modified Ceaser cipher output')
ceaser(num)
print('Mono cipher output')
mono()
print(a)
