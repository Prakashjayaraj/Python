text = "i am currently learning python "
# Opening the file in by using w
with open("file.txt", "w") as file:
    file.write(text)
    print("Text has been written to the file.")
    # a  mode is used to append the files
with open("file.txt","a")as file:
    file.write("will learn quickly ")
with open("file.txt") as f:
    print(f.read())
    print(f.closed)


