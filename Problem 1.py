# Driver: Anshul Raghuvanshi           U-Number: U75799592
# Navigator: Christian Taylor          U-Number: U69656337
# This program was designed to read a file and then remove the first letter of each word, put it in the back of the word and add 'ay'.

filename = input('Enter the name of the file (with .txt extension): ')
out1 = open(filename, 'w')
out1.write('Go placidly amid the noise and the haste, and remember what peace there may be in silence. As far as possible, without surrender, be on good terms with all persons. Speak the truth quietly and clearly; and listen to others, even to the dull and the ignorant; they too have their story.\nAvoid loud and aggressive persons; they are vexatious to the spirit. If you compare yourself with others, you may become vain or bitter, for always there will be greater and lesser persons than yourself.\nEnjoy your achievements as well as your plans. Keep interested in your own career, however humble; it is a real possession in the changing fortunes of time.\nExercise caution in your business affairs, for the world is full of trickery. But let this not blind you to what virtue there is; many persons strive for high ideals, and everywhere life is full of heroism.\nBe yourself. Especially do not feign affection. Neither be cynical about love; for in the face of all aridity and disenchantment, it is as perennial as the grass.\nTake kindly the counsel of the years, gracefully surrendering the things of youth.\nNurture strength of spirit to shield you in sudden misfortune. But do not distress yourself with dark imaginings. Many fears are born of fatigue and loneliness.\nBeyond a wholesome discipline, be gentle with yourself. Therefore be at peace with God, when you perceive Him. And whatever your labors and aspirations, in the noisy confusion of life, keep peace in your soul. With all its sham, drudgery and broken dreams, it is still a beautiful world. Be cheerful. Strive to be happy.')
out1.close()

def originalToPiglatin(words):
    out1 = open(filename, 'w')
    out1 = out1.lower()
    the_words = words.split()
    for k in range(len(words)):
        i = words[k]
        words[k] = i[1:] + i[0] + 'ay'
    return ' '.join(words)

    def t(str):
        return str[0] + str[1]

    def main():
        for word in words:
            print(word[1:] + word[0] + "ay", end = " ")

    main()

originalToPiglatin()