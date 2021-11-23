def palindrom(word):
    """
    func that checks if given word is palindrome
    Aguments:
    word: provide word to check
    
    """
    new_word = ""
    
    for letter in word[::-1]:
        new_word = new_word + letter
    
    return new_word == word

print(palindrom("kajak"))
