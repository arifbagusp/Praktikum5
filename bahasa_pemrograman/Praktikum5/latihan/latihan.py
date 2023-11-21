print("Name = Arif Bagus Pramono")
print("NIM = 312310445")
print("Kelas = TI 23 A5")
print("===================================================")

my_list_a =[1, 5, 6, 8, 7]
print("my_list:", my_list_a)

# akses list
print("element ke 3 =", my_list_a[3])
print("element ke 2 sampai ke 4 =", my_list_a[2:4])
print("element terakhir =",my_list_a[-1])

# ubah elemen list
my_list_a[2] = 3
my_list_a[3:4] = [5, 4]
print("list =", my_list_a )
print("list =", my_list_a )

# tambah elemen list
my_list_b = my_list_a[0:2]
my_list_b.append("Hello")
my_list_b.extend([1, 2, 3])
my_list_c = my_list_a + my_list_b

print("List A =", my_list_a)
print("List B =", my_list_b)
print("List C =", my_list_c)