import markovify
import spacy
from spacy.lang.en.examples import sentences

# Get raw text as string.
with open('poems_data.txt', errors='ignore') as f:
    text = f.read()
# Naive Build the model.
# text_model = markovify.Text(text)



# building MARKOV chains


# redefine the marovify class using spacy to build better sentence structure.
nlp = spacy.load("en_core_web_sm")

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        # https://ashutoshtripathi.com/2020/04/13/parts-of-speech-tagging-and-dependency-parsing-using-spacy-nlp/
        sentence = ""
        last_word = ""
        for word in words:
            word_part_0 = (word.split("::")[0])
            word_part_1 = word.split("::")[1]
            if word_part_0 == '\n':  # 100% bodge to make it just say one thing - you love to see it
#                return sentence
                pass
            elif word_part_1 == 'PUNCT':  # this gets seriously messy with individualised exception handling....
                sentence += last_word.strip()
                last_word = word_part_0 + " "
            elif word_part_1 == 'SYM':
                sentence += last_word.strip()
                last_word = word_part_0 + " "
            elif word_part_1 == 'AUX':
                if word_part_0 == '''\'ve''':
                    sentence += last_word.strip()
                    last_word = word_part_0 + " "
                elif word_part_0 == '''\'s''':
                    sentence += last_word.strip()
                    last_word = word_part_0 + " "
                elif word_part_0 == '''\'m''':
                    sentence += last_word.strip()
                    last_word = word_part_0 + " "
                elif word_part_0 == '''\'d''':
                    sentence += last_word.strip()
                    last_word = word_part_0 + " "
                elif word_part_0 == '''ve''':
                    sentence += last_word.strip()
                    last_word = word_part_0 + " "
                else:
                    sentence += last_word
                    last_word = word_part_0 + " "
            elif word_part_1 == 'VERB':
                if word_part_0 == '''\'m''':
                    sentence += last_word.strip()
                    last_word = word_part_0 + " "
                else:
                    sentence += last_word
                    last_word = word_part_0 + " "
            elif word_part_1 == 'NOUN':
                if word_part_0 == '''%''':
                    sentence += last_word.strip()
                    last_word = word_part_0 + " "
                else:
                    sentence += last_word
                    last_word = word_part_0 + " "
            elif word_part_1 == 'PART':
                if word_part_0 == 'not':
                    sentence += last_word
                    last_word = word_part_0 + " "
                elif word_part_0 == 'to':
                    sentence += last_word
                    last_word = word_part_0 + " "
                else:
                    sentence += last_word.strip()
                    last_word = word_part_0 + " "
            else:
                sentence += last_word
                last_word = word_part_0 + " "
        return sentence


# Build the Model with fancier stuff
text_model = POSifiedText(text)