import pymorphy3

morph = pymorphy3.MorphAnalyzer()

input_file = 'dict-a.txt'

output_file = 'test-output.txt'

# Open the output file in write mode
with open(output_file, 'w') as file_out:
    # Process each word and write the result to the common output file
    with open(input_file, 'r') as file_in:
        # Read the contents of the input file
        words = file_in.read().splitlines()
        for word in words:
            processed_word = morph.parse(word)[0]

            if processed_word.tag.POS == 'NOUN':
                nomn = processed_word.inflect({'sing', 'nomn'}).word
                file_out.write(nomn + '\n')

                gent = processed_word.inflect({'sing', 'gent'}).word
                file_out.write(gent + '\n')

                datv = processed_word.inflect({'sing', 'datv'}).word
                file_out.write(datv + '\n')

                accs = processed_word.inflect({'sing', 'accs'}).word
                file_out.write(accs + '\n')

                ablt = processed_word.inflect({'sing', 'ablt'}).word
                file_out.write(ablt + '\n')

                loct = processed_word.inflect({'sing', 'loct'}).word
                file_out.write(loct + '\n')

                plural_noun = processed_word.inflect({'plur'})

                if plural_noun:
                    plural_nomn = plural_noun.inflect({'nomn'}).word
                    file_out.write(plural_nomn + '\n')

                    plural_nomn = plural_noun.inflect({'gent'}).word
                    file_out.write(plural_nomn + '\n')

                    plural_nomn = plural_noun.inflect({'datv'}).word
                    file_out.write(plural_nomn + '\n')

                    plural_nomn = plural_noun.inflect({'accs'}).word
                    file_out.write(plural_nomn + '\n')

                    plural_nomn = plural_noun.inflect({'ablt'}).word
                    file_out.write(plural_nomn + '\n')

                    plural_nomn = plural_noun.inflect({'loct'}).word
                    file_out.write(plural_nomn + '\n')

                else:
                    file_out.write('Failed to inflect to plural')

            elif processed_word.tag.POS == 'INFN':
                # Process infinitive verbs
                file_out.write('Here is a verb - ' + processed_word.word + '\n')

            elif processed_word.tag.POS == 'ADJF':
                # Process the full-form adjectives
                file_out.write('Here is an adjective - ' + processed_word.word + '\n')

            else:
                file_out.write('Failed to parse the following word: ' + processed_word.word + '\n')
