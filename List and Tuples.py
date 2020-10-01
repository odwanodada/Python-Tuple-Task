a_list = [1,2,3,4,5]
a_list.insert(0,0) #To add element whereever you want use .insert()
a_list.remove(2)#To remove item in the list
print(a_list)


a_list = [1,2,3,4,5]
del a_list[1]#to remove item by index
print(a_list)

def print_list(a_list):# a list using function
    print(a_list)
print_list(a_list)#Always call a function

####################################################################################################################
# Tuples Exercise 30/09
def tuple_exercise():
    number = int(input("How many numbers would you like to add: "))

    my_tuple = tuple()
    tmp_list = []
    while number > 0:
        num = int(input("Please enter a number(again): "))
        tmp_list.append(num)
        number -= 1
    my_tuple = tuple(tmp_list)

    print("Max: ", max(my_tuple))
    print("Sum: ", sum(my_tuple))
    print("Min: ", min(my_tuple))

    new_list = list(my_tuple)
    new_list.append(45)
    new_list.append(56)
    new_tuple = tuple(new_list)

    print("Initial tuple: ", my_tuple)
    print("New tuple: ", new_tuple)


tuple_exercise()