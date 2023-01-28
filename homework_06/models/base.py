from sqlalchemy.orm import declared_attr


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User -> users
        Author -> authors
        """
        return f"{cls.__name__.lower()}s"

    def __repr__(self):
        return str(self)
