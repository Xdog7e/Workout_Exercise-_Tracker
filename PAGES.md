# PAGES · แดชบอร์ดความคืบหน้า

อัปเดตตามงานที่ทำจริง — อาจารย์ดูไฟล์นี้ + `git log` แทนการถาม

**หัวข้อ:** Workout Exercise Tracker
**data.json เก็บอะไร (field):** name, muscle_group, sets, reps, calories_per_set, difficulty, day
**คัดลอก data.json → data.sample.json แล้ว:** [ ]

## team — หน้าทีม (สัปดาห์ 0)
- [x] กรอก `team.json` ครบทุกคน (ชื่อ, รหัส, บทบาท, งานที่รับผิดชอบ)
- [x] เปิด /team เห็นชื่อทุกคน
- [ ] commit `team: members filled` + push

## page1 — ผู้รับผิดชอบ: นายปวริศ แดงวงศ์ · แบบจาก catalog: list
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [x] ใช้ field ของ data.json ของกลุ่ม
- [x] เปิด /page1 ได้ ไม่มี TODO
- [x] `check.bat` → /page1 ✓ ไม่มี warning
- [ ] commit `page1: ...`

## page2 — ผู้รับผิดชอบ: นายธนวัฒน์ บุตรทอง · แบบจาก catalog: detail
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [x] ใช้ field ของ data.json ของกลุ่ม
- [x] เปิด /page2 ได้ ไม่มี TODO
- [x] `check.bat` → /page2 ✓ ไม่มี warning
- [ ] commit `page2: ...`

## page3 — ผู้รับผิดชอบ: นายภูวนาท สายแวว · แบบจาก catalog: stats
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [x] ใช้ field ของ data.json ของกลุ่ม
- [x] เปิด /page3 ได้ ไม่มี TODO
- [x] `check.bat` → /page3 ✓ ไม่มี warning
- [ ] commit `page3: ...`

## models.py — ผู้รับผิดชอบ: นายธนวัฒน์ บุตรทอง
- [x] เปลี่ยนชื่อ class ให้ตรงหัวข้อ, field ตรง data.json
- [x] method 1 ตัวที่มีประโยชน์ (ไม่เหลือ TODO)
- [x] มีหน้าใดหน้าหนึ่งใช้ class นี้ (page2 แบบ detail)
- [x] `python check_project.py` → class ✓ 9/9
- [ ] commit `models: ...`

## ส่งงาน
- [x] โค้ดผ่านเงื่อนไข page และ Python foundations 60/60 (ตรวจซ้ำหลังแก้)
- [ ] `check.bat` → 60/60, pytest 4 passed, ไม่มี warning
- [ ] ทุกคนอยู่ใน `git log`
- [ ] นำเสนอ: ทุกคนอธิบายหน้าของตัวเอง 1 นาที
