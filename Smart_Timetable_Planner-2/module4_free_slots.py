"""Module 4: Free-Slot Finder
Owner: Tanuj Bansal (S26CSEU0203)
"""
from module1_menu_validation import to_minutes, to_hhmm, validate_day


def find_free_slots(activities, day, window_start="08:00", window_end="18:00"):
    """Find free gaps between activities on a chosen day within a time window."""
    day_clean = validate_day(day)
    win_s = to_minutes(window_start)
    win_e = to_minutes(window_end)
    if win_e <= win_s:
        raise ValueError("window end must be after window start")

    # Collect and sort busy slots on that day
    busy = []
    for act in activities:
        if act.day == day_clean:
            s = max(act.get_start_min(), win_s)
            e = min(act.get_end_min(), win_e)
            if e > s:
                busy.append((s, e))
    busy.sort()

    # Merge overlapping busy intervals
    merged = []
    for s, e in busy:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    # Extract free gaps
    free_slots = []
    current = win_s
    for bs, be in merged:
        if bs > current:
            free_slots.append((to_hhmm(current), to_hhmm(bs), bs - current))
        current = max(current, be)
    if win_e > current:
        free_slots.append((to_hhmm(current), to_hhmm(win_e), win_e - current))
    return free_slots


def print_free_slots(activities, day, window_start="08:00", window_end="18:00"):
    """Print free study slots nicely."""
    slots = find_free_slots(activities, day, window_start, window_end)
    print(f"\nFree slots on {day} ({window_start}-{window_end}):")
    if not slots:
        print("  No free slots available in this window.")
    for start, end, mins in slots:
        print(f"  {start} - {end} ({mins} mins)")
    return slots
