findlargest = lambda sentence: max(sentence.split(), key=len)
sentence=input()
largest=findlargest(sentence)
print("Largest word: ",largest)
