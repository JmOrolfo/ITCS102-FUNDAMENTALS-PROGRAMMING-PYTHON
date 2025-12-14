#List Fundamentals and Iteration 

li = ['ham', 'egg', 'bacon', 'sausage']#list
li.append('hotdog')#Add
print(li)
li.pop() #remove
print(li)


for l in li:
    print(f"{l} is already in the fridge")


fname = 'Jay Lord Menk Orolfo'
for fn in fname:
    print(fn)
print("\nReversed\n")
for n in fname [::-1]:
    print(n)

