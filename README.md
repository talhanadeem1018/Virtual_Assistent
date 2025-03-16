# Jerry - Voice Assistant with Games

**Jerry** is a Python-based voice assistant designed to assist users with various tasks, such as web searches, playing music, sending messages, and providing time/date information. Additionally, it includes two built-in games: Snake and Tic-Tac-Toe. The assistant features a graphical user interface (GUI) with Siri-like animations and voice interaction.

This project integrates several Python libraries for voice recognition, web browsing, and game development, along with HTML, CSS, and JavaScript for the GUI.

---

## Features

### Voice Assistant (Jerry)
- **Voice Commands**: Recognizes and processes voice inputs using Google's speech recognition API.
- **Web Searches**:
  - Search on Google or YouTube.
  - Open specific websites like Google and YouTube.
- **Media Playback**:
  - Play songs on YouTube using voice commands.
- **Messaging**:
  - Send WhatsApp messages to predefined contacts.
- **Time and Date**:
  - Provide the current time and date.
- **Wikipedia Search**:
  - Fetch and read summaries from Wikipedia based on user queries.
- **Built-in Applications**:
  - Open a web-based calculator.
  - Launch Snake and Tic-Tac-Toe games.

### Games
- **Snake Game**:
  - A classic Snake game implemented using Tkinter.
  - Control the snake using arrow keys to eat food and grow.
  - Game over on collision with the snake's body.
- **Tic-Tac-Toe**:
  - A two-player game (human vs. computer) implemented using Tkinter.
  - The computer makes random moves.
  - Displays win/draw messages and allows game reset.

### GUI
- **Siri-Like Interface**:
  - Animated Siri wave visualization using the `siriwave` JavaScript library.
  - Text animations for welcome messages using `textillate`.
- **Responsive Design**:
  - Built with Bootstrap for a clean and responsive layout.
  - Black background with centered content for an immersive experience.

---

## Technologies Used

### Backend
- **Python Libraries**:
  - `pyttsx3`: Text-to-speech conversion.
  - `speech_recognition`: Voice input recognition.
  - `wikipedia`: Fetch Wikipedia summaries.
  - `webbrowser`: Open web URLs.
  - `pywhatkit`: Play YouTube videos and send WhatsApp messages.
  - `tkinter`: GUI for games (Snake and Tic-Tac-Toe).
  - `subprocess`: Launch external Python scripts (games).

### Frontend
- **HTML/CSS**:
  - Bootstrap for responsive design.
  - Custom CSS for styling (black background, centered content).
- **JavaScript**:
  - `siriwave`: Siri-like wave animation.
  - `textillate`: Text animation for welcome messages.
  - jQuery for DOM manipulation.

---

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system.
- A working microphone for voice input.
- Internet connection for web searches and messaging.
- A local server (e.g., Live Server in VS Code) to run the GUI.

### Installation
1. **Clone or Download the Project**:
   - Clone the repository or download the project files to your local machine.

2. **Install Python Dependencies**:
   - Open a terminal in the project directory and run:
