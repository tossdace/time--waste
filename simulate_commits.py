import subprocess
from datetime import datetime, timedelta

# Settings
days = 30               # How many past days to generate commits
commits_per_day = 3     # Commits per day

# Create commits
for i in range(days):
    date = datetime.now() - timedelta(days=i)
    date_str = date.strftime("%Y-%m-%dT12:00:00")  # Noon for each day
    for j in range(commits_per_day):
        # Make a small change in a file
        with open("dummy.txt", "a") as f:
            f.write(f"Commit {j+1} for {date_str}\n")
        # Stage changes
        subprocess.run(["git", "add", "."])
        # Commit with custom date
        subprocess.run(["git", "commit", "-m", f"Commit {j+1} for {date_str}", "--date", date_str])
