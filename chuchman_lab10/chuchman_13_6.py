def text_file(words, filename):
    with open (filename, 'w') as file:
        while len(words) > 0:
            line = words[:40]
            words = words [40:]
            file.write(line + '\n')


text = "The early bird catches the worm.Don't count your chickens before they hatch.Every cloud has a silver lining.A picture is worth a thousand words.All good things must come to an end."
filename = "text_13_6"

text_file(text, filename)
