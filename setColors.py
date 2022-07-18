# Write a Python program to print out a set containing
# all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = (["red", "yellow", "green"])
color_list_2 = (["red", "green", "pink", "purple"])
len1 = len(color_list_1)
len2 = len(color_list_2)
if len1 > len2:
    for i in range(len1):
        if color_list_1[i] in color_list_2:
            print(color_list_1[i])
else:
    for i in range(len2):
        if color_list_2[i] in color_list_1:
            print(color_list_2[i])
