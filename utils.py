import random
import json
import os

from settings import *

def get_frog_facts():
    with open(os.path.join(DATA_DIR, 'frogs.json')) as f:
        frog_file = json.load(f)
    fact = random.choice(frog_file['frog-facts'])
    return fact

def get_8ball_answer():
    with open(os.path.join(DATA_DIR, 'eightball.json')) as f:
        answers_file = json.load(f)
    answer = random.choice(answers_file['answers'])
    return answer

def get_sad_face():
    with open(os.path.join(DATA_DIR, 'sad.json')) as f:
        answers_file = json.load(f)
    answer = random.choice(answers_file['sad'])
    return answer


vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    # for v in vowels:
    #     if 'n{}'.format(v) in text:
    #         text = text.replace('n{}'.format(v), 'ny{}'.format(v))
    #     if 'N{}'.format(v) in text:
    #         text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))

    return text

