"""Flask application for the flashcards web app."""
from flask import Flask, render_template, jsonify, current_app
from pathlib import Path
import os
from .core.models import FlashcardDeck

app = Flask(__name__)

# Load flashcards
CARDS_PATH = Path(__file__).parent / "data" / "sample_cards.json"
VOICES_PATH = Path(__file__).parent / "voices" / "v1_0"
deck = FlashcardDeck.from_json(CARDS_PATH)

def get_available_voices():
    """Get list of available voice models."""
    voices = []
    for file in VOICES_PATH.glob("*.pt"):
        voice_id = file.stem
        # Create a display name from the voice ID
        display_name = voice_id.replace('_', ' ').title()
        voices.append({"id": voice_id, "name": display_name})
    return sorted(voices, key=lambda x: x['name'])

# Configure TTS endpoint
app.config['KOKORO_TTS_ENDPOINT'] = os.getenv('KOKORO_TTS_ENDPOINT', 'http://10.0.0.6:8880/v1/audio/speech')

@app.route('/')
def index():
    """Render the main page."""
    voices = get_available_voices()
    return render_template('index.html', 
                         tts_endpoint=app.config['KOKORO_TTS_ENDPOINT'],
                         voices=voices)

@app.route('/api/cards')
def get_cards():
    """Return all cards as JSON."""
    return jsonify([card.model_dump() for card in deck.cards])

def run_app(debug=True):
    """Run the Flask application."""
    port = int(os.getenv('FLASK_PORT', 5001))
    app.run(host='0.0.0.0', debug=debug, port=port)

if __name__ == '__main__':
    run_app() 