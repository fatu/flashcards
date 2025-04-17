import pandas as pd
import json
from pathlib import Path
import os

def process_excel_file(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Get the base name of the file without extension
        file_name = Path(file_path).stem
        
        # Initialize list to store cards
        cards = []
        
        # Process each row
        for _, row in df.iterrows():
            # Skip rows where 题目 is NaN
            if pd.isna(row.get('题目', '')):
                continue
                
            question = str(row.get('题目', '')).strip()
            
            # For these files, we'll use the question as both question and answer
            # since they are already in English
            if question:  # Only add if question exists
                card = {
                    "question": question,
                    "answer": question,  # Same as question since it's already in English
                    "category": file_name  # Use filename as category
                }
                cards.append(card)
        
        # Create output directory if it doesn't exist
        output_dir = Path('flashcards/data')
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Write to JSON file
        output_file = output_dir / f"{file_name}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(cards, f, ensure_ascii=False, indent=2)
            
        print(f"Processed {file_path} -> {output_file} ({len(cards)} cards)")
        return len(cards)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return 0

def main():
    # Define the directories containing Excel files
    excel_dirs = [
        'IGB/真题1-x/英文',
        'IGB/真题2-x/英文xls',
        'IGB/真题3-x/英文xls'
    ]
    
    total_cards = 0
    
    # Process each directory
    for dir_path in excel_dirs:
        dir_path = Path(dir_path)
        if not dir_path.exists():
            print(f"Directory not found: {dir_path}")
            continue
            
        # Process each Excel file in the directory
        for file_path in dir_path.glob('*.xls'):
            cards_count = process_excel_file(file_path)
            total_cards += cards_count
    
    print(f"\nTotal cards processed: {total_cards}")

if __name__ == '__main__':
    main() 