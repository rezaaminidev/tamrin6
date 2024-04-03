def word_count(sentence):

    words = sentence.split()
    
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts

sentence = "this is a test sentence is is test"
result = word_count(sentence)
items_corrected = [key for key, value in result.items() if key == "hello"]
print(items_corrected)
