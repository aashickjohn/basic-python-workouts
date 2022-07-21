# 1. question do factorial using lambda function
x = lambda x,y : x+y
x(5,10)

x = lambda x : x*x
x(5)


# 2. question reverse only alphabets not special characters
# str1="a@bc%d" do string reverse without changing special characters
# str1="d@cb%a" #expected output

# str1="a@bc%d"

# print('postion : ',str1.find('@'))
# print(dir(str))

# str2 = ''
# for i in str1[::-1]:
#     if i.isalpha():
#         print('if :',i)
#         str2 += i
#     else:
#         print('else : ',i)
# print(f'str2 : {str2}')


# 3. question take out nested dictionary values and make as list and sum the list.
# x={"s1":{"p1":42, "p2":90, "p3":"absent"},
#   "s2":{"p1":32, "p2":100, "p3":40},
#   "s3":{"p1":82, "p2":100, "p3":100}}
  
# Expected Result
# [42, 90, 'absent']
# 132
# [32, 100, 40]
# 172
# [82, 100, 100]
# 282

# for k in x.keys():
#     print(f"key : {k}")
#     li = []
#     for k, v in x[k].items():
#         print(f"key : {k}, value : {v}")
#         li.append(v)
#     print(f'Final list : {sum([x for x in li if type(x) == int])}')

# 4. question add 2 list and sort
# l1=[2,7,9,0] 
# l2=[5,8,2,6] 
# # final_list = [0 , 2 , 2, 5 , 6 , 7 , 8 , 9]

# fin_lis = l1 + l2

# print(fin_lis)
# fin_lis.sort()
# print(f'Final list : {fin_lis}')