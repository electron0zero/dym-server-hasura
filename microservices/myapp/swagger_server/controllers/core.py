from autocorrect import spell
from wordsegment import segment
from nltk import word_tokenize
import json

def segment_and_correct(payload, spelling, segmenting):
    tokens = word_tokenize(payload)

    final_tokens = []

    if (segmenting and spelling):
        segmented = segment_tokens(tokens)
        final_tokens = spell_tokens(segmented)
    elif (not segmenting and not spelling):
        print("do nothing")
        final_tokens = tokens
    elif (segment and not spelling):
        final_tokens = segment_tokens(tokens)
    elif (spelling and not segmenting):
        final_tokens = spell_tokens(tokens)

    final_text = " ".join(final_tokens)
    is_equal = is_it_equal(payload, final_text)
    return json.dumps({'dym-word': final_text, 'dym-done': not is_equal})


def segment_tokens(tokens):
    segmented_tokens = []
    for token in tokens:
        segments = segment(token)
        segmented_tokens.extend(segments)
    return segmented_tokens

def spell_tokens(tokens):
    spelled_tokens = []
    for token in tokens:
        spelled = spell(token)
        spelled_tokens.append(spelled)
    return spelled_tokens

def is_it_equal(first, second):
    try:
       return first.lower() == second.lower()
    except AttributeError:
       return first == second