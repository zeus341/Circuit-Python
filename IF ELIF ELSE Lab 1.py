# Python Lab 1 - Asking Questions - Introduction
# Last Edit Jan 30 2023
print('''When you are making a variable assignment 
you use the "=" operator.
      ''')
x = 7
print("x =",x)
x = 25
print("x =",x)
x = 42
print("x =",x)

print('''
When you are asking a question, you are
performing a comparison, and use the "==" operator.
 
The comparison operator == compares two operands 
and produces "True" if they are equal and "False" if 
they are not:
      ''')
x = 7
y = 9
z = 7
print('x =',x,'  # This is an assignment')
print('y =',y,'  # This is an assignment')
print('z =',z,'  # This is an assignment')
print("(x == z) is",x == z,'  # This is a comparison')
print("(x == y) is",x == y,'  # This is a comparison')
print("(z == y) is",z == y,'  # This is a comparison')

print('''
When asking a question, the answer is Boolean. 
Boolean means it can only be "TRUE" or "FALSE", 1 or 0.  
If you are performing a comparison or evaluation, the 
answer will be Booliean, "TRUE" or "FALSE".  With 
that answer, you can make program flow decisions.  
      ''')
x=5
y=9
print("The variable or object",x, "is type", type(x))
print("type(",y,'==',x,") is ",type(y == x))
print('type(True") is ',type(True))
print('type(Fasle") is ',type(False))

print('''
Challenge # 1
----------------------------------------------------
Can you explain?

What do the following mean?
1) Assignment: to assign a value to a int or variable that can be anything
2) Comparison: The process of comparing two different values and to determine if they are equal to eachother, less than, greater than, not equal to and such.
3) Evaluation: The part of computing to determine if values are true or false of an expression or statement.
4) What is the difference between "=" and "==": = is the assigning a value to a variable rather than '==' which is comparison of which two values each to eachother.
5) Boolean: This process is the process of evualute values and determing if its true or false if the values. If the values were to equal to eachother.
      
Hint: https://www.w3schools.com/python/python_operators.asp
---
''')
