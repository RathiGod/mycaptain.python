def most_frequent(word):
    word = word.lower()
    freq = {}

    for letter in word:
        if letter not in freq.keys():
            freq[letter] = 1
        else:
            freq[letter] += 1

    freqSorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return freqSorted


word = input("Enter a string : ")
frequency_list = most_frequent(word)
for i in frequency_list:
    print(f"{i[0]}={i[1]}",end=" ")
