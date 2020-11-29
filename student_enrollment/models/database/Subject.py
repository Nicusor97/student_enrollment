from datetime import datetime

from student_enrollment import db
from student_enrollment.models.database import helpers


class Subject(db.Model):

    __tablename__ = "subjects"

    subject_id = db.Column(db.String(50), unique=True, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(150))
    teacher_id = db.Column(db.String(50), db.ForeignKey("teachers.staff_id"))
    major_students = db.relationship("Student", backref="major",
                                     lazy="dynamic")
    minor_students = db.relationship("Student",
                                     secondary=helpers.student_subject_table,
                                     back_populates="minors")
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __repr__(self):
        return "<Subject ID: {}>".format(self.subject_id)

    @classmethod
    def get_subject_by_subject_id(cls, subject_id):
        return cls.query.filter(cls.subject_id == subject_id).first()

    @classmethod
    def delete_subject_by_subject_id(cls, subject_id):
        return cls.query.filter(cls.subject_id == subject_id).delete()
