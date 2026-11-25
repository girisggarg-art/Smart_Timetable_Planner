"""Main Program: Integration of All 5 Modules
Integration Owner: Tanuj Bansal (S26CSEU0203)
Run interactive menu: python3 main.py
Run quick demo:       python3 main.py --demo
"""
import sys
from module1_menu_validation import show_menu, get_activity_input
from module2_csv_storage import (
    load_schedule,
    view_schedule,
    add_activity,
    edit_activity,
    delete_activity,
)
from module3_clash_detector import print_clashes, run_tests
from module4_free_slots import print_free_slots
from module5_weekly_summary import generate_weekly_summary


def run_demo():
    """Run all 5 modules automatically on schedule.csv for quick Viva demo."""
    activities = load_schedule("schedule.csv")
    print(f"Loaded {len(activities)} activities from schedule.csv.")
    view_schedule(activities)
    print("\n--- CLASH DETECTION ---")
    print_clashes(activities)
    print_free_slots(activities, "Monday", "08:00", "18:00")
    summary = generate_weekly_summary(activities, limit=5.0)
    print("\n" + summary["report_text"])
    print("Saved weekly summary to weekly_report.txt")
    run_tests()


def main():
    activities = load_schedule("schedule.csv")
    print(f"Loaded {len(activities)} activities.")

    while True:
        choice = show_menu()
        if choice == "1":
            view_schedule(activities)
        elif choice == "2":
            vals = get_activity_input()
            add_activity(activities, *vals)
        elif choice == "3":
            view_schedule(activities)
            try:
                num = int(input("Enter activity number to edit: ")) - 1
                vals = get_activity_input()
                edit_activity(activities, num, *vals)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            view_schedule(activities)
            try:
                num = int(input("Enter activity number to delete: ")) - 1
                delete_activity(activities, num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print_clashes(activities)
        elif choice == "6":
            day = input("Enter day (e.g. Monday): ")
            try:
                print_free_slots(activities, day, "08:00", "18:00")
            except ValueError as err:
                print(f"Error: {err}")
        elif choice == "7":
            summary = generate_weekly_summary(activities, limit=5.0)
            print("\n" + summary["report_text"])
            print("Report saved to weekly_report.txt.")
        elif choice == "8":
            run_tests()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 0 to 8.")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        run_demo()
    else:
        main()
