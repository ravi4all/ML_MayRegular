file = open('bahubali.jpg', 'rb')
data = file.read()
# print(data)
file.close()

file_2 = open('dhoni.jpg','rb')
data_2 = file_2.read()
file_2.close()

file = open('img_2.jpg','wb')
file.write(data)
file.write(data_2)
file.close()