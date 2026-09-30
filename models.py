"""models.py — คลาสสำหรับเก็บข้อมูลท่าออกกำลังกาย (Exercise)

A page can turn a row from data.json into an object like this:

    import models
    exercise = models.Exercise(row["name"], row["muscle_group"], row["sets"], row["reps"], row["calories_per_set"], row["difficulty"])
    exercise.total_calories()
"""


class Exercise:
    def __init__(self, name, muscle_group, sets, reps, calories_per_set, difficulty):
        self.name = name
        self.muscle_group = muscle_group
        self.sets = sets
        self.reps = reps
        self.calories_per_set = calories_per_set
        self.difficulty = difficulty

    def total_calories(self):
        return self.sets * self.reps * self.calories_per_set