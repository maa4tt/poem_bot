from markovify_poems import text_model
import random


# text maker generates the lines of the poem
def text_gen(x=1):
    poetry = []
    for i in range(x):
        poetry.append(text_model.make_sentence())
    print('TXT text complete - generated')
    return (poetry)


# title maker generates the poems title
def title_gen(poem):
    try:
        words_for_title = poem[0].split()
        title = random.choice(words_for_title)
    except:
        return ""
    if len(title) > 3:
        print('TXT title complete - generated \n'
              'Poem will now be displayed below \n'
              '-------------------------------------------------------------------------------------------------------')
        return title.capitalize()
    else:
        print('TXT title complete - generated \n'
              'Poem will now be displayed below \n'
              '-------------------------------------------------------------------------------------------------------')
        return "POEM"


# print poem and write to text file
def poem_writer(file_name='poem.txt', length=random.randint(2,
                                                            5)):  # file name must be a valid txt file in tthe
    # directory of the programme the poem will be output in.
    poetry_in_motion = text_gen(length)
    title = title_gen(poetry_in_motion)
    lines = []
    poem_txt = open(f"{file_name}", 'wt')
    print(title)
    n = poem_txt.write(f'{title} \n'
                       f'\n')
    for line in poetry_in_motion:
        if line is not None:
            line += '.'
            lines.append(line)
            n = poem_txt.write(f'{line} \n')
            print(line)
    poem_txt.close()
    print(f'---------------------------------------------------------------------------------------------------------\n'
          f'TXT title/text complete output to {file_name}')
    return (title, lines)

def column_wrap(lines):  # this function should be rewritten.
    small_lines = []
    line_length = 40  # max number of characters per line. If line_len < 30 number of recursions on checks may be bad
    counter = line_length
    for line in lines:
        #print(len(line))  # this remains as a good debugging statement. Poems with very long lines have a higher
        # chance to break in the function below. The below is naive and just checks 6! residuals lines above
        # line_length*7 characters will still break! This is a bad way of doing this smarter would be a
        # recursive function
        if len(line) < line_length:
            small_lines.append(line)
            continue
        else:
            while line[counter] != ' ':  # search for the first space before line_length max.
                counter -= 1
            small_lines.append(line[
                               :counter])  # once found break up the line, append the first bit (now shorter than
            # line_length) and inspect whats left
            residual = line[
                       counter + 1:]  # adding one to the residual counter removes the space at the front. Can also
            # edit here to change formatting between lines.
            counter = line_length  # reset counter before starting again
            if len(residual) < line_length:
                small_lines.append(residual)
                counter = line_length
                continue
            else:
                while residual[counter] != ' ':
                    counter -= 1
                small_lines.append(residual[:counter])
                residual_2 = residual[
                             counter + 1:]  # adding one to the residual counter removes the space at the front. Can
                # also edit here to change formatting between lines.
                counter = line_length
                if len(residual_2) < line_length:
                    small_lines.append(residual_2)
                    counter = line_length
                    continue
                else:
                    while residual_2[counter] != ' ':
                        counter -= 1
                    small_lines.append(residual_2[:counter])
                    residual_3 = (residual_2[counter + 1:])
                    counter = line_length
                    if len(residual_3) < line_length:
                        small_lines.append(residual_3)
                        counter = line_length
                    else:
                        while residual_3[counter] != ' ':
                            counter -= 1
                        small_lines.append(residual_3[:counter])
                        residual_4 = (residual_3[counter + 1:])
                        counter = line_length
                        if len(residual_4) < line_length:
                            small_lines.append(residual_4)
                            counter = line_length
                        else:
                            while residual_4[counter] != ' ':
                                counter -= 1
                            small_lines.append(residual_4[:counter])
                            residual_5 = (residual_4[counter + 1:])
                            counter = line_length
                            if len(residual_5) < line_length:
                                small_lines.append(residual_3)
                                counter = line_length
                            else:
                                while residual_5[counter] != ' ':
                                    counter -= 1
                                small_lines.append(residual_5[:counter])
                                residual_6 = (residual_5[counter + 1:])
                                counter = line_length
                                if len(residual_6) < line_length:
                                    small_lines.append(residual_6)
                                    counter = line_length
                                else:
                                    while residual_6[counter] != ' ':
                                        counter -= 1
                                    small_lines.append(residual_6[:counter])
                                    small_lines.append(residual_6[counter + 1:])  # by residual 6 we append the fucker
                                    # without checking. I am too scared of the recursive to write properly
                                    counter = line_length
                                    continue
                        continue
    return (small_lines)

# BELOW IS PRINT TEST
# generates a random poem and saves it in poem.txt and makes an image saved as POEM.png
# poem_temp = poem_writer()
# print(poem_temp)
#
# split_poem = poem_splitter(poem_temp[1])
# print(split_poem)
# make_image.make_card(poem_temp[0], split_poem)
