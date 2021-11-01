####################################
# Comparison Operators
####################################
## > greater than
## < less than
## >= greater than or equal
## <= less than or equal
## == equal
## != not equal


a=100
b=200
result1= (a>b)   # test 100>200 outputs false
print (result1)

result2= (a==b)  # test 100==200 outputs false.
print (result2)

result3= (a!=b)  # test 100!=200 outputs true.
print (result3)

result4= (a < b)   # test 100<200 outputs true.
print (result4)

result5= (a <= b)   # test 100<=200 outputs true.
print (result5)

result6= (a >= b)   # test 100>=200 outputs false.
print (result6)


###############################################################
# Example: Assume variable a holds 10 and variable b holds 20
###############################################################
x = 21
y = 10

if ( x == y ):
   print("Line 1 - x is equal to y")
else:
   print("Line 1 - x is not equal to y")

if ( x != y ):
   print("Line 2 - x is not equal to y")
else:
   print("Line 2 - x is equal to y")

if ( x < y ):
   print("Line 4 - x is less than y")
else:
   print("Line 4 - x is not less than y")

if ( x > y ):
   print("Line 5 - x is greater than y")
else:
   print("Line 5 - x is not greater than y")

x = 5
y = 20
if ( x <= y ):
   print("Line 6 - x is either less than or equal to  y")
else:
   print("Line 6 - x is neither less than nor equal to  y")

if (y >= x):
   print("Line 7 - y is either greater than  or equal to x")
else:
   print("Line 7 - y is neither greater than  nor equal to x")