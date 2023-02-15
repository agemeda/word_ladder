#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    stack = [] #Create a stack
    stack.append(start_word) #Push the start word onto the stack
    que = deque() #Create a queue 
    que.append(stack) #Enqueue the stack onto the queue
    
    if start_word == end_word:
        return stack

    with open(dictionary_file, 'r') as x:
        dictionary_file = [word.strip() for word in x]

    while len(que) != 0: #While the queue is not empty
        newstack = que.popleft()
        copy_dictionary = copy.copy(dictionary_file)

        for word in copy_dictionary: #For each word in the dictionary
            if _adjacent(word, newstack[-1]) is  True: #If the word is adjacent to the top of the stack
                if word == end_word: #If this word is the end word
                    ladder = newstack.append(word) #The front stack plus this word is your word ladder.
                    return ladder  #you are done!
                else:
                    stack2 = copy.copy(newstack) #Make a copy of the stack
                    stack2.append(word) #Push the found word onto the copy
                    que.append(stack2) #Enqueue the copy
                    dictionary_file.remove(word) #Delete word from the dictionary
    return None

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    x = True

    while x == True:
        for i in ladder:
            i = 0
            if _adjacent(ladder[i], ladder[i+1]) == True:
                i += 1
            else:
                x = False
    return x

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    stop = 0
    for i in  range(len(word)):
        if word1[i] != word2[i]:
            stop += 1
    if stop > 1:
        return False
    else:
        return True
