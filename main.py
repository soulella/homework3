# task_1
a = "immediate"


def first_and_last(a):
    x = ''.join(sorted(list(a)))
    return [x, x[::-1]]


print(first_and_last(a))

# task_2

lst = [1, 2, 3, 4, 5]
lst2 = [0,1,2,3,4]
result = 0
summa = 0
summa2 = 0
while summa < len(lst) and summa2 < len(lst2):
    a = lst[summa]
    b = lst2[summa2]
    summa += 1
    summa2 += 1
    result += a * b
print(result)
# task_3

amplify = int(input("Enter number: "))
result = []
i = 1

while i <= amplify:
    if i % 4 == 0:
        amplified_number = 10 * i
        result.append(amplified_number)
    else:
        result.append(i)
    i += 1

print("Natija:", result)

# task_4

lst = [3, 3, 3, 7, 3, 3]
sm = 0

while sm < len(lst):
    a = lst[sm]
    sm += 1
    if lst.count(a) == 1:
        print(a)

# task_5

name = ["Google", "Apple", "Microsoft"]
i = 0
while i < len(name):
    j = i + 1
    while j < len(name):
        if len(name[i]) > len(name[j]):
            name[i], name[j] = name[j], name[i]
        j += 1
    i += 1

print(name)
# task_6

letters = input("harf kriting: ")
list2 = []
list = [
    ["D", "E", "Y", "H", "A", "D"],
    ["C", "B", "Z", "Y", "J", "K"],
    ["D", "B", "C", "A", "M", "N"],
    ["F", "G", "G", "R", "S", "R"],
    ["V", "X", "H", "A", "S", "S"]
]

i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        if letters == list[i][j]:
            list2.append(list[i][j])
        j += 1
    i += 1

print(len(list2))
# task_7

num = [1, 2, 3, 4, 5, 1]


def remove_smallest(lst):
    lst.remove(min(lst))
    return lst
print(remove_smallest(lst=num))

# task_8
abc = ["aaaaaa", "ccc", "dddd", "bb"]

i = 0
while i < len(abc):
    j = i + 1
    while j < len(abc):
        if len(abc[i]) > len(abc[j]):
            abc[i], abc[j] = abc[j], abc[i]
        j += 1
    i += 1

print(abc)

# task_9


list = [0, 0, -10]
i = 0
result = 0


def find_vector(lst, index, result):
    while index < len(lst):
        x = list[index]
        result += x ** 2
        index += 1

    return int(result ** 0.5)


print(find_vector(list, i, result))

# task_10


name_dub = input("enter name:")
name = ["Della", "Ann", "Seva"]

i = 0

while i < len(name):
    x = name[i]
    i += 1
    if x == name_dub:
        name.remove(x)
        print(name)

