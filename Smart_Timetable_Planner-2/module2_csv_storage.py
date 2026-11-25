"""Module 2: CSV File Handling (Add, Edit, Delete, Load, Save)
Owner: Girish Garg (S26CSEU0213)
"""
import csv
from activity_model import make_activity
from module1_menu_validation import to_minutes, validate_day, validate_type


def load_schedule(filename="schedule.csv"):
    """Read activities from CSV into a list of Activity objects."""
    activities = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                try:
                    day = validate_day(row["day"])
                    s_min = to_minutes(row["start"])
                    e_min = to_minutes(row["end"])
                    if e_min <= s_min:
                        raise ValueError("end must be after start")
                    atype = validate_type(row["type"])
                    act = make_activity(day, row["start"], row["end"], s_min, e_min, row["title"], atype)
                    activities.append(act)
                except (ValueError, KeyError) as err:
                    print(f"Skipping invalid row: {err}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Starting with an empty schedule.")
    return activities


def save_schedule(activities, filename="schedule.csv"):
    """Save list of Activity objects back to CSV."""
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["day", "start", "end", "title", "type"])
        writer.writeheader()
        for act in activities:
            writer.writerow(act.to_dict())


def view_schedule(activities):
    """Display all scheduled activities in a clean numbered table."""
    if not activities:
        print("No activities found.")
        return
    print(f"\n{'No.':<4} {'Day':<10} {'Time':<13} {'Type':<7} {'Title':<22} {'Priority'}")
    print("-" * 78)
    for i, a in enumerate(activities, start=1):
        print(f"{i:<4} {a.day:<10} {a.start}-{a.end}  {a.type:<7} {a.title:<22} {a.get_priority()}")


def add_activity(activities, day, start, end, s_min, e_min, title, atype, filename="schedule.csv"):
    """Add a new activity and save to CSV."""
    act = make_activity(day, start, end, s_min, e_min, title, atype)
    activities.append(act)
    save_schedule(activities, filename)
    print(f"Added: {title} ({day} {start}-{end})")


def edit_activity(activities, index, day, start, end, s_min, e_min, title, atype, filename="schedule.csv"):
    """Edit an activity at 0-based index and save to CSV."""
    if 0 <= index < len(activities):
        activities[index] = make_activity(day, start, end, s_min, e_min, title, atype)
        save_schedule(activities, filename)
        print(f"Updated activity #{index + 1}.")
    else:
        print("Error: Invalid activity number.")


def delete_activity(activities, index, filename="schedule.csv"):
    """Delete an activity at 0-based index and save to CSV."""
    if 0 <= index < len(activities):
        removed = activities.pop(index)
        save_schedule(activities, filename)
        print(f"Deleted: {removed.title} ({removed.day})")
    else:
        print("Error: Invalid activity number.")
