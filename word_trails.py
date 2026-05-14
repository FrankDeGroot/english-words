with open('words_alpha.txt') as infile, open('word_trails.txt', 'w') as outfile:
    for line in infile:
        word = line.strip()
        if len(word) >= 3:
            outfile.write(word + '\n')
