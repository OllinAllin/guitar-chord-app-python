# 🎸 Guitar Chords & Scales App

A desktop application built with Python and CustomTkinter that helps guitarists visualize musical scales and their corresponding chord shapes across any key.

![App Screenshot](screenshots/app_preview.png)

## 🌟 Key Features

- **Dynamic Scale Generation:** Supports both Major and Minor scales in every key (including sharps and flats).
- **Correct Enharmonic Spelling:** Uses a custom algorithm to ensure notes are spelled correctly according to music theory (e.g., E# instead of F in C# Major).
- **Visual Chord Diagrams:** Automatically displays guitar chord shapes for every degree of the chosen scale.
- **Modern UI:** Built with a responsive, dark-mode interface using `CustomTkinter`.

## 🛠️ Technical Highlights

As a developer, I focused on several "clean code" principles during this project:

*   **DRY (Don't Repeat Yourself):** Refactored the scale generation logic into a single, dynamic function that handles multiple modes.
*   **Separation of Concerns:** Split the project into `main.py` (UI/UX) and `music_logic.py` (Music Theory Math) to keep the codebase maintainable.
*   **Robust Asset Loading:** Implemented a fallback mechanism for missing images and used absolute pathing to ensure the app is portable across different systems.
*   **Object-Oriented Programming (OOP):** Utilized Python classes to manage the application state and UI lifecycle.

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher
- `pip install customtkinter pillow`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com
