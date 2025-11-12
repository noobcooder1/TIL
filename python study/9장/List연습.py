prac = [1, 2, 3, 4, 5, 6]
prac2 = ["a", "b", "c", "d", "e"]

prac.remove(5)
prac2.remove("c")
prac2.append("c")
prac2.insert(2, 'd')

for item in prac2 :
    print(item)