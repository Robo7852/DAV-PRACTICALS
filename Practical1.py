# 1. Given below is a dictionary having two keys ‘Boys’ and ‘Girls’ and having two lists of heights of five Boys and
# Five Girls respectively as values associated with these keys
# Original dictionary of lists:
# {'Boys': [72, 68, 70, 69, 74], 'Girls': [63, 65, 69, 62, 61]}
# From the given dictionary of lists create the following list of dictionaries:
# [{'Boys': 72, 'Girls': 63}, {'Boys': 68, 'Girls': 65}, {'Boys': 70, 'Girls': 69}, {'Boys': 69, 'Girls': 62}, {‘Boys’: 74, ‘Girls’: 61]

dic = {'Boys': [72, 68, 70, 69, 74], 'Girls': [63, 65, 69, 62, 61]}
print("Type : ", type(dic))
print("Dictionary:", dic)

l = []  # new list
key = []
temp = []
for i in dic:
    key.append(i)
    temp.append(dic[i])

print("Keys:", key)
print("Values:", temp)

for i in range(len(temp[0])):
    dic2 = {}
    k = 0
    for j in key:
        dic2[j] = temp[k][i]
        k = k+1
    l.append(dic2)
print("Output:\n", l)
