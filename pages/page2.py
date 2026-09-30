"""page2 — รายละเอียดท่าออกกำลังกาย
แสดงรายละเอียดของแต่ละท่า และใช้ Exercise จาก models.py คำนวณแคลอรี่รวม
"""
import models
import storage

TITLE = "รายละเอียดท่าออกกำลังกาย"


def build(query):
    items = storage.load()
    rows = []
    position = 0

    for item in items:
        exercise = models.Exercise(
            item["name"],
            item["muscle_group"],
            item["sets"],
            item["reps"],
            item["calories_per_set"],
            item["difficulty"],
        )
        rows.append({
            "no": position,
            "name": exercise.name,
            "muscle_group": exercise.muscle_group,
            "sets": exercise.sets,
            "reps": exercise.reps,
            "calories_per_set": exercise.calories_per_set,
            "difficulty": exercise.difficulty,
            "total_calories": exercise.total_calories(),
            "day": item.get("day", "ยังไม่ได้กำหนด"),
        })
        position = position + 1

    selected = None
    selected_no = query.get("exercise", "")
    if selected_no.isdigit() and int(selected_no) < len(rows):
        selected = rows[int(selected_no)]

    return {
        "items": rows,
        "count": len(rows),
        "selected": selected,
    }
