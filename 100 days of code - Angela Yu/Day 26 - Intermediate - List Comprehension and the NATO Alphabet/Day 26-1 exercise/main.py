import pandas

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

# squared_numbers = [num**2 for num in numbers]
# squaring numbers
# results = [num for num in numbers if (num % 2 == 0)]
# filtering common numbers in file1 and file 2
# data_1 = pandas.read_csv("file1.txt")
# data_1_to_list = data_1.num.to_list()
# print(data_1_to_list)
#
# data_2 = pandas.read_csv("file2.txt")
# data_2_to_list = data_2.num.to_list()
# print(data_2_to_list)
with open("file1.txt") as file_1:
    file_1_data = file_1.readlines()
with open("file2.txt") as file_2:
    file_2_data = file_2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]
print(result)




#Write your code 👆 above:

# print(squared_numbers)
# print(results)


