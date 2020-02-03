a=int(input())
b=int(input())
c=int(input())
if(a!=0):
	if((b**2-4*a*c)>0):
		print('roots are real')
		x1=(-b+((b**2-4*a*c)**0.5))/2*a
		x2=(-b-((b**2-4*a*c)**0.5))/2*a
		print("roots are : ",x1,x2)

	elif((b**2-4*a*c)==0):
		print('roots are equal')
		x1=(-b+((b**2-4*a*c)**0.5))/2*a
		print("roots are :",x1)

    else:
		print('roots are imaginary')
		x1=(-b+((b**2-4*a*c)**0.5))/2*a
		x2=(-b-((b**2-4*a*c)**0.5))/2*a
		print("roots are : ",x1,x2)
else:
	print("roots do not exist")

