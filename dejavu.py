def dejavu(word):
    seen_letters = set()
    for letter in word:
        if letter in seen_letters:
            return True
        else:
            seen_letters.add(letter)
    return False

word = str(input())

is_dejavu = dejavu(word)
if is_dejavu:
    print("dejavu")
else:
    print("unique")
