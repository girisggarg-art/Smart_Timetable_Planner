"""Module 5: Weekly Summary, Workload Alerts and Report File
Owner: Arnav Kumar (S26CSEU0212)
"""
from module1_menu_validation import VALID_DAYS
from module3_clash_detector import find_clashes_sorted


def get_workload_status(hours, limit=5.0):
    """Rule-based alert using nested if/elif/else (Activity 5 Decision Tree)."""
    if hours == 0:
        return "Free Day"
    elif hours > limit:
        return "OVERLOAD ALERT"
    elif hours >= 3.5:
        return "Moderate"
    else:
        return "Balanced"


def generate_weekly_summary(activities, limit=5.0, report_file="weekly_report.txt"):
    """Compute hours per day and per type, check alerts, and save to TXT."""
    hours_by_day = {d: 0.0 for d in VALID_DAYS}
    hours_by_type = {"class": 0.0, "lab": 0.0, "study": 0.0}

    for act in activities:
        hrs = act.duration_hours()
        hours_by_day[act.day] += hrs
        hours_by_type[act.type] = hours_by_type.get(act.type, 0.0) + hrs

    total_hours = sum(hours_by_day.values())
    busiest_day = max(VALID_DAYS, key=lambda d: hours_by_day[d])
    clashes = find_clashes_sorted(activities)

    lines = []
    lines.append("====================================================")
    lines.append("   SMART TIMETABLE PLANNER - WEEKLY SUMMARY REPORT")
    lines.append("====================================================")
    lines.append(f"Total Activities : {len(activities)}")
    lines.append(f"Total Hours/Week : {total_hours:.2f} hrs")
    lines.append(f"Busiest Day      : {busiest_day} ({hours_by_day[busiest_day]:.2f} hrs)")
    lines.append(f"Clashes Detected : {len(clashes)}")
    lines.append(f"Workload Limit   : {limit:.1f} hrs/day")
    lines.append("----------------------------------------------------")
    lines.append("Hours per Day:")
    for d in VALID_DAYS:
        h = hours_by_day[d]
        status = get_workload_status(h, limit)
        lines.append(f"  {d:<10}: {h:>5.2f} hrs  [{status}]")
    lines.append("----------------------------------------------------")
    lines.append("Hours per Activity Type:")
    for t, h in hours_by_type.items():
        pct = (h / total_hours * 100) if total_hours > 0 else 0.0
        lines.append(f"  {t.capitalize():<10}: {h:>5.2f} hrs ({pct:.1f}%)")
    lines.append("====================================================")

    report_text = "\n".join(lines)
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report_text + "\n")

    return {
        "hours_by_day": hours_by_day,
        "hours_by_type": hours_by_type,
        "total_hours": total_hours,
        "busiest_day": busiest_day,
        "clash_count": len(clashes),
        "report_text": report_text,
    }
