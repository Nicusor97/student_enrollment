from student_enrollment import db

# For the many-to-many relationship between subjects and students.
# One student can minor in several subjects and one subject can
# be taught to several students as a minor
student_subject_table = db.Table(
    "student_subject", db.Model.metadata,
    db.Column("student_id", db.String(50), db.ForeignKey(
        "students.student_id")),
    db.Column("subject_id", db.String(50), db.ForeignKey(
        "subjects.subject_id"))
)
