# Driver: Anshul Raghuvanshi (U69656337), Navigator: Christian Taylor (U75799592)
# This program is intended to convert a user-entered sentence to morse code using the tuple.

x = input('Enter a sentence to be converted to morse code: ')
x = x.upper()

code = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'), ('G', '--.'),
         ('H', '. ...'), ('I', '. .'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'),
         ('O', '---'), ('P', '.---.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'), ('Z', '--..'), ('0', '-----'),
         ('1', '.----'), ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'),
         ('7', '--...'), ('8', '---..'), ('9', '----.'), (' ', ' '), (',', '--..--'), ('.', '.-.-.-'), ('?', '..--..')]

my_str = ''
for character in x:
    my_str += character + ''
    if x[0][0] == code[0][1]:
        print(my_str)
    else:
        print('no')