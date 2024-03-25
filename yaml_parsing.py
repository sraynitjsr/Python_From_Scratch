import yaml

# Define YAML content as a multiline string
yaml_content = """
team:
  name: "Indian Cricket Team"
  captain: "Virat Kohli"
  vice_captain: "Rohit Sharma"
  players:
    - name: "Virat Kohli"
      role: "Batsman"
      age: 33
    - name: "Rohit Sharma"
      role: "Batsman"
      age: 34
    - name: "Jasprit Bumrah"
      role: "Bowler"
      age: 28
    - name: "Ravindra Jadeja"
      role: "All-rounder"
      age: 33
"""

# Load the YAML content
data = yaml.safe_load(yaml_content)

# Accessing the parsed data
team_name = data["team"]["name"]
captain = data["team"]["captain"]
vice_captain = data["team"]["vice_captain"]
players = data["team"]["players"]

print("Team Name:", team_name)
print("Captain:", captain)
print("Vice Captain:", vice_captain)
print("\nPlayers:")
for player in players:
    print("Name:", player["name"])
    print("Role:", player["role"])
    print("Age:", player["age"])
    print()
