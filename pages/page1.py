"""pages/page1.py — ★ your page 1.

Pick a page type from catalog/ (list, form, detail, search, stats, ranking, calculator, cart, gallery, text),
copy its page.py over this file and its page.html over templates/page1.html, then adapt.
Ask Copilot:  /new-page
"""
"""page1 — ตารางออกกำลังกายรายสัปดาห์: ดู เพิ่ม แก้ไข และลบท่าได้ในหน้าเดียว
Foundations: loop, if/else, function"""
import storage

TITLE = "ตารางออกกำลังกาย"
DIFFICULTIES = ["ง่าย", "ปานกลาง", "ยาก"]
DAYS = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]


def build(query):
    items = storage.load()

    # ใส่เลขลำดับ (ตำแหน่งจริงใน data.json) + คำนวณแคลอรี่รวมของแต่ละท่า
    numbered = []
    position = 0
    total_calories_all = 0
    for item in items:
        item["no"] = position
        item["total_calories"] = item["sets"] * item["reps"] * item["calories_per_set"]
        total_calories_all = total_calories_all + item["total_calories"]
        item["is_hard"] = item["difficulty"] == "ยาก"
        if item.get("day", "") not in DAYS:
            item["day"] = DAYS[0]          # ท่าเก่าที่ยังไม่เคยกำหนดวัน ให้ไปอยู่จันทร์เป็นค่าเริ่มต้น
        numbered.append(item)
        position = position + 1

    # จัดกลุ่มท่าทั้งหมดเป็นตารางรายสัปดาห์ ทีละวันตามลำดับใน DAYS
    week = []
    for day in DAYS:
        day_items = []
        day_calories = 0
        for item in numbered:
            if item["day"] == day:
                day_items.append(item)
                day_calories = day_calories + item["total_calories"]
        week.append({"day": day, "items": day_items, "total_calories": day_calories})

    # ถ้า URL มี ?edit=<no> ให้ดึงข้อมูลแถวนั้นมาเติมในฟอร์มฝั่งซ้าย
    edit_item = None
    edit_no = query.get("edit", "")
    if edit_no.isdigit() and int(edit_no) < len(numbered):
        edit_item = numbered[int(edit_no)]

    return {
        "items": numbered,
        "week": week,
        "count": len(numbered),
        "total_calories_all": total_calories_all,
        "difficulties": DIFFICULTIES,
        "days": DAYS,
        "edit_item": edit_item,
        "edit_no": edit_no if edit_item else "",
    }


def read_number(text):
    """แปลงข้อความจากฟอร์มเป็นตัวเลข หรือคืน None ถ้าไม่ใช่ตัวเลข"""
    try:
        value = float(text)
    except ValueError:
        return None
    if value != value or value in (float("inf"), float("-inf")):
        return None
    return value


def check(form):
    """คืนข้อความ error หรือ "" ถ้าข้อมูลถูกต้อง"""
    if form.get("name", "").strip() == "":
        return "กรุณากรอกชื่อท่า"
    if not form.get("sets", "").isdigit():
        return "จำนวนเซตต้องเป็นตัวเลขจำนวนเต็ม"
    if not form.get("reps", "").isdigit():
        return "จำนวนครั้งต้องเป็นตัวเลขจำนวนเต็ม"
    calories = read_number(form.get("calories_per_set", ""))
    if calories is None or calories < 0:
        return "แคลอรี่ต่อเซตต้องเป็นตัวเลขไม่ติดลบ"
    if form.get("day", "") not in DAYS:
        return "กรุณาเลือกวัน"
    return ""


def handle(form):
    items = storage.load()

    if "delete" in form:
        position = form["delete"]
        if position.isdigit() and int(position) < len(items):
            removed = items.pop(int(position))
            storage.save(items)
            return "🗑 ลบ " + removed["name"] + " แล้ว"
        return "✗ ไม่พบรายการที่จะลบ"

    error = check(form)
    if error != "":
        return "✗ " + error

    new_row = {
        "name": form["name"].strip(),
        "muscle_group": form.get("muscle_group", "").strip(),
        "sets": int(form["sets"]),
        "reps": int(form["reps"]),
        "calories_per_set": read_number(form["calories_per_set"]),
        "difficulty": form.get("difficulty", DIFFICULTIES[0]),
        "day": form["day"],
    }

    if "edit" in form:
        position = form["edit"]
        if not (position.isdigit() and int(position) < len(items)):
            return "✗ ไม่พบรายการที่จะแก้ไข"
        items[int(position)] = new_row
        storage.save(items)
        return "✓ แก้ไข " + new_row["name"] + " แล้ว"

    items.append(new_row)
    storage.save(items)
    return "✓ เพิ่ม " + new_row["name"] + " แล้ว"