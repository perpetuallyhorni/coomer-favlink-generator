import json
import os
import glob

def find_json_file():
    json_files = glob.glob('response_*.json')
    if len(json_files) == 0:
        return input("No 'response_*.json' files found. Please enter the path to the desired file: ")
    elif len(json_files) == 1:
        return json_files[0]
    else:
        print("Multiple 'response_*.json' files found:")
        for i, file in enumerate(json_files):
            print(f"{i + 1}: {file}")
        file_index = int(input("Enter the number of the file you want to use: ")) - 1
        return json_files[file_index]

def generate_links(file_path):
    # Open the JSON file and load its content
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Initialize an empty list to store the generated links
    links = []
    
    # Iterate through each item in the JSON data
    for item in data:
        # Check the service type and generate the appropriate link
        if item['service'] == 'onlyfans':
            link = f"https://coomer.su/onlyfans/user/{item['name']}"
        elif item['service'] == 'fansly':
            link = f"https://coomer.su/fansly/user/{item['id']}"
        # Adding candfans profiles to favorites doesn't even work in coomer but whatever
        elif item['service'] == 'fansly':
            link = f"https://coomer.su/candfans/user/{item['id']}"
        else:
            continue
        
        links.append(link)
    
    return links

def main():
    file_path = find_json_file()
    links = generate_links(file_path)
    with open('coomer_links.txt', 'w') as output_file:
        for link in links:
            output_file.write(link + '\n')

if __name__ == "__main__":
    main()

    