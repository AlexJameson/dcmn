import os
import urllib.request
import json

def confirm_overwrite(file_path):
    """ Asks the user whether to overwrite a file if it already exists. """
    response = input(f"The file '{file_path}' already exists. Do you want to overwrite it? (yes/no): ")
    return response.strip().lower() in ['yes', 'y']

def download_latest_release(download_path=None):
    if download_path is None:
        download_path = os.getcwd()

    # Check if the download_path is valid
    if not os.path.exists(download_path) or not os.access(download_path, os.W_OK):
        print(f"Error: The specified path '{download_path}' does not exist or is not writable.")
        return

    api_url = f"https://api.github.com/repos/AlexJameson/software-development-dictionary-ru/releases/latest"
    try:
        with urllib.request.urlopen(api_url, timeout=10) as response:
            response_data = response.read()
            release_data = json.loads(response_data)
            download_url = None
            version = release_data.get('tag_name')

            for asset in release_data.get('assets', []):
                if asset['name'].endswith('sdd.txt'):
                    download_url = asset['browser_download_url']
                    break

            if download_url:
                local_file_path = os.path.join(download_path, 'sdd.txt')
                
                # Check if file exists and ask for overwrite confirmation
                if os.path.exists(local_file_path):
                    if not confirm_overwrite(local_file_path):
                        print("Operation aborted by the user.")
                        return
                    else:
                        print("Overwriting the file...")

                try:
                    with urllib.request.urlopen(download_url, timeout=10) as download_response:
                        with open(local_file_path, 'wb') as file:
                            file.write(download_response.read())
                        print(f"Downloaded sdd.txt from version {version} to {local_file_path}")
                except urllib.error.URLError as e:
                    print("Error: The download request timed out or failed.", e)
            else:
                print("Error: Could not find sdd.txt in the latest release.")
    except urllib.error.URLError as e:
        print("Error: The request to GitHub API timed out or failed.", e)

