import os

# Function to search for folders or files based on a query
def search_folder_or_file():
    # Prompt the user to enter the search query (folder or file name)
    search_query = input("Enter the name of the folder or file to search for: ")
    # List to store found items (folders or files)
    found_items = []
    # Walk through the directory tree starting from the current directory ('.')
    for root, dirs, files in os.walk('.'):
        # Search for folders (dirs)
        for dir_name in dirs:
            # If the search query is found in the folder name (case-insensitive)
            if search_query.lower() in dir_name.lower():
                # Add the full path of the found folder to the found_items list
                found_items.append(os.path.join(root, dir_name))
        # Search for files
        for file_name in files:
            # If the search query is found in the file name (case-insensitive)
            if search_query.lower() in file_name.lower():
                # Add the full path of the found file to the found_items list
                found_items.append(os.path.join(root, file_name))
    # Output the search results
    if found_items:
        # Print the number of found items and their paths
        print(f"\n--- Found {len(found_items)} matching items ---")
        for item in found_items:
            print(item)
    else:
        # Notify the user if no items match the search query
        print(f"\nNo folders or files found matching '{search_query}'.")
