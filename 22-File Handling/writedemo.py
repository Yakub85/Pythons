f = open("sample.txt","w+")
f.write("Python is awesome.\n")
f.writelines(['Python\n','Django\n','Drf\n'])
print('Cursor is at ',f.tell())
f.seek(0)
# print('Cursor is at ',f.tell())
print(f.read())
f.close()