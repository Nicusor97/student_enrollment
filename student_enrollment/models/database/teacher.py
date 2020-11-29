from datetime import datetime

from student_enrollment import db
from student_enrollment.models.database.Person import Person


class Teacher(Person):

    __tablename__ = "teachers"

    email_address = db.Column(db.String(255), db.ForeignKey(
                                "person.email_address"))
    staff_id = db.Column(db.String(50), unique=True, primary_key=True)
    subjects_taught = db.relationship("Subject", backref="teacher",
                                      lazy="dynamic")
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    __mapper_args__ = {
        "polymorphic_identity": "teachers",
    }

    def __repr__(self):
        return "<Staff ID: {}>".format(self.staff_id)

    @classmethod
    def get_teacher_by_stuff_id(cls, stuff_id):
        return cls.query.filter(cls.stuff_id == stuff_id).first()

    @classmethod
    def delete_teacher_by_stuff_id(cls, stuff_id):
        return cls.query.filter(cls.stuff_id == stuff_id).delete()
