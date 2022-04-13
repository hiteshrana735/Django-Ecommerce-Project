# File Handling 
fp = open("file.txt", "w")
mystr = "This is some text that I want to write into the file"
str2 = ".\nThis is another line of text that we wrote inside this. \nThis file has 3 lines in total"
fp.write(mystr)
fp.write(str2)
fp.close()

fp2 = open("file.txt", "r")
# text_from_file = fp2.read(10)
line = fp2.readline()
line2 = fp2.readline()
line3 = fp2.readline()
line4 = fp2.readline()
print(line4)
fp2.close()
# print(fp2.read())


fp3 = open("file.txt", "a")
appended_text = "\nThis text is appended later on"
appended_text2 = "\nWe appended another line"
fp3.write(appended_text)
fp3.write(appended_text2)
fp3.close() 

file = open("myintro.txt", "r")
text = file.read()
print(text)
file.close()

file = open("IntroCopy.txt", "w")
file.write("COPIED DATA - \n")
file.write(text)



# To - Do list 
# 1. View Records
# 2. Add record  

# Work - 