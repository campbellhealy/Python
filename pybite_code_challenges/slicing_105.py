# slicing_105.py

from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""

def slice_and_dice(text: str = text) -> list:

    """
    1' strip off the whitespace at both ends. 
    2' Split the text by newline (\n).

    Loop through the lines, for each line:
        3' strip off any leading spaces,
        4' check if the first character is lowercase,
            4a' if so, split the line into words and get the last word,
            4b' strip off BOTH the trailing dot (.) and exclamation mark (!) from this last word,
        5' finally add it to the results list.
    6' Return the results list.
    """
    results = []
    last_word = []
    split_sentences = []
    text = text.lstrip()
    text = text.split('\n') #2

    for sentences in text:
        sentences = sentences.strip() #1. 3
        sentences = sentences.split()
        split_sentences.append(sentences)
    print('\n',f'Total number of sentences in the text are: {len(split_sentences)}')

    for i in range(len(split_sentences)-1):
        sentence = split_sentences[i]
        for j in range(1):
            word = sentence[j]
            if word[0].islower(): #4
                last_word.append(sentence[-1])
    print(last_word)
    for item in last_word:
        if item[-1] == '.' or item[-1] == '!': #5
            item = item[0:-1]
        results.append(item) #6
    return results


# slice_and_dice()
print(slice_and_dice(text)) # 5
print(slice_and_dice(another_text)) #6
print('Done')