import json
import os.path

def read_words_from_json():
    if not os.path.exists('Dictionary_English.json'):
        return []

    with open('Dictionary_English.json', 'r', encoding='utf-8') as fail:
        data = json.load(fail)
        dictionary = data['Dictionary']
        list_of_words = []
        for row in dictionary:
            list_of_words.append(row["word"])

        print(f"Words in json before: {len(list_of_words)}")
        return list_of_words

def get_unique_numbers(words):
    list_of_unique_words = []
    unique_words = set(words)

    for word in unique_words:
        list_of_unique_words.append(word)

    return list_of_unique_words

def write_to_json(array):
    unique_words = get_unique_numbers(array)
    unique_words.sort()
    print(f"Words in json after: {len(unique_words)}")

    data ={}
    data['Language'] = 'English'
    data['Dictionary'] = []
    for arr in unique_words:

        data['Dictionary'].append({
                'word': arr,
                'description' : ''   
        })

    with open('Dictionary_English_New.json', 'w') as outfile:
        json.dump(data, outfile, indent=4) 
