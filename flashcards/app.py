"""Flask application for the flashcards web app."""
from flask import Flask, render_template, jsonify, current_app, request
from pathlib import Path
import os
from .core.models import FlashcardDeck

app = Flask(__name__)

# Load flashcards
CARDS_PATH = Path(__file__).parent / "data"
VOICES_PATH = Path(__file__).parent / "voices" / "v1_0"

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
app.config['KOKORO_TTS_ENDPOINT'] = os.getenv('KOKORO_TTS_ENDPOINT', 'http://10.0.0.155:8880/v1/audio/speech')

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
    file_name = request.args.get('file', 'sample_cards.json')
    file_path = CARDS_PATH / file_name
    
    # Validate that the file exists and is within the data directory
    if not file_path.exists() or not str(file_path).startswith(str(CARDS_PATH)):
        return jsonify({"error": "Invalid file"}), 400
        
    deck = FlashcardDeck.from_json(file_path)
    return jsonify([card.model_dump() for card in deck.cards])

@app.route('/api/files')
def get_files():
    """Return all available JSON files."""
    files = []
    for file in sorted(CARDS_PATH.glob('*.json')):
        if file.name != 'all_cards.jsonl':  # Skip the JSONL file
            files.append(file.name)
    return jsonify(files)

def run_app(debug=True):
    """Run the Flask application."""
    port = int(os.getenv('FLASK_PORT', 9001))
    app.run(host='0.0.0.0', debug=debug, port=port)

if __name__ == '__main__':
    run_app() 
