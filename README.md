# Book Title Generator

This is a Streamlit-based application that generates a book title based on your idea in English and your preferred language using the Groq API. 

## Features

- User-friendly interface to input your idea and language.
- Generates creative and unique book titles in the specified language using AI.
- Simple and responsive design powered by Streamlit.

## How It Works

1. **Input**: Provide your idea in both English and your preferred language.
2. **Language Selection**: Specify the language in which you want the book title generated.
3. **Title Generation**: The app uses the Groq API to generate a suitable book title.

## Getting Started

### Prerequisites

- Python 3.7+
- [Groq API Key](https://console.groq.com/keys)

### Installation

1. Clone the repository:

  - git clone https://github.com/your-username/book-title-generator.git
   - cd book-title-generator
   
2. Install the required dependencies:

   pip install -r requirements.txt

3. Set up your Groq API key:

   Create a .env file in the root directory:
   Add your API key to the .env file:

      GROQ_API_KEY=your_groq_api_key_here

4. Running the Application

    streamlit run app.py

5. Open your browser and go to http://localhost:8501 to access the application.
================================================================================================
## Usage

Enter your idea in the text area (in both English and your specified language).
Specify the language in which you want the book title.
Click "Generate Book Title" and get your creative book title in seconds!

## Example
Input Idea: "A mystery novel about finding hidden treasures."
Language: "Spanish"
Generated Title: "El Misterio de los Tesoros Ocultos"

## Project Structure

book-title-generator/
│
├── app.py               # The main application code
├── .env                 # Environment file storing the API key
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

## Built With

Streamlit - The framework used for building the user interface.
Groq API - The AI service for generating book titles.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments
Special thanks to the Streamlit and Groq teams for their awesome tools.

This file provides clear and comprehensive instructions for setting up, running, and contributing to the project. The project structure and example usage are also included for better understanding.






