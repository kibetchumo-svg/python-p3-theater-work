from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///theater.db")
Session = sessionmaker(bind=engine)
session = Session()


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    auditions = relationship("Audition", back_populates="role")

    # Return all actor names
    @property
    def actors(self):
        return [audition.actor for audition in self.auditions]

    # Return all locations
    @property
    def locations(self):
        return [audition.location for audition in self.auditions]

    # Return first hired audition
    def lead(self):
        hired = [a for a in self.auditions if a.hired]
        if hired:
            return hired[0]
        return "no actor has been hired for this role"

    # Return second hired audition
    def understudy(self):
        hired = [a for a in self.auditions if a.hired]
        if len(hired) > 1:
            return hired[1]
        return "no actor has been hired for understudy for this role"

    def __repr__(self):
        return f"<Role {self.id}: {self.character_name}>"


class Audition(Base):
    __tablename__ = "auditions"

    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="auditions")

    # Hire callback
    def call_back(self):
        self.hired = True
        session.commit()

    def __repr__(self):
        return f"<Audition {self.id}: {self.actor} ({'HIRED' if self.hired else 'not hired'})>"
