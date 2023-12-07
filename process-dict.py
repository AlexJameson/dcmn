import pymorphy3

morph = pymorphy3.MorphAnalyzer()

input_file = 'dict-a.txt'

output_file = 'test-output.txt'

# Grammatical number = NMbr as per OpenCorpora
numbers = ('sing', 'plur')

# Gender = GNdr as per OpenCorpora
genders = ('masc', 'femn', 'neut')

# Case = CAse as per OpenCorpora
cases = ('nomn', 'gent', 'datv', 'accs', 'ablt', 'loct')

# Verb tense = TEns as per OpenCorpora
Tenses = ('pres', 'past', 'futr')

# Verb person = PERs as per OpenCorpora
Persons = ('1per', '2per', '3per')

# Use MOod == 'impr' to conjugate verbs too

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
                # Process infinitive verbs
                file_out.write('Here is a verb - ' + processed_word.word + '\n')

            elif processed_word.tag.POS == 'ADJF':
                # Process the full-form adjectives
                file_out.write('Here is an adjective - ' + processed_word.word + '\n')

            else:
                file_out.write('Failed to parse the following word: ' + processed_word.word + '\n')
