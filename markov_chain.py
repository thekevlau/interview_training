from collections import defaultdict
from random import randint

def solution(input_string):
    list_of_words = input_string.split(' ')
    output_array = defaultdict(list)
    for i, v in enumerate(list_of_words):
        # how do I stop one before the end?! i can't check for its existance, since simply checking for existance of the i+1th element at the end of the list throws an error?!
        if i+1 >= len(list_of_words):
            return output_array
        output_array[v].append(list_of_words[i+1])

def randomize(word, output_array, output_string=""):
    #random_number = round(random() % len(output_array[word]))
    random_number = randint(0, len(output_array[word])-1)
    output_word = output_array[word][random_number]
    output_string = output_string + output_word + " "
    if '.' in output_word:
        return output_string
    return randomize(output_word, output_array, output_string)

word_of_interest = "the"
some_string = "In 1915, a German submarine torpedoed and sank the RMS Lusitania; 128 Americans were among the 1,198 dead. The event outraged McCay, but the newspapers of his employer William Randolph Hearst downplayed the tragedy, as Hearst was opposed to the US joining World War I. McCay was required to illustrate anti-war and anti-British editorial cartoons for Hearst's papers. In 1916, McCay rebelled against his employer's stance and began to make the self-financed, patriotic Sinking of the Lusitania on his own time. The film followed McCay's earlier successes in animation: Little Nemo (1911); How a Mosquito Operates (1912); and Gertie the Dinosaur (1914). The earlier films were drawn on rice paper, onto which backgrounds had to be laboriously traced; The Sinking of the Lusitania was the first film McCay made using the new, more efficient cell technology. McCay and his assistants spent twenty-two months making the film. His subsequent animation output suffered setbacks, as the film was not as commercially successful as his earlier efforts, and Hearst put increased pressure on McCay to devote his time to editorial drawings."
print (randomize(word_of_interest, solution(some_string)))


# mention efficiency.
# look for period. take word before it, flag it as
# set of words that could end sentences.
# O(n). just check last char of the word.

# weighting by frequency of occurances
# of the occurs five times
# of a occurs once. then 5x. tuple. cannot change length and entries, but you can change individual entries.
# two step markov chain:take two words and generate one word
#