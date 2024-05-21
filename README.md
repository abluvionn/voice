# Voice Recognition Assistant

This project is a simple voice recognition assistant built with Python using the `speech_recognition` library. The assistant can capture voice input, convert it to text, and respond to specific commands.

## Features

- Captures voice input through the microphone.
- Converts voice input to text using Google's speech recognition service.
- Processes voice commands and responds appropriately.
- Ends the program when the user says "goodbye".

## Prerequisites

- Python 3.x
- `speech_recognition` library
- `PyAudio` library (required for microphone input)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/voice-recognition-assistant.git
    cd voice-recognition-assistant
    ```

2. **Install the required libraries:**
    ```sh
    pip install speechrecognition pyaudio
    ```

## Usage

1. **Run the program:**
    ```sh
    python voice.py
    ```

2. **Interact with the assistant:**
    - Speak clearly into the microphone.
    - Use commands like "hello", "goodbye", "how are you", "thank you", or "what is your name".

3. **End the program:**
    - Say "goodbye" to end the program.

## File Structure

- `voice.py`: The main script for the voice recognition assistant.

## Code Explanation

- **capture_voice_input()**: Captures audio input from the microphone.
- **convert_voice_to_text(audio)**: Converts the captured audio to text using Google's speech recognition service.
- **process_voice_command(text)**: Processes the recognized text and responds to specific commands.
- **main()**: The main function that runs the voice recognition loop until the user says "goodbye".

## Example

