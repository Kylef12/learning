import math
#player_name = input()
#goals = int(input())
real_pi = math.pi

print(f'{"Player Name":16} {"Goals":8}')
print('-' * 24)

print(f'{"Sadio Mane":16}{"22":8}')
print(f'{"Gabriel Jesus":16}{"7":8}')
print(f'{"Gabriel Jesus":<16}{"7":<8}') # left aligned
print(f'{"Gabriel Jesus":>16}{"7":>8}') # right aligned
print(f'{"Gabriel Jesus":^16}{"7":^8}') #centered
print(f'{"Gabriel Jesus":16}{"7":8}') # regular fill just uses space
print(f'{"Gabriel Jesus":16}{"7":0>8}') #fill before
print(f'{"Gabriel Jesus":16}{"7":0^8}') #fill centered
print(f'{"Gabriel Jesus":16}{"7":*>8}') #anything can be used instead of the 0
print(f'{"Gabriel Jesus":16}{real_pi}')
print(f'{"Gabriel Jesus":16}{real_pi:.2f}') #can use .#f to choose length after decimal place
print(f'{"Gabriel Jesus":16}{7:.3f}') #can be used for whole numbers as well
print(f'{"Gabriel Jesus":16}{7:8.3f}') #can format with as well
#print(f'{player_name:16} {goals:8}')

air_temperature = float(input())

print(f'{air_temperature:.1f}C')

#STRING METHODS:

#replace(old, new) -- Returns a copy of the string with all occurrences of the substring old replaced by the string new. The old and new arguments may be string variables or string literals.
#replace(old, new, count) -- Same as above, except only replaces the first count occurrences of old.

phrase = 'Someday I will have three goats, six horses, and nine llamas.'
print(phrase)

phrase = phrase.replace('one', 'uno')
phrase = phrase.replace('two', 'dos')
phrase = phrase.replace('three', 'tres')
phrase = phrase.replace('four', 'cuatro')
phrase = phrase.replace('five', 'cinco')
phrase = phrase.replace('six', 'seis')
phrase = phrase.replace('seven', 'siete')
phrase = phrase.replace('eight', 'ocho')
phrase = phrase.replace('nine', 'nueve')

print('Translation:', phrase)



#find(x) -- Returns the index of the first occurrence of item x in the string, else returns -1. x may be a string variable or string literal. Recall that in a string, the index of the first character is 0, not 1. If my_str is 'Boo Hoo!':
#my_str.find('!')  # Returns 7
#my_str.find('Boo')  # Returns 0
#my_str.find('oo')  # Returns 1 (first occurrence only)

#find(x, start) -- Same as find(x), but begins the search at index start:
#my_str.find('oo', 2)  # Returns 5

#find(x, start, end) -- Same as find(x, start), but stops the search at index end - 1:
#my_str.find('oo', 2, 4)  # Returns -1 (not found)

#rfind(x) -- Same as find(x) but searches the string in reverse, returning the last occurrence in the string

#count(x) -- Returns the number of times x occurs in the string.
#my_str.count('oo')  # Returns 2

#Note that methods such as find() and rfind() are useful only for cases where a programmer needs to know the exact location of the character or substring in the string.

#If the exact position is not important, then the in membership operator should be used to check if a character or substring is contained in the string:
#if 'batman' in superhero_name:
    # Statements to execute if superhero_name contains 'batman' in any position.


my_string = 'Kyle/James/Chase/Nick/Corey/John/Matthew'
my_tokens = my_string.split('/')
print(my_tokens)