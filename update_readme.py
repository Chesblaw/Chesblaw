import requests
import re

USERNAME = "https://github.com/Chesblaw"
TOP_N = 3
README_PATH = "README.md"

# Fetch repos sorted by stars
url = f"https://api.github.com/users/{Chesblaw}/repos?sort=stars&per_page={TOP_N}"
res = requests.get(url)
repos = res.json()

project_html = '<p align="center">\n'
for repo in repos:
    name = repo['name'].replace('-', '_')
    url = repo['html_url']
    project_html += f'  <a href="{url}" target="_blank">\n'
    project_html += f'    <img src="https://img.shields.io/badge/{name}-00ADD8?style=for-the-badge&logo=github&logoColor=white"/>\n'
    project_html += '  </a>\n'
project_html += '</p>\n\n---\n'

# Read current README
with open(README_PATH, 'r') as f:
    content = f.read()

# Replace the section between <!-- ==================== Projects ==================== --> and the next ---
new_content = re.sub(
    r'<!-- ==================== Projects ==================== -->.*?---',
    f'<!-- ==================== Projects ==================== -->\n### 🚀 Featured Projects\n{project_html}',
    content, flags=re.S
)

# Write back
with open(README_PATH, 'w') as f:
    f.write(new_content)
