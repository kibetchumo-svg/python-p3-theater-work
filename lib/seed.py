from models import session, Role, Audition

# Clear tables
session.query(Audition).delete()
session.query(Role).delete()

# Create roles
hamlet = Role(character_name="Hamlet")
ophelia = Role(character_name="Ophelia")

session.add_all([hamlet, ophelia])
session.commit()

# Create auditions
a1 = Audition(actor="John Doe", location="Nairobi", phone=1234, role=hamlet)
a2 = Audition(actor="Mary Wanjiku", location="Mombasa", phone=5678, hired=True, role=hamlet)
a3 = Audition(actor="Peter Okoth", location="Kisumu", phone=9999, hired=True, role=hamlet)

a4 = Audition(actor="Sarah Atieno", location="Nakuru", phone=2222, role=ophelia)

session.add_all([a1, a2, a3, a4])
session.commit()

print("Database seeded successfully!")
