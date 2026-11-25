"""Module 1: Menu, Input Handling and Validation
Owner: Bhavya Garg (S26CSEU0214)
"""

VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
VALID_TYPES = ["class", "lab", "study"]


def to_minutes(t):
    """Convert 'HH:MM' to minutes since midnight. Raises ValueError if invalid."""
    parts = t.strip().split(":")
    if len(parts) != 2:
        raise ValueError("time must be in HH:MM format")
    h, m = int(parts[0]), int(parts[1])
    if not (0 <= h <= 23 and 0 <= m <= 59):
        raise ValueError("time out of range")
    return h * 60 + m


def to_hhmm(total_minutes):
    """Convert minutes since midnight back to 'HH:MM'."""
    h = total_minutes // 60
    m = total_minutes % 60
    return f"{h:02d}:{m:02d}"


def validate_day(day_text):
    """Validate day name (case-insensitive)."""
    cleaned = day_text.strip().capitalize()
    if cleaned not in VALID_DAYS:
        raise ValueError(f"invalid day '{day_text}' (use Monday to Sunday)")
    return cleaned


def validate_type(type_text):
    """Validate activity type (class, lab, or study)."""
    cleaned = type_text.strip().lower()
    if cleaned not in VALID_TYPES:
        raise ValueError(f"invalid type '{type_text}' (use class, lab, or study)")
    return cleaned


def show_menu():
    """Display the main text menu and return the user's choice."""
    print("\n--- SMART TIMETABLE & STUDY PLANNER ---")
    print("1. View Weekly Schedule")
    print("2. Add Activity")
    print("3. Edit Activity")
    print("4. Delete Activity")
    print("5. Detect Clashes")
    print("6. Find Free Slots")
    print("7. Weekly Summary & Alerts (Save TXT)")
    print("8. Run Simple Tests")
    print("0. Exit")
    return input("Enter your choice (0-8): ").strip()


def get_activity_input():
    """Prompt user for valid activity details using try/except."""
    while True:
        try:
            day = validate_day(input("Enter day (e.g. Monday): "))
            start = input("Enter start time (HH:MM): ").strip()
            end = input("Enter end time (HH:MM): ").strip()
            s_min = to_minutes(start)
            e_min = to_minutes(end)
            if e_min <= s_min:
                raise ValueError("end time must be after start time")
            title = input("Enter activity title: ").strip()
            if not title:
                raise ValueError("title cannot be empty")
            atype = validate_type(input("Enter type (class/lab/study): "))
            return day, start, end, s_min, e_min, title, atype
        except ValueError as err:
            print(f"Invalid input: {err}. Please try again.")
