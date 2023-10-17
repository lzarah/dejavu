def reverse(word):
 r=word[::-1]
 return r

def remove_non_alphabets(word):
  alphabetic_word = ""
  for char in word:
    if char.isalpha():
      alphabetic_word += char
  return alphabetic_word


word =str(input())
alphabetic_word = remove_non_alphabets(word)
alphabetic_word=reverse(alphabetic_word)
print(alphabetic_word)
