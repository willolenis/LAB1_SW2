from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class StudyGroup(db.Model):
    """
    Represents a study group created by a student for a specific course
    at a specific day/time, so other students can filter by class + schedule.
    """
    id = db.Column(db.Integer, primary_key=True)

    course_code = db.Column(db.String(20), nullable=False)   # e.g. "CS 3345"
    course_name = db.Column(db.String(100), nullable=False)  # e.g. "Data Structures"

    creator_name = db.Column(db.String(100), nullable=False)

    day_of_week = db.Column(db.String(10), nullable=False)   # e.g. "Monday"
    start_time = db.Column(db.String(5), nullable=False)     # "14:00"
    end_time = db.Column(db.String(5), nullable=False)       # "15:30"

    location = db.Column(db.String(100))
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<StudyGroup {self.course_code} {self.day_of_week} {self.start_time}-{self.end_time}>"
