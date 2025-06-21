file= open('output.txt','w')
x= (input("Enter text to write to the file: "))
WRITE= file.write(x +'\n' )
print("Data succesfully written to output.txt.")
file.close()

file= open('output.txt','a')
y = (input("Enter additional text to append: "))
APPEND= file.write(y)
print("Data succesfully appended.")
file.close()

file= open('output.txt','r')
READ= file.read()
print("Final content of output.txt:")
print(READ)
file.close()


