"""Models for the flashcards application."""
from pydantic import BaseModel, Field
from typing import List, Optional
import json
from pathlib import Path

class Flashcard(BaseModel):
    """A single flashcard with a question and answer."""
    question: str
    answer: str
    category: Optional[str] = None

class FlashcardDeck:
    """A collection of flashcards."""
    def __init__(self, cards: List[Flashcard] = None):
        self.cards = cards or []
    
    @classmethod
    def from_json(cls, file_path: str | Path) -> "FlashcardDeck":
        """Load flashcards from a JSON file."""
        path = Path(file_path)
        if not path.exists():
            return cls([])
        
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            cards = [Flashcard(**card) for card in data]
            return cls(cards)

    def to_json(self, file_path: str | Path) -> None:
        """Save flashcards to a JSON file."""
        path = Path(file_path)
        data = [card.model_dump() for card in self.cards]
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2) 