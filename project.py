import re
def main():
    text = input("Text: ")
    words = count_words(text)
    chars = count_chars(text)
    sentences = count_sentences(text)
    common_words = most_common_words(text,3)
    palindromes = find_palindromes(text)
    print("Words:",words)
    print("Characters:",chars)
    print("Sentences:",sentences)
    print("Average word length:", int(chars/words))
    print("Top 3 common words")
    for i,(word, frequency) in enumerate(common_words,1):
        percentage = (frequency / words) * 100
        print("{}. {} - {} and makes up for {:.2f}% of the text".format(i, word, frequency, percentage))
    print("Palindrome words found in the text:")
    for i,palindrome in enumerate(palindromes,1):
        print("{}. {}".format(i,palindrome))



def count_words(text):
    #splits whenever there is a space
    words = text.split()
    return len(words)

def count_chars(text):
    #Shows the size of text
    return len(text)

def count_sentences(text):
    #I used regular expressions to apply many split factors on my split function
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s', text)

    return len(sentences)

def most_common_words(text,num):
    #Split text in words
    words = re.findall(r'\b\w+\b', text)
    #Dictionary to store words
    freq_words = {}

    #Store words in dictionary
    for word in words:
        if word.upper() in freq_words:
            freq_words[word.upper()] += 1
        else:
            freq_words[word.upper()] = 1

    #sort the dictionary in descending order based on Value
    sorted_dict = sorted(freq_words.items(),key=lambda x:x[1], reverse = True)

    #slice the list and get only the first 3 variables
    most_common = sorted_dict[:num]

    return most_common

def find_palindromes(text):
    words = re.findall(r'\b\w+\b',text)
    palindromes = [word for word in words if word.lower() == word.lower()[::-1]]

    return palindromes







if __name__ == "__main__":
    main()