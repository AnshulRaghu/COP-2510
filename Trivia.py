from Questions import Quiz

def get_questions():
    questions = []
    questions.append(Quiz('How many days are in a lunar year?', '354', '365', '243', '379', 1))
    questions.append(Quiz('What is the largest planet?', 'Mars', 'Jupiter', 'Earth', 'Pluto', 2))
    questions.append(Quiz('What is the largest kind of whale?', 'Orca whale', 'Humpback whale', 'Beluga whale', 'Blue whale', 4))
    questions.append(Quiz('Which dinosaur could fly?', 'Triceratops', 'Tyrannosaurus Rex', 'Pterandon', 'Diplodocus', 3))
    questions.append(Quiz('Which of these Winnie the Pooh characters is a donkey?', 'Pooh', 'Eeyore', 'Piglet', 'Kanga', 2))
    questions.append(Quiz('What is the hottest planet?', 'Mars', 'Pluto', 'Earth', 'Venus', 4))
    questions.append(Quiz('Which dinosaur had the largest brain compared to body size?', 'Troodon', 'Stegosaurus', 'Ichthysaurus', 'Giganoraptor', 1))
    questions.append(Quiz('What is the largest type of penguin?', 'Chinstrap penguins', 'Macaroni penguins', 'Emperor penguins', 'White-flippered penguins', 3))
    questions.append(Quiz('Which children\'s story character is a monkey?', 'Winnie the Pooh', 'Curious George', 'Horton', 'Goofy', 2))
    questions.append(Quiz('How long is a year on Mars?', '550 Earth days', '498 Earth days', '126 Earth days', '687 Earth days', 4))

    return questions