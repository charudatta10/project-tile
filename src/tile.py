from jinja2 import Environment, FileSystemLoader
import json
import random

# Load the project details from the JSON file
with open("projects.json") as f:
    projects = json.load(f)
for project in projects:
    project["color"] = random.choice(["red", "green", "blue", "yellow"])

# Configure Jinja2 environment
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.html")

# Render the template with project data
output = template.render(projects=projects)

# Write the rendered HTML to a file
with open("output.html", "w") as f:
    f.write(output)

print("HTML file generated successfully.")
