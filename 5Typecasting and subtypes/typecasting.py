# name = "radhe"
# print(type(name))
# age  = 23 
# print(type(age))

# a = 1
# b = 2.3
# c = a + b
# # now see a is integer and b is float so now if we print c , then python automatic gives value in float ,
# # this called implicit typecasting .
# print(c)
# print(type(c))


# sometimes python dont do implicit typecasting so we need to do explicitly suppose, 

a = "123"    # a is string 123 
print(type(a))
a = int(a)   # similarly we can convert this into any of datatype . 
print("after conversion",type(a)) 
b = 2.3
c = int(a) + b
# or we can do a = int(a)
print(c)