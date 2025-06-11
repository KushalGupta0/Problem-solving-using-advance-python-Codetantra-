class String:

    def __init__(self, string):
        self.string = string

    def count_uppercase(self):
        uppercase = 0
        for char in self.string:
            if char.isupper():
                uppercase += 1
        return uppercase
        
       
        
        

    def count_lowercase(self):
        lowercase = 0
        for char in self.string:
            if char.islower():
                lowercase += 1
        return lowercase

    def count_vowels(self):
        vowels = "AEIOUaeiou"
        
        vowel_count = 0
        for char in self.string:
            if char in vowels:
                vowel_count += 1
        return vowel_count

    def count_consonants(self):
        vowels = "AEIOUaeiou"
        consonants = 0
        for char in self.string:
            if char.isalpha() and char not in vowels:
                consonants += 1
        return consonants

    def count_space(self):
        spaces = 0
        for char in self.string:
            if char == " ":
                spaces += 1
        return spaces
    
s1 = String(input("Enter string: "))

print("Uppercase letters:", s1.count_uppercase())
print("Lowercase letters:",s1.count_lowercase())
print("Vowels:",s1.count_vowels())
print("Consonants",s1.count_consonants())
print("Space",s1.count_space())