# Day 82: Text to Morse Code Converter

## 📌 Project Overview
A bidirectional Morse code translator that converts text to Morse code and back, with optional WAV audio file generation of the Morse signal.

## 🚀 Features
- **Encrypt**: Converts plain text → Morse code
- **Decrypt**: Converts Morse code → plain text
- **Audio Generation**: Saves the Morse code as a `.wav` file with proper dot/dash tones
- Supports letters, digits, and common punctuation

## 🛠️ How It Works
- **Dot duration**: 0.08s | **Dash**: 3× dot | **Word gap**: 7× dot
- Tone frequency: 440 Hz, Sample rate: 44100 Hz
- Audio built using NumPy sine waves and written via `scipy.io.wavfile`

## 📦 Dependencies
```
numpy
scipy
```

## ▶️ Usage
```bash
python TextToMorse.py
```
Choose:
- `1` → Enter text, get Morse output, optionally save as WAV
- `2` → Enter Morse code (space-separated, `/` for word gaps), get decoded text

## 📁 Files
| File | Description |
|------|-------------|
| `TextToMorse.py` | Main script |
| `*.wav` | Generated audio output |
