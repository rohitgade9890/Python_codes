import requests

# Correct API endpoint for your GitHub repos
url = "https://api.github.com/users/rohitgade9890/repos"

# Send HTTP GET request
response = requests.get(url)
response.raise_for_status()

# Parse JSON
repos = response.json()

# Print repo names and stars
for repo in repos:
    print(repo["name"], repo["stargazers_count"])