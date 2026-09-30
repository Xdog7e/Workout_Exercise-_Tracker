"""สรุปสถิติการออกกำลังกายจากข้อมูลใน data.json"""
import storage

TITLE = "สถิติการออกกำลังกาย"


def build():
    items = storage.load()

    count = 0
    total_calories = 0
    most_calories = None
    least_calories = None
    per_muscle_group = {}

    for item in items:
        calories = item["sets"] * item["reps"] * item["calories_per_set"]
        row = {
            "name": item["name"],
            "muscle_group": item["muscle_group"],
            "calories": calories,
        }
        count = count + 1
        total_calories = total_calories + calories

        if most_calories is None or calories > most_calories["calories"]:
            most_calories = row
        if least_calories is None or calories < least_calories["calories"]:
            least_calories = row

        group = item["muscle_group"]
        if group in per_muscle_group:
            per_muscle_group[group] = per_muscle_group[group] + calories
        else:
            per_muscle_group[group] = calories

    average_calories = 0
    if count > 0:
        average_calories = total_calories / count

    biggest_group_total = 0
    for group in per_muscle_group:
        if per_muscle_group[group] > biggest_group_total:
            biggest_group_total = per_muscle_group[group]

    bars = []
    for group in per_muscle_group:
        percent = 0
        if biggest_group_total > 0:
            percent = int(per_muscle_group[group] * 100 / biggest_group_total)
        bars.append({
            "label": group,
            "value": per_muscle_group[group],
            "percent": percent,
        })

    return {
        "count": count,
        "total_calories": total_calories,
        "average_calories": average_calories,
        "most_calories": most_calories,
        "least_calories": least_calories,
        "bars": bars,
    }
