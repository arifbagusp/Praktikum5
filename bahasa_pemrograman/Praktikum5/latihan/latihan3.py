# tambah elemen list
my_list_a =[1, 5, 6, 8, 7]
my_list_b = my_list_a[0:2]
my_list_b.append("Hello")
my_list_b.extend([1, 2, 3])
my_list_c = my_list_a + my_list_b

print("List A =", my_list_a)
print("List B =", my_list_b)
print("List C =", my_list_c)