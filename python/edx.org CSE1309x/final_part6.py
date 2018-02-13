#Write a function named "reverse_dictionary" that receives a dictionary as input argument and returns a reverse
#of the input dictionary where the values of the original dictionary are used as keys for the returned dictionary and the
#keys of the original dictionary are used as value for the returned dictionary as explained below: 

#For example, if the function is called as

#reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']})
#then your function should return
#{'precise': ['accurate', 'exact'], 'clever': ['astute', 'smart'], 'talented': ['smart'], 'bright': ['smart'], 'exact': ['accurate'], 'smart': ['astute']}
#Notes:
#The list of values in the returned dictionary is sorted in ascending order
#Capitalization does not matter. This means that all the words should be converted to lower case letters. For example the word
# "Accurate" is capitalized in the original dictionary but in the returned dictionary it is written with all lower case letters
def reverse_dictionary(input_dict):
    result = {}
    # build new keys and init with empty value
    for val in list(input_dict.keys()) :
        for vv in list(input_dict[val]):
            result[vv.lower()] = []

    # set values 
    for val in list(input_dict.keys()) :
        for vv in list(input_dict[val]):
            result[vv.lower()].append(val.lower())
    return result

print(reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}))
