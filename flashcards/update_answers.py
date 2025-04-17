import json
from pathlib import Path

def update_json_files():
    data_dir = Path(__file__).parent / "data"
    
    # Process all JSON files in the data directory
    for json_file in data_dir.glob("*.json"):
        if json_file.name == "all_cards.jsonl":
            continue
            
        print(f"Processing {json_file.name}...")
        
        try:
            # Read the JSON file
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Update all answers to "answer"
            if isinstance(data, list):
                for card in data:
                    if isinstance(card, dict) and 'answer' in card:
                        card['answer'] = "answer"
            
            # Write the updated data back to the file
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            print(f"Successfully updated {json_file.name}")
            
        except Exception as e:
            print(f"Error processing {json_file.name}: {str(e)}")

if __name__ == "__main__":
    update_json_files() 