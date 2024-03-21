import subprocess
import os

# Array of new scene names
scenes = ["Auditorium", "Ballroom", "Barn", "Caterpillar", "Church", "Courthouse", "Courtroom", "Family", "Francis", "Horse", "Ignatius", "Lighthouse", "M60", "Meetingroom", "Museum", "Palace", "Panther", "Playground", "Temple", "Train", "Truck"]

# Loop over each scene and run the conversion command
for scene in scenes:
    print(f"Processing {scene}...")
    source_dir = os.path.join("./tanks_and_temples", scene)
    # Ensure the convert.py script is executable and located in the current directory or in the PATH
    subprocess.run(["python", "convert.py", "-s", source_dir, "--resize"], check=True)

print("All scenes processed.")
