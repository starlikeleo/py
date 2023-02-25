#Comment
# print("Hello World!")

# print("Hello World!")

# print("Hello World!")


# #演算
# print(1+1)
# print(1-1)
# print(2*2)
# print(10/2)
# print(5*3)

# 変数
unko = 'l_size'
unko_length = 0
unko_times = 5.5

# print(unko_length + unko_times) 

# unko_shitai = False

#条件分岐と関係演算子
# if unko_length > 6:
#     print('ooi')
# elif unko_length == 0:
#     print('nai')
# else:
#     print('sukunai')

#関数
def unko_funbaru(arg):
    unko_status = arg
    
    if(unko_status < 10):
        return 'mada daijobu'
    else:
        return 'yabai'

# print()

# list
# unko_list = ['unko_small','unko_medium','unko_large']
# # print(unko_list[0])

# #for
# # for index in range(11):
# #     print(unko_funbaru(index))

# for item in unko_list:
#     print(item)

#with
#open()
with open('./unko.txt', 'r') as file:
    print(file.read())

#class



