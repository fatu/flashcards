# Flashcards

A Python-based flashcards application for efficient learning, featuring Kokoro TTS for natural-sounding voice feedback.

## Features

- Interactive flashcard interface with 3D flip animation
- Text-to-Speech using Kokoro TTS API
- Keyboard shortcuts for easy navigation
- Category-based organization
- Adjustable speech speed
- JSON-based flashcard storage

## Setup

This project uses `uv` for dependency management. To get started:

1. Make sure you have `uv` installed:
```bash
pip install uv
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
uv pip install -e .
```

4. Configure Kokoro TTS endpoint:
   - Set the `KOKORO_TTS_ENDPOINT` environment variable to your Kokoro TTS FastAPI endpoint
   - Default endpoint: `http://localhost:8000/tts`

## Usage

1. Start the application:
```bash
python run.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Interact with flashcards:
   - Click or press Space to flip cards
   - Use arrow keys for navigation
   - Press 'V' to hear the question
   - Adjust speech speed as needed

## Adding Flashcards

Add or modify flashcards in `flashcards/data/sample_cards.json`:

```json
{
  "question": "Your question here",
  "answer": "Your answer here",
  "category": "Optional category"
}
```

## Environment Variables

- `KOKORO_TTS_ENDPOINT`: URL of the Kokoro TTS FastAPI endpoint
- `FLASK_ENV`: Set to `development` for debug mode
- `FLASK_PORT`: Port for the Flask application (default: 5000)

## License

MIT 