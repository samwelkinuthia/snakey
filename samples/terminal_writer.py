def terminal_writer():
    name = input("Enter the file name: ")
    text = input("What do you want to write?: ")

    fw=open(name +".txt", "w")
    fw.write(text)
    fw.close

terminal_writer()
