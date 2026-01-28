import os
from utilities.utils import (
    ensure_folder,
    create_journal,
    create_entry,
    list_entries,
    read_entry,
    delete_entry,
    delete_journal,
    count_entries,
    list_journals
)

def print_header(title):
    """Prints a clear, designed header for each section."""
    print("\n" + "=" * 45)
    print(f" {title.upper():^43} ")
    print("=" * 45)

def pause():
    """Pauses the program so the user can read the error/success message."""
    input("\nPress Enter to return to the main menu...")

def display_menu():
    """Prints the main navigation menu."""
    print("\n[ DIGITAL JOURNAL - MAIN MENU ]")
    print("1) ✨ Create New Journal")
    print("2) 📂 List All Journals")
    print("3) 📝 Add New Entry")
    print("4) 📖 Read an Entry")
    print("5) 🗑️  Delete an Entry")
    print("6) 🔥 Delete Entire Journal")
    print("7) ❌ Exit")
    print("-" * 25)

def main():
    # Ensure the journals directory exists at startup
    ensure_folder()
    
    try:
        while True:
            display_menu()
            choice = input("Select an option (1-7): ").strip()

            if choice == "1":
                print_header("New Journal")
                name = input("Enter journal name: ").strip()
                if name:
                    if create_journal(name):
                        print(f"SUCCESS: Journal '{name}' created.")
                    else:
                        print(f"ERROR: Journal '{name}' already exists.")
                else:
                    print("ERROR: Journal name cannot be empty.")
                pause()

            elif choice == "2":
                print_header("Your Journals")
                journals = list_journals()
                if journals:
                    for j in journals:
                        print(f"• {j} ({count_entries(j)} entries)")
                else:
                    print("ERROR: No journals found. Please create one using option 1.")
                pause()

            elif choice == "3":
                print_header("Add Entry")
                current_journals = list_journals()
                j_name = input("Enter journal name: ").strip()
                
                if j_name not in current_journals:
                    print(f"ERROR: Journal '{j_name}' not found. You must create it first.")
                else:
                    title = input("Entry title: ").strip()
                    if not title:
                        print("ERROR: Title cannot be empty.")
                    else:
                        content = input("Write your content:\n> ")
                        if create_entry(j_name, title, content):
                            print(f"SUCCESS: Entry saved in '{j_name}'.")
                        else:
                            print("ERROR: Could not save the entry.")
                pause()

            elif choice == "4":
                print_header("Read Entry")
                j_name = input("Which journal do you want to open? ").strip()
                
                # Check if journal exists
                if j_name not in list_journals():
                    print(f"ERROR: Journal '{j_name}' does not exist.")
                else:
                    entries = list_entries(j_name)
                    # Check if journal is empty
                    if not entries:
                        print(f"ERROR: Journal '{j_name}' is empty. Nothing to read.")
                    else:
                        print("\nAvailable Entries:")
                        for i, entry in enumerate(entries, 1):
                            print(f"{i}. {entry}")
                        
                        target = input("\nEnter the filename (e.g., MyStory.txt): ").strip()
                        content = read_entry(j_name, target)
                        if content:
                            print("\n" + "~" * 45)
                            print(content)
                            print("~" * 45)
                        else:
                            print(f"ERROR: File '{target}' was not found in '{j_name}'.")
                pause()

            elif choice == "5":
                print_header("Delete Entry")
                j_name = input("Journal name: ").strip()
                if j_name not in list_journals():
                    print(f"ERROR: Journal '{j_name}' not found.")
                else:
                    entries = list_entries(j_name)
                    if not entries:
                        print(f"ERROR: Journal '{j_name}' is already empty.")
                    else:
                        for i, entry in enumerate(entries, 1):
                            print(f"{i}. {entry}")
                        target = input("Filename to delete: ").strip()
                        if delete_entry(j_name, target):
                            print(f"SUCCESS: '{target}' deleted.")
                        else:
                            print(f"ERROR: Could not find '{target}'.")
                pause()

            elif choice == "6":
                print_header("Delete Journal")
                j_name = input("Enter journal name to delete: ").strip()
                if j_name not in list_journals():
                    print(f"ERROR: Journal '{j_name}' does not exist.")
                else:
                    confirm = input(f"WARNING: Delete '{j_name}' and ALL entries? (y/n): ").lower()
                    if confirm == 'y':
                        if delete_journal(j_name):
                            print(f"SUCCESS: Journal '{j_name}' deleted.")
                        else:
                            print(f"ERROR: Failed to delete '{j_name}'.")
                    else:
                        print("CANCELLED: Journal was not deleted.")
                pause()

            elif choice == "7":
                print("\nExiting... Goodbye!")
                break
                
            else:
                print(f"ERROR: '{choice}' is an invalid option. Choose 1-7.")
                pause()

    except KeyboardInterrupt:
        print("\n\nNOTICE: Program stopped by user. Goodbye!")
    except Exception as e:
        print(f"\nCRITICAL ERROR: {e}")

if __name__ == "__main__":
    main()
    