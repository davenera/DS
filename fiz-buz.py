inp_arr = ['hello', 'world', 'my', 'name', 'is', 'jonathan']
for word in inp_arr:
    counts = {}
    x = 1
    for letter in word:
        key = letter in counts
        if key:
            counts[letter] = x + 1
        else:
            counts[letter] = x
    if max(counts.values()) > 1:
        print(word)


i = 3

def f1():
    #hi
    "Prints 'Hello World' "
    print("Hello world")

f1()

jag = [1,2,3,4,5,56,7,8,98,90]
print(jag * 2)
print("Eastern University")
h = 'data science for all'
print(h[14:])

for x in range(1,6):
    for y in range(1,3):
        print(x + y, ",")

help(abs)