import json
from pathlib import Path

def combine_json_files():
    # Get the data directory
    data_dir = Path('flashcards/data')
    output_file = data_dir / 'all_cards.jsonl'
    
    total_cards = 0
    
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Process each JSON file in the data directory
        for json_file in sorted(data_dir.glob('*.json')):
            # Skip the output file itself if it exists
            if json_file.name == 'all_cards.jsonl':
                continue
                
            print(f"Processing {json_file.name}...")
            
            try:
                # Read the JSON file
                with open(json_file, 'r', encoding='utf-8') as infile:
                    cards = json.load(infile)
                    
                # Write each card as a separate line in JSONL format
                for card in cards:
                    json.dump(card, outfile, ensure_ascii=False)
                    outfile.write('\n')
                    total_cards += 1
                    
            except Exception as e:
                print(f"Error processing {json_file.name}: {str(e)}")
    
    print(f"\nTotal cards written to {output_file}: {total_cards}")

if __name__ == '__main__':
    combine_json_files() 