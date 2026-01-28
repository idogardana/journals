import os
from datetime import datetime

BASE_PATH = "journals"

def ensure_folder():
    # Verifies that the base journal directory exists
    try:
        if not os.path.exists(BASE_PATH):     
            os.makedirs(BASE_PATH)
            print(f"Successfully created: {BASE_PATH}")
    except Exception as e:
        print(f"Error in creating base folder: {e}")

def list_journals():
    # Returns a list of all existing journal folders
    try:
        ensure_folder()
        return [d for d in os.listdir(BASE_PATH) if os.path.isdir(os.path.join(BASE_PATH, d))]
    except Exception as e:
        print(f"Error listing journals: {e}")
        return []

def count_entries(journal_name):
    # Counts how many .txt files are in a journal
    return len(list_entries(journal_name))

def create_journal(journal_name):
    try:
        journal_path = os.path.join(BASE_PATH, journal_name)
       
        if os.path.exists(journal_path):
             print(f"The journal '{journal_name}' already exists.")
             return False
      
        # FIX: We use journal_path so it is created inside the 'journals' folder
        os.makedirs(journal_path) 
        print(f"The journal '{journal_name}' has been created.")
        return True
    
    except Exception as e:
        print(f"Error creating the journal: {e}")
        return False

def create_entry(journal_name, title, content):
    # This function creates a new journal entry with a timestamp header.
    try:
        journal_path = os.path.join(BASE_PATH, journal_name)
        if not os.path.exists(journal_path):
            return False
            
        filename = f"{title}.txt"
        file_path = os.path.join(journal_path, filename)
        
        # gets the current time and formats it
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # format the content like a real journal entry
        formatted_content = f"Title: {title}\nDate: {timestamp}\n"
        formatted_content += "-" * 30 + "\n"
        formatted_content += content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
            
        return True
    except Exception as e:
        print(f"Error creating entry: {e}")
        return False
            
def list_entries(journal_name):
    # Scans a specific journal folder and returns a list of all .txt files
    try:
        journal_path = os.path.join(BASE_PATH, journal_name)
        if not os.path.exists(journal_path):
            return []
        
        entries = [f for f in os.listdir(journal_path) if f.endswith('.txt')]
        return sorted(entries)
    except Exception as e:
        print(f"Error listing entries: {e}")
        return []
    
def read_entry(journal_name, entry_filename):
    # Reads and returns the content of a specific entry
    try:
        journal_path = os.path.join(BASE_PATH, journal_name)
        file_path = os.path.join(journal_path, entry_filename)
        
        if not os.path.exists(file_path):
            return None
            
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
            
    except Exception as e:
        print(f"Error reading entry: {e}")
        return None

def delete_entry(journal_name, entry_filename):
    # Deletes a specific entry file
    try:
        journal_path = os.path.join(BASE_PATH, journal_name)
        file_path = os.path.join(journal_path, entry_filename)

        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    except Exception as e:
        print(f"Error deleting entry: {e}")
        return False

def delete_journal(journal_name):
    # Deletes an entire journal folder and its content
    try:
        journal_path = os.path.join(BASE_PATH, journal_name)
        if not os.path.exists(journal_path):
            return False

        for filename in os.listdir(journal_path):
            file_path = os.path.join(journal_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

        os.rmdir(journal_path)
        return True
    except Exception as e:
        print(f"Error deleting journal: {e}")
        return False
    
