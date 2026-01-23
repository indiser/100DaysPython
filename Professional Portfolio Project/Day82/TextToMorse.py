import numpy as np
from scipy.io.wavfile import write
import os

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.',' ': '/'
}

TEXT_TO_CODE=MORSE_CODE_DICT
CODE_TO_TEXT={value:key for key,value in MORSE_CODE_DICT.items()}

DOT_DURATION=0.08
FREQUENCY=440
SAMPLE_RATE=44100

def encrypt(messege: str):
    return " ".join(TEXT_TO_CODE.get(ch.upper(),"") for ch in messege)


def decrypt(messege:str):
    decoded_words=[]
    morse_words=messege.split(" / ")
    for morse_word in morse_words:
        morse_chars=morse_word.split(" ")
        decoded_chars=[CODE_TO_TEXT.get(ch,"") for ch in morse_chars]
        decoded_words.append(" ".join(decoded_chars))
    return " ".join(decoded_words)


def generate_tone(duration):
    t=np.linspace(0,duration,int(SAMPLE_RATE * duration),False)
    tone=np.sin(FREQUENCY * t * 2 * np.pi) * 0.5
    return tone

def generate_silence(duration):
    return np.zeros(int(SAMPLE_RATE * duration))

def transmitSound(messege:str, filename:str):
    audio_sequence=[]

    dot_wave=generate_tone(DOT_DURATION)
    dash_wave=generate_tone(DOT_DURATION * 3)
    intra_char_space=generate_silence(DOT_DURATION)
    inter_char_space=generate_silence(DOT_DURATION * 3)
    word_space=generate_silence(DOT_DURATION * 7)

    for symbol in messege:
        if symbol=='.':
            audio_sequence.append(dot_wave)
            audio_sequence.append(intra_char_space)
        elif symbol=='-':
            audio_sequence.append(dash_wave)
            audio_sequence.append(intra_char_space)
        elif symbol.isspace():
            audio_sequence.append(inter_char_space)
        elif symbol=='/':
            audio_sequence.append(word_space)
    
    if audio_sequence:
        full_audio=np.concatenate(audio_sequence)
        audio=(full_audio * 32767).astype(np.int16)

        script_dir=os.path.dirname(os.path.abspath(__file__))
        file_path=os.path.join(script_dir,filename)

        write(file_path,SAMPLE_RATE,audio)
        print(f"Saved to {filename}")
    else:
        print("No Audio generated")

if __name__ == "__main__":
    print("1. Text to Morse (Encrypt)")
    print("2. Morse to Text (Decrypt)")
    
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid choice.")
        exit(1)

    if choice == 1:
        message = input("Enter Text: \n")
        encrypted_msg = encrypt(message)
        print(f"Morse: {encrypted_msg}")
        
        quest = input("Save sound? (Y/N): \n").strip().upper()
        if quest == "Y":
            fn=message.split()[0]
            transmitSound(encrypted_msg,f"{fn}.wav")
            
    elif choice == 2:
        message = input("Enter Morse Code (space separated): \n")
        print(decrypt(message))