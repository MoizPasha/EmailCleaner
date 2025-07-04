from bs4 import BeautifulSoup
import csv
import warnings

# Global settings
warnings.simplefilter("ignore")  # catch all warnings

def clean_html(file_path):
    """
    Cleans HTML content from a csv file and returns a list of cleaned text.
    
    Args:
        file_path (str): Path to the file.
        
    Returns:
        parsed_list: A list of extracted entries.
    """
    
    reader = None
    parsed_list = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            file_rows = list(reader)
    except FileNotFoundError:
        print("CSV file not found.")
    except csv.Error as e:
        print(f"CSV parsing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    for i,rows in enumerate(file_rows):
        parsed = BeautifulSoup(rows['full_body'], 'html.parser')
        title = parsed.find_all('a', style=lambda x: x and ('#5558af' in x or 'text-decoration: none' in x))
        message = parsed.find_all('div', style=lambda x: x and 'max-height:36px' in x and 'max-width:500px' in x)

        if len(title) == len(message):
            for i in range(len(title)):
                parsed_list.append({
                    'title': title[i].text.strip(),
                    'message': message[i].text.strip()
                })
    return parsed_list



if __name__ == "__main__":
    file_path = 'data.csv'  # Replace with your actual file path
    extracted = clean_html(file_path)
    print(f"Extracted {len(extracted)} entries.")
 