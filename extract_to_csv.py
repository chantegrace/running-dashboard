import csv
import re

print("Extracting running workouts...")

# Open Apple Health export

file_path = "export.xml"

with open("running_workouts.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["StartDate", "EndDate", "Duration_Minutes"])

# Identify running workouts
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if 'HKWorkoutActivityTypeRunning' in line:
# Extract dates and duration
                start = re.search(r'startDate="([^"]+)"', line)
                end = re.search(r'endDate="([^"]+)"', line)
                duration = re.search(r'duration="([^"]+)"', line)
# Export results to CSV
                writer.writerow([
                    start.group(1) if start else "",
                    end.group(1) if end else "",
                    duration.group(1) if duration else ""
                ])

print("CSV created successfully!")