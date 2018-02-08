# Write a function named n_letter_dictionary that receives
# a string (words separated by spaces) as parameter and returns
# a dictionary whose keys are numbers and whose values are lists that
# contain unique words that have the number of letters equal to the keys. 

def n_letter_dictionary(my_string):
    words_count = {}
    # count words first
    words = my_string.split()
    for word in words :
        words_count[len(word)] = {}
    for word in words :
        elem = words_count[len(word)]
        elem[word.lower()] = 0;
    for ind in list(words_count.keys()) :
        elem = words_count[ind]
        v = elem.keys()
        words_count[ind] = list(v)
    return words_count



print(n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become"))
# expected
#{2: ['is'], 3: ['and', 'see', 'the', 'way', 'you'], 4: ['them', 'they', 'what'], 5: ['treat'], 6: ['become', 'people']}
