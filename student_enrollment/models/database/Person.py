from student_enrollment import db


class Person(db.Model):

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email_address = db.Column(db.String(255), unique=True, primary_key=True)
    person_type = db.Column(db.String(50))

    __mapper_args__ = {
        "polymorphic_identity": "person",
        "polymorphic_on": person_type
    }

    def __repr__(self):
        return "<{}: {} {}>".format(self.person_type, self.first_name,
                                    self.last_name)

    @classmethod
    def get_person_by_email_address(cls, email):
        return cls.query.filter(cls.email_address == email).first()

    @classmethod
    def delete_person_by_email_address(cls, email):
        return cls.query.filter(cls.email_address == email).delete()

    def to_dict(self):
        details_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email_address": self.email_address,
            "person_type": self.person_type
        }

        return details_dict

