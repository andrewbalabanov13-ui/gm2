import os
import json

folder = "offline"

# Get all HTML files in the offline folder
games = [
    filename
    for filename in os.listdir(folder)
    if filename.lower().endswith((".html", ".htm"))
]

# Sort alphabetically
games.sort()

# Generate the JavaScript
output = "const games = " + json.dumps(games, indent=4) + ";"

print(output)

# Save it to a file
with open("games.js", "w", encoding="utf-8") as f:
    f.write(output)

print(f"\nGenerated games.js with {len(games)} games.")