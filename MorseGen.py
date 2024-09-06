import streamlit as st

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}


# Reverse dictionary for Morse to text conversion
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def text_to_morse(txt):
    '''Function to convert text to Morse code'''
    txt = txt.upper()
    morse_list = [MORSE_CODE_DICT[letter] for letter in txt if letter in MORSE_CODE_DICT]
    return ' '.join(morse_list)


def morse_to_text(morse):
    '''Function to convert Morse code to text'''
    words = morse.split(' / ')
    decoded_words = []
    for word in words:
        decoded_word = ''.join(REVERSE_MORSE_CODE_DICT[letter] for letter in word.split() if letter in REVERSE_MORSE_CODE_DICT)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

st.title("MorseGen. 😊")
st.write("🔤Convert your text into Morse Code below:📡")

conversion_type = st.selectbox("Choose conversion type:", ["Text to Morse", "Morse to Text"])

if conversion_type == "Text to Morse":
    user_input = st.text_input("Enter the text you want to convert to Morse Code:")
    if user_input:
        morse_code = text_to_morse(user_input)
        st.success("💻⬇️ Here’s your Morse Code! 💻⬇️")
        st.code(morse_code)
        st.balloons()
else:
    user_input = st.text_input("Enter the Morse Code you want to convert to text (separate letters with spaces and words with /):")
    if user_input:
        text_output = morse_to_text(user_input)
        st.success("💻⬇️ Here’s your decoded text! 💻⬇️")
        st.code(text_output)
        st.balloons()


st.write("Thanks for using the Morse Code Converter! Have a great day! 🌟")
