# Offline Speech-to-Text Data Pipeline

## Project Overview
An automated, offline audio transcription pipeline built in Python. This tool processes 16-bit PCM WAV files and extracts raw phonetic transcriptions utilizing the Google Web Speech API. 

This project focuses on the practical application of digital signal processing, specifically handling varying signal-to-noise ratios in acoustic environments.

## Technical Architecture
* **Audio Processing:** Utilizes the `SpeechRecognition` library to handle file I/O operations and API requests.
* **Signal Calibration:** Implements dynamic noise-floor calibration (`adjust_for_ambient_noise`) to baseline room acoustics before processing.
* **Threshold Tuning:** The energy threshold is manually tuned (`r.energy_threshold = 120`) to prevent acoustic clipping of micro-words (e.g., "the", "a") and soft trailing consonants.
* **Data Persistence:** Automatically logs successful transcription payloads to a local `.txt` file for batch review.

## Quick Start
**1. Install the required dependency:**
`pip install SpeechRecognition`

**2. Run the pipeline:**
`python speechToText.py`

*When prompted, enter the name of your `.wav` file. The system will output the API transcription to the console and log it persistently in `transcriptions.txt`.*