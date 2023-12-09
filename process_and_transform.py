import pymorphy3

morph = pymorphy3.MorphAnalyzer()

input_file = 'test-dict.txt'

output_file = 'test-output.txt'

# Grammatical number = NMbr as per OpenCorpora
numbers = ('sing', 'plur')

# Gender = GNdr as per OpenCorpora
genders = ('masc', 'femn', 'neut')

# Case = CAse as per OpenCorpora
cases = ('nomn', 'gent', 'datv', 'accs', 'ablt', 'loct')

# Verb tense = TEns as per OpenCorpora
tenses = ('pres', 'past', 'futr')

# Verb person = PERs as per OpenCorpora
persons = ('1per', '2per', '3per')

# Verb mood = MOod as per OpenCorpora
# moods = ('indc', 'impr')

# Open the output file in write mode
with open(output_file, 'w') as file_out:
    # Process each word and write the result to the common output file
    with open(input_file, 'r') as file_in:
        # Read the contents of the input file
        words = file_in.read().splitlines()
        for word in words:
            processed_word = morph.parse(word)[0]

            if processed_word.tag.POS == 'NOUN':
                if processed_word:
                    for num in numbers:
                        for case in cases:
                            noun = processed_word.inflect({num, case})
                            if noun:
                                file_out.write(noun.word + '\n')

                else:
                    file_out.write('Failed to process a noun' + processed_word.word + '\n')

            elif processed_word.tag.POS == 'INFN':
                if processed_word:
                    for num in numbers:
                        for person in persons:
                            for tense in tenses:
                                verb = processed_word.inflect({num, person, tense})
                                if verb:
                                    file_out.write(verb.word + '\n')
                                else:
                                    file_out.write('Failed to conjugate a verb ' + processed_word.word + '\n')
                else:
                    file_out.write('Failed to process a verb ' + processed_word.word + '\n')

            elif processed_word.tag.POS == 'ADJF':
                if processed_word:
                    for num in numbers:
                        for gen in genders:
                            for case in cases:
                                adjective = processed_word.inflect({num, gen, case})
                                if adjective:
                                    file_out.write(adjective.word + '\n')
                else:
                    file_out.write('Failed to process an adjective' + processed_word.word + '\n')

            else:
                file_out.write('Failed to parse the following word: ' + processed_word.word + '\n')
