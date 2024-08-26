import os
import pymorphy3

morph = pymorphy3.MorphAnalyzer()

# Grammatical number = NMbr as per OpenCorpora
numbers = ('sing', 'plur')

# Gender = GNdr as per OpenCorpora
genders = ('masc', 'femn', 'neut')

# Case = CAse as per OpenCorpora
cases = ('nomn', 'gent', 'datv', 'accs', 'ablt', 'loct')

# Verb tense = TEns as per OpenCorpora
# tenses = ('pres', 'past', 'futr')

# Verb person = PERs as per OpenCorpora
persons = ('1per', '2per', '3per')

# Verb mood = MOod as per OpenCorpora
# moods = ('indc', 'impr')

def process_and_transform(input_file_path, output_file_path):

    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: Input file at '{input_file_path}' does not exist.")
        return

    # Optionally, you could also check for output file path issues like non-writable directories
    output_dir = os.path.dirname(output_file_path)
    if output_dir and not os.path.exists(output_dir):
        print(f"Error: Output directory '{output_dir}' does not exist.")
        return
    if output_dir and not os.access(output_dir, os.W_OK):
        print(f"Error: Output directory '{output_dir}' is not writable.")
        return

    # If output file exists, decide if overwrite is allowed or a warning should be given
    if os.path.exists(output_file_path):
        # If not wanting to overwrite automatically, prompt or log a message
        print(f"Warning: Output file '{output_file_path}' already exists and will be overwritten.")
        
    # Proceed with file processing and writing to output
    # Place here your actual processing logic
    print(f"Processing {input_file_path} and saving results to {output_file_path}")


    # Open the output file in write mode
    with open(output_file_path, 'w') as file_out:
        # Process each word and write the result to the common output file
        with open(input_file_path, 'r') as file_in:
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
                        file_out.write(processed_word.word + '\n')
                        for person in persons:
                            for num in numbers:
                                verb = processed_word.inflect({num, person})
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

