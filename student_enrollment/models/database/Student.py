from datetime import datetime

from student_enrollment import db
from student_enrollment.models.database.Person import Person
from student_enrollment.models.database import helpers


class Student(Person):

    __tablename__ = "students"

    email_address = db.Column(db.String(255), db.ForeignKey(
                                "person.email_address"))
    student_id = db.Column(db.String(50), unique=True, primary_key=True)
    major_id = db.Column(db.String(50), db.ForeignKey("subjects.subject_id"))
    minors = db.relationship("Subject", secondary=helpers.student_subject_table,
                             back_populates="minor_students")
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    __mapper_args__ = {
        "polymorphic_identity": "students",
    }

    def __repr__(self):
        return "<Student ID: {}>".format(self.student_id)

    @classmethod
    def get_student_by_student_id(cls, student_id):
        return cls.query.filter(cls.student_id == student_id).first()

    @classmethod
    def delete_student_by_student_id(cls, student_id):
        return cls.query.filter(cls.student_id == student_id).delete()
