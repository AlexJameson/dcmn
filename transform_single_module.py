import pymorphy3

morph = pymorphy3.MorphAnalyzer()
numbers = ('sing', 'plur')
genders = ('masc', 'femn', 'neut')
cases = ('nomn', 'gent', 'datv', 'accs', 'ablt', 'loct')
persons = ('1per', '2per', '3per')

def process_word(word, remove_duplicates=False):
    processed_word = morph.parse(word)[0]
    results_set = set() if remove_duplicates else []

    # Helper function to add results
    def add_result(result):
        if remove_duplicates:
            results_set.add(result)
        else:
            if result not in results_set:  # Mimic non-duplicate behavior without set
                results_set.append(result)

    if processed_word.tag.POS == 'NOUN':
        for num in numbers:
            for case in cases:
                noun = processed_word.inflect({num, case})
                if noun:
                    add_result(noun.word)

    elif processed_word.tag.POS == 'INFN':
        for person in persons:
            for num in numbers:
                verb = processed_word.inflect({num, person})
                if verb:
                    add_result(verb.word)

    elif processed_word.tag.POS == 'ADJF':
        for num in numbers:
            for gen in genders:
                for case in cases:
                    adjective = processed_word.inflect({num, gen, case})
                    if adjective:
                        add_result(adjective.word)

    if not results_set:
        add_result(f'Failed to process the word: {word}')
    
    return list(results_set) if remove_duplicates else results_set

# Keep the remainder of the file unchanged