import os

def last_4chars(entry):
    return entry[-4:]

entries = sorted(os.listdir('/Users/umidjonaskarov'))

file_extension = input("Enter file extension: ")

def search():
    found = False
    for entry in entries:
        if file_extension in entry:
            print("-", entry)
            print("Last 4 characters:", last_4chars(entry))
            found = True
    if not found:
        print("No files with the specified extension found.")
        search()

search()
