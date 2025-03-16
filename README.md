Jerry - Voice Assistant with Games
Jerry is a Python-based voice assistant designed to assist users with various tasks, such as web searches, playing music, sending messages, and providing time/date information. Additionally, it includes two built-in games: Snake and Tic-Tac-Toe. The assistant features a graphical user interface (GUI) with Siri-like animations and voice interaction.

This project integrates several Python libraries for voice recognition, web browsing, and game development, along with HTML, CSS, and JavaScript for the GUI.

Features
Voice Assistant (Jerry)
Voice Commands: Recognizes and processes voice inputs using Google's speech recognition API.
Web Searches:
Search on Google or YouTube.
Open specific websites like Google and YouTube.
Media Playback:
Play songs on YouTube using voice commands.
Messaging:
Send WhatsApp messages to predefined contacts.
Time and Date:
Provide the current time and date.
Wikipedia Search:
Fetch and read summaries from Wikipedia based on user queries.
Built-in Applications:
Open a web-based calculator.
Launch Snake and Tic-Tac-Toe games.
Games
Snake Game:
A classic Snake game implemented using Tkinter.
Control the snake using arrow keys to eat food and grow.
Game over on collision with the snake's body.
Tic-Tac-Toe:
A two-player game (human vs. computer) implemented using Tkinter.
The computer makes random moves.
Displays win/draw messages and allows game reset.
GUI
Siri-Like Interface:
Animated Siri wave visualization using the siriwave JavaScript library.
Text animations for welcome messages using textillate.
Responsive Design:
Built with Bootstrap for a clean and responsive layout.
Black background with centered content for an immersive experience.
Technologies Used
Backend
Python Libraries:
pyttsx3: Text-to-speech conversion.
speech_recognition: Voice input recognition.
wikipedia: Fetch Wikipedia summaries.
webbrowser: Open web URLs.
pywhatkit: Play YouTube videos and send WhatsApp messages.
tkinter: GUI for games (Snake and Tic-Tac-Toe).
subprocess: Launch external Python scripts (games).
Frontend
HTML/CSS:
Bootstrap for responsive design.
Custom CSS for styling (black background, centered content).
JavaScript:
siriwave: Siri-like wave animation.
textillate: Text animation for welcome messages.
jQuery for DOM manipulation.
Setup Instructions
Prerequisites
Python 3.x installed on your system.
A working microphone for voice input.
Internet connection for web searches and messaging.
A local server (e.g., Live Server in VS Code) to run the GUI.
Installation
Clone or Download the Project:
Clone the repository or download the project files to your local machine.
Install Python Dependencies:
Open a terminal in the project directory and run:
text

Collapse

Wrap

Copy
pip install pyttsx3 speechrecognition wikipedia-api pywhatkit
Ensure Tkinter is installed (comes with Python by default).
Set Up the GUI:
Open the index.html file in a browser using a local server (e.g., Live Server in VS Code).
Alternatively, run the Python script to launch the GUI:
text

Collapse

Wrap

Copy
python controller.py
The GUI will open automatically in your default browser.
Configure WhatsApp Messaging:
Ensure the phone number (+923203533038) in controller.py is correct for sending WhatsApp messages.
Log in to WhatsApp Web on your default browser for seamless messaging.
Run Games:
The Snake and Tic-Tac-Toe games are launched via voice commands or by running their respective Python files:
text

Collapse

Wrap

Copy
python snake.py
python game.py
Usage
Running the Voice Assistant
Run the main script:
text

Collapse

Wrap

Copy
python controller.py
The GUI will open, displaying the Siri wave and welcome messages.
Jerry will greet you with a voice message (e.g., "Good Morning!").
Speak commands clearly into the microphone. Examples:
"Open YouTube"
"Play [song name]"
"Search [query] on Google"
"Send message"
"Open Snake game"
"What time is it?"
To exit, say "no" when prompted.
Playing Games
Snake Game:
Say "Open Snake game" or run snake.py.
Use arrow keys to control the snake.
Game ends on collision; restart by rerunning the script.
Tic-Tac-Toe:
Say "Open Tic-Tac-Toe game" or run game.py.
Click on the grid to make moves (X for human, O for computer).
Game resets after a win or draw.
Sample Commands
Web Searches:
"Open Google"
"Search Python tutorial on YouTube"
"Who is Elon Musk?"
Media Playback:
"Play Despacito"
Messaging:
"Send message" (sends "hello" to the predefined number).
Games:
"Open Snake game"
"Open Tic-Tac-Toe game"
Utilities:
"What time is it?"
"What is today's date?"
"Open calculator"
Limitations
Voice recognition accuracy depends on the microphone quality and background noise.
WhatsApp messaging requires an active WhatsApp Web session.
The computer's moves in Tic-Tac-Toe are random and not optimized.
Some features (e.g., Wikipedia search) require an internet connection.
The GUI must be run via a local server to load external scripts correctly.
Troubleshooting
Voice Recognition Issues:
Ensure your microphone is working and selected as the default input device.
Check for background noise and speak clearly.
WhatsApp Messaging Fails:
Verify the phone number in controller.py.
Ensure WhatsApp Web is logged in on your browser.
Games Not Launching:
Confirm Tkinter is installed and the game files (snake.py, game.py) are in the project directory.
GUI Not Loading:
Run index.html using a local server (e.g., Live Server in VS Code).
Check the browser console for errors.
Future Improvements
Add support for more voice commands and natural language processing.
Implement a smarter AI for Tic-Tac-Toe (e.g., Minimax algorithm).
Enhance the GUI with more interactive elements.
Add support for multiple languages for voice recognition.
Include more games and utility features.
License
This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

Acknowledgments
Inspired by Siri and other voice assistants.
Thanks to the open-source community for libraries like pyttsx3, speech_recognition, and siriwave.
