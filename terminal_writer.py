def terminal_writer():
    print("Enter the file name")
    name=str(input())

    print("what do you want to write?")
    text=str(input())

    fw=open(name +".txt", "w")
    fw.write(text)
    fw.close

terminal_writer()
