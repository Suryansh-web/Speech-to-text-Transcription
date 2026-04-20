import speech_recognition as sr
import os

# Initialize the recognizer
r = sr.Recognizer()

def transcribe_audio_file(file_path):
    """
    Converts a pre-recorded audio file into text.
    Optimized for 16-bit PCM WAV files with dynamic noise calibration.
    """
    # 1. Check if the file actually exists to prevent crashes
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found in this directory.")
        return

    # 2. Use the audio file as the source
    try:
        with sr.AudioFile(file_path) as source:
            print(f"Reading {file_path}... Please wait.")
            
            # --- OPTIMIZATION 1: Ambient Noise Calibration ---
            # Normalizes the noise floor to help the API distinguish silence from speech
            r.adjust_for_ambient_noise(source, duration=0.5)
            
            # --- OPTIMIZATION 2: Energy Threshold ---
            # Lowers the required audio amplitude to trigger word detection.
            # This helps catch soft consonants and trailing syllables.
            r.energy_threshold = 120
            
            # Record the full audio data from the file
            audio_data = r.record(source)
            
            # --- OPTIMIZATION 3: Language Specification ---
            # Forces the Acoustic Model to expect standard US English pronunciation
            print("Transcribing (this may take a moment)...")
            text = r.recognize_google(audio_data, language="en-US")
            
            # 4. Display and Save results
            print("\n--- Transcription Result ---")
            print(text)
            
            save_to_text_file(file_path, text)
            
    except sr.UnknownValueError:
        print("Error: Google Speech Recognition could not understand the audio. The signal-to-noise ratio might be too low.")
    except sr.RequestError as e:
        print(f"Error: Could not request results from Google Service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def save_to_text_file(original_filename, text):
    """Saves the transcription to a persistent local text file."""
    with open("transcriptions.txt", "a") as f:
        f.write(f"File: {original_filename}\n")
        f.write(f"Result: {text}\n")
        f.write("-" * 30 + "\n")
    print("\nSuccessfully logged to transcriptions.txt")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("=== Offline Speech-to-Text Transcriber ===")
    filename = input("Enter the audio filename (include extension, e.g., harvard.wav): ")
    transcribe_audio_file(filename)