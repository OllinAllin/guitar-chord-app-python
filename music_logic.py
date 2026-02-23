##################################### music_logic.py #####################################
LETTERS = ["A", "B", "C", "D", "E", "F", "G"]

NOTE_TO_INDEX = {
    "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, 
    "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, 
    "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11, "Cb": 11, "B#": 0
}

MAJOR_DEGREES = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
MINOR_DEGREES = ["i", "ii°", "III", "iv", "v", "VI", "VII"]

MAJOR_QUALITIES = ["major", "minor", "minor", "major", "major", "minor", "dim"]
MINOR_QUALITIES = ["minor", "dim", "major", "minor", "minor", "major", "major"]


def spell_note(piano_index, target_letter):
    natural_index = NOTE_TO_INDEX[target_letter]
    diff = (piano_index - natural_index + 6) % 12 - 6
    
    if diff == 0: return target_letter
    if diff == 1: return target_letter + "#"
    if diff == 2: return target_letter + "##" 
    if diff == -1: return target_letter + "b"
    if diff == -2: return target_letter + "bb" 
    return target_letter 

def get_scale(user_input, mode):
    if len(user_input) > 1:
        root = user_input[0].upper() + user_input[1:].lower()
    else:
        root = user_input.upper()

    if root not in NOTE_TO_INDEX: 
        return []
    
    current_piano_idx = NOTE_TO_INDEX[root]
    current_letter_idx = LETTERS.index(root[0]) 
    major_steps = [0, 2, 2, 1, 2, 2, 2]
    minor_steps = [0, 2, 1, 2, 2, 1, 2]
    scale=[]
    
    if mode == "major":
        mode = major_steps
    else:
        mode = minor_steps

    for step in mode:
        current_piano_idx = (current_piano_idx + step) % 12
        if step > 0:
            current_letter_idx = (current_letter_idx + 1) % 7
            
        target_letter = LETTERS[current_letter_idx]
        correct_note = spell_note(current_piano_idx, target_letter)
        scale.append(correct_note)
   
    return scale

