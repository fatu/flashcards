import json
from pathlib import Path

def clean_json_files():
    # Get the data directory
    data_dir = Path('flashcards/data')
    
    total_cards = 0
    
    # Process each JSON file in the data directory
    for json_file in sorted(data_dir.glob('*.json')):
        # Skip the JSONL file if it exists
        if json_file.name == 'all_cards.jsonl':
            continue
            
        print(f"Processing {json_file.name}...")
        
        try:
            # Read the JSON file
            with open(json_file, 'r', encoding='utf-8') as infile:
                cards = json.load(infile)
            
            # Set each card's answer to empty string
            for card in cards:
                total_cards += 1
                card['answer'] = ""
            
            # Write the modified cards back to the file
            with open(json_file, 'w', encoding='utf-8') as outfile:
                json.dump(cards, outfile, ensure_ascii=False, indent=2)
                
        except Exception as e:
            print(f"Error processing {json_file.name}: {str(e)}")
    
    print(f"\nTotal cards processed: {total_cards}")

if __name__ == '__main__':
    clean_json_files() 