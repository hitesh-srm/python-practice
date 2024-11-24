# # Define two input lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]

# # Use a lambda function with map to perform addition
# result_list = list(map(lambda x, y: x + y, list1, list2))

# # Display the result
# print("List 1:", list1)
# print("List 2:", list2)
# print("Resultant List (Sum):", result_list)



x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

a = [10, 20, 30, 40]

res = 0

for val in a:

    res += val

print(res)