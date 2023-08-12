# writer：LeBron James
a=input()
print(a)

##16进制转化
a=input()
a=int(a,16)
print(a)

#去掉空格

a=input()
print(a.strip())

#打印字符前n位
str=input()
print(str[0:10])

#替换
offer_list=['Allen','Tom']
for i in offer_list:
     print(i + ", you have passed our interview and will soon become a member of our company.")
offer_list.remove('Tom')
offer_list.append('Andy')
for j in offer_list:
    print(j + ", welcome to join us!")

 #变字符串
a = input()
print(a.split())


#生成数字列表
a=input().split(" ")
mylist=[]
for i in a:
    mylist.append(int(i))
print(mylist)