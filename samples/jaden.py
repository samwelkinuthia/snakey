def jaden(sentence):
    return ' '.join(i.capitalize() for i in sentence.split())

# for user input scenario
    # sentence = input("enter a sentence: ")
    # print(jaden(sentence))

#test scenario
    # print(jaden("Why does round pizza come in a square box?"))