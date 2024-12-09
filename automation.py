# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///
import os
import requests
import shutil

def setup_new_day(day_number):
    day_dir = f"day{day_number}"
    test_file = f"tests/test_{day_number}.py"
    
    session_cookie = os.getenv('AOC_SESSION_COOKIE')
    if not session_cookie:
        print("Session cookie not found. Please set the AOC_SESSION_COOKIE environment variable.")
        return
    
    if not os.path.exists(day_dir):
        os.makedirs(day_dir)
        
        shutil.copy('day0/solution.py', os.path.join(day_dir, 'solution.py'))
        
        shutil.copy('day0/test_0.py', test_file)
        
        url = f"https://adventofcode.com/2024/day/{day_number}/input"
        headers = {'Cookie': f'session={session_cookie}'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            with open(os.path.join(day_dir, 'input.txt'), 'w') as f:
                f.write(response.text)
            print(f"Input for day {day_number} downloaded successfully.")
        else:
            print(f"Failed to download input for day {day_number}. Status code: {response.status_code}")
        
        print(f"Setup complete for {day_dir}")
    else:
        print(f"{day_dir} already exists")

# Example usage
setup_new_day(3)

# uv run --env-file .env automation.py