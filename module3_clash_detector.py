"""Module 3: Clash Detection and Testing
Owner: Kushagar Mehta (S26CSEU0220)
"""
from activity_model import make_activity
from module1_menu_validation import to_minutes


def find_clashes(activities):
    """Pairwise clash detection O(n^2) — directly from Milestone 1."""
    clashes = []
    for i in range(len(activities)):
        for j in range(i + 1, len(activities)):
            a, b = activities[i], activities[j]
            if (
                a.day == b.day
                and a.get_start_min() < b.get_end_min()
                and b.get_start_min() < a.get_end_min()
            ):
                clashes.append((a, b))
    return clashes


def find_clashes_sorted(activities):
    """Sorted clash detection O(n log n) — compares activities sorted by day and start time."""
    sorted_acts = sorted(activities, key=lambda x: (x.day, x.get_start_min()))
    clashes = []
    for i in range(len(sorted_acts)):
        a = sorted_acts[i]
        for j in range(i + 1, len(sorted_acts)):
            b = sorted_acts[j]
            if a.day != b.day or b.get_start_min() >= a.get_end_min():
                break  # Stop early since list is sorted
            clashes.append((a, b))
    return clashes


def print_clashes(activities):
    """Detect and print all clashing pairs with overlap minutes."""
    clashes = find_clashes_sorted(activities)
    if not clashes:
        print("No clashes found.")
        return clashes
    print(f"Found {len(clashes)} clash(es):")
    for a, b in clashes:
        overlap = min(a.get_end_min(), b.get_end_min()) - max(a.get_start_min(), b.get_start_min())
        print(
            f"  CLASH on {a.day}: {a.title} ({a.start}-{a.end}) overlaps "
            f"{b.title} ({b.start}-{b.end}) by {overlap} mins"
        )
    return clashes


def run_tests():
    """Simple automated test cases to verify core functions."""
    print("\n--- RUNNING SIMPLE TESTS ---")
    # Test 1: Valid time conversion
    assert to_minutes("09:30") == 570
    print("[PASS] Test 1: to_minutes('09:30') == 570")

    # Test 2: Invalid time raises ValueError
    try:
        to_minutes("25:00")
        assert False
    except ValueError:
        print("[PASS] Test 2: Invalid time '25:00' rejected safely")

    # Test 3: Back-to-back activities do NOT clash
    a1 = make_activity("Tuesday", "10:00", "11:00", 600, 660, "English", "class")
    a2 = make_activity("Tuesday", "11:00", "12:00", 660, 720, "Study Group", "study")
    assert len(find_clashes_sorted([a1, a2])) == 0
    print("[PASS] Test 3: Back-to-back classes (10:00-11:00 & 11:00-12:00) do not clash")

    # Test 4: Overlapping activities detected by both algorithms
    b1 = make_activity("Monday", "09:00", "10:00", 540, 600, "Python Lecture", "class")
    b2 = make_activity("Monday", "09:30", "11:00", 570, 660, "Digital Design Lab", "lab")
    assert len(find_clashes([b1, b2])) == 1
    assert len(find_clashes_sorted([b1, b2])) == 1
    print("[PASS] Test 4: Overlapping clash detected identically by both methods")

    # Test 5: OOP Inheritance priority check
    assert b2.get_priority() == "High (Mandatory Lab)"
    assert a2.get_priority() == "Low (Flexible Study)"
    print("[PASS] Test 5: OOP subclasses return correct priority labels")
    print("All 5 tests passed successfully!")
