def countvowels(text):
    vowel_count={
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    for ch in text.lower():
        if ch in vowel_count:
            vowel_count[ch] +=1
    return vowel_count

sentence=input("Enter a string: ")

result=countvowels(sentence)

print("Number of vowels: ",result)
