# -*- coding: utf-8 -*-
import collections

# --- State Machine Definitions ---
STATE_START = 0
STATE_CONSONANT = 1
STATE_VOWEL = 2

# --- Character Type Definitions ---
TYPE_CONSONANT = 1
TYPE_VOWEL_DIACRITIC = 2
TYPE_INDEPENDENT_VOWEL = 3
TYPE_MODIFIER = 4
TYPE_COMPOUND = 5
TYPE_EXPLICIT_CONJUNCT = 6

# --- The Phonetic Rule Set ---
# The order is CRITICAL. Longer, more specific rules must come first.
RULES = collections.OrderedDict([
    # --- Modifiers (Chandrabindu, Bisorgo, etc.) ---
    ('C', 'ঁ'), ('nN', 'ঁ'),
    (':', 'ঃ'), ('H', 'ঃ'),
    ('ng', 'ং'),  # Anusvara. For the consonant 'ঙ', use 'Ng'.
    ('`', 'ৎ'),
    ('+', '্'),  # Explicit Hosonto

    # --- Juktakkhor (Conjuncts) & Folas ---
    ('kSh', 'ক্ষ'), ('jNG', 'জ্ঞ'),
    ('rf', 'র্'),  # Explicit Reph (e.g., dhorfmo -> ধর্ম)
    ('w', 'ব'),   # B-Fola (e.g., shwar -> স্বর)
    ('Z', 'য'),   # J-Fola (e.g., boZto -> ব্যস্ত)

    # --- Compound Vowels / Characters (High Priority) ---
    ('rri', 'ঋ'),
    ('hRi', 'হৃ'),  # NEW: consume 'hRi' together so hRidoy -> হৃদয়
    ('hR', 'হৃ'),   # Bengali হৃ
    ('rr', 'রি'),
    ('OU', 'ঔ'),
    # Capitalized 'oi' variants for কৈ. Lowercase 'oi' is intentionally omitted for কই.
    ('OI', 'ঐ'), ('Oi', 'ঐ'), ('oI', 'ঐ'),
    ('ee', 'ঈ'), ('oo', 'ঊ'),

    # --- Independent Vowels ---
    ('a', 'আ'), ('A', 'আ'),
    ('i', 'ই'), ('I', 'ঈ'),
    ('u', 'উ'), ('U', 'ঊ'),
    ('e', 'এ'), ('E', 'ঐ'),
    ('o', 'অ'), ('O', 'ও'),

    # --- Vowel Diacritics (Kar-chihno) ---
    ('RI', 'ৃ'),  # For all consonants other than 'h' (e.g., kRIpon -> কৃপণ)

    # --- Consonants (Aspirated) ---
    ('kh', 'খ'), ('gh', 'ঘ'),
    ('ch', 'ছ'), ('jh', 'ঝ'),
    ('Th', 'ঠ'), ('Dh', 'ঢ'),
    ('th', 'থ'), ('dh', 'ধ'),
    ('ph', 'ফ'), ('bh', 'ভ'),
    ('sh', 'শ'), ('Sh', 'ষ'),
    ('Rh', 'ঢ়'),

    # --- Basic Consonants ---
    ('k', 'ক'), ('g', 'গ'), ('Ng', 'ঙ'),
    ('c', 'চ'), ('j', 'জ'), ('NG', 'ঞ'),
    ('T', 'ট'), ('D', 'ড'), ('N', 'ণ'),
    ('t', 'ত'), ('d', 'দ'), ('n', 'ন'),
    ('p', 'প'), ('f', 'ফ'), ('b', 'ব'), ('v', 'ভ'), ('m', 'ম'),
    ('z', 'য'),
    ('y', 'য'),  # Contextually changed to 'য়' inside the function
    ('r', 'র'), ('l', 'ল'),
    ('S', 'শ'), ('s', 'স'), ('h', 'হ'),
    ('R', 'ড়'),
])

# Map rules to character types for the state machine
CHAR_TYPES = {
    'C': TYPE_MODIFIER, 'nN': TYPE_MODIFIER, ':': TYPE_MODIFIER, 'H': TYPE_MODIFIER,
    'ng': TYPE_MODIFIER, '`': TYPE_MODIFIER, '+': TYPE_MODIFIER,
    'rf': TYPE_EXPLICIT_CONJUNCT,
    'rri': TYPE_INDEPENDENT_VOWEL, 'a': TYPE_INDEPENDENT_VOWEL, 'A': TYPE_INDEPENDENT_VOWEL,
    'i': TYPE_INDEPENDENT_VOWEL, 'I': TYPE_INDEPENDENT_VOWEL, 'u': TYPE_INDEPENDENT_VOWEL,
    'U': TYPE_INDEPENDENT_VOWEL, 'e': TYPE_INDEPENDENT_VOWEL, 'E': TYPE_INDEPENDENT_VOWEL,
    'o': TYPE_INDEPENDENT_VOWEL, 'O': TYPE_INDEPENDENT_VOWEL, 'ee': TYPE_INDEPENDENT_VOWEL,
    'oo': TYPE_INDEPENDENT_VOWEL, 'OU': TYPE_INDEPENDENT_VOWEL, 'OI': TYPE_INDEPENDENT_VOWEL,
    'Oi': TYPE_INDEPENDENT_VOWEL, 'oI': TYPE_INDEPENDENT_VOWEL,
    'RI': TYPE_VOWEL_DIACRITIC,
    'hRi': TYPE_COMPOUND, 'hR': TYPE_COMPOUND, 'rr': TYPE_COMPOUND,
}

DIACRITICS = {
    'a': 'া', 'A': 'া', 'i': 'ি', 'I': 'ী', 'ee': 'ী',
    'u': 'ু', 'U': 'ূ', 'oo': 'ূ',
    'e': 'ে', 'E': 'ৈ', 'OI': 'ৈ', 'Oi': 'ৈ', 'oI': 'ৈ',
    'O': 'ো', 'OU': 'ৌ',
    'RI': 'ৃ', 'o': ''
}
HOSONTO = "্"

def transliterate_word(word):
    bengali_word = ""
    i = 0
    word_len = len(word)
    current_state = STATE_START
    while i < word_len:
        matched_key = None
        for key in RULES.keys():
            if word.startswith(key, i):
                char_type = CHAR_TYPES.get(key, TYPE_CONSONANT)
                is_valid = False
                if char_type in [TYPE_MODIFIER, TYPE_EXPLICIT_CONJUNCT]:
                    is_valid = True
                elif current_state == STATE_START:
                    is_valid = (char_type != TYPE_VOWEL_DIACRITIC)
                elif current_state == STATE_CONSONANT:
                    is_valid = True
                elif current_state == STATE_VOWEL:
                    is_valid = (char_type != TYPE_VOWEL_DIACRITIC)
                if is_valid:
                    matched_key = key
                    break
        if matched_key:
            bengali_char = RULES[matched_key]
            char_type = CHAR_TYPES.get(matched_key, TYPE_CONSONANT)

            if matched_key == 'y' and current_state == STATE_VOWEL:
                bengali_char = 'য়'

            if char_type == TYPE_MODIFIER:
                bengali_word += bengali_char

            elif char_type == TYPE_EXPLICIT_CONJUNCT:
                if current_state == STATE_CONSONANT:
                    bengali_word = bengali_word[:-1]
                bengali_word += bengali_char
                current_state = STATE_CONSONANT

            elif char_type == TYPE_VOWEL_DIACRITIC:
                bengali_word += DIACRITICS[matched_key]
                current_state = STATE_VOWEL

            elif char_type == TYPE_INDEPENDENT_VOWEL:
                if current_state == STATE_CONSONANT:
                    bengali_word += DIACRITICS.get(matched_key, '')
                else:
                    bengali_word += bengali_char
                current_state = STATE_VOWEL

            elif char_type == TYPE_COMPOUND:
                # For hRi/hR we just output the compound and treat as a vowel cluster result
                bengali_word += bengali_char
                current_state = STATE_VOWEL

            else:  # TYPE_CONSONANT
                if current_state == STATE_CONSONANT:
                    bengali_word += HOSONTO + bengali_char
                else:
                    bengali_word += bengali_char
                current_state = STATE_CONSONANT

            i += len(matched_key)
        else:
            bengali_word += word[i]
            current_state = STATE_START
            i += 1
    return bengali_word

def post_process_word(bengali_word, original_english_word):
    if (original_english_word.endswith('o') and not original_english_word.endswith('O') and len(original_english_word) > 2):
        if original_english_word[-2] == 'y':
            pass
        else:
            VOWELS = "aeiouAEIOU"
            should_add_okar = False
            if len(original_english_word) == 2 and original_english_word[0] not in VOWELS:
                should_add_okar = True
            elif len(original_english_word) > 2:
                if original_english_word[-2] not in VOWELS and original_english_word[-3] in VOWELS:
                    should_add_okar = True
            if should_add_okar and bengali_word and bengali_word[-1] not in DIACRITICS.values() and bengali_word[-1] != HOSONTO:
                bengali_word += DIACRITICS['O']
    if bengali_word.endswith(HOSONTO) and not original_english_word.endswith('+'):
        bengali_word = bengali_word[:-1]
    return bengali_word

def transliterate(input_text):
    """The main transliteration function for the library."""
    input_text = input_text.replace('.', '।')
    words = input_text.split(' ')
    result_words = []
    for word in words:
        if not word:
            continue
        transliterated = transliterate_word(word)
        final_word = post_process_word(transliterated, word)
        result_words.append(final_word)
    return ' '.join(result_words)
