menu=['pho','com','my','bun']
# print(menu)
#
# menu.append('hu tieu')
# print(menu)
#
# for i in range (len(menu)):
#     print(i,".",menu[i],end="  ")
#     print()
# for i in menu:
#     print(i,end="  ")
#     print()
for (i,n) in enumerate (menu):
    mes="{0}.{0}. {1}".format(i+1,n)
    print(mes,end="\n")
    # print(i+1,'.',n)
