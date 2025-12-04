from models import session, Role, Audition

# Fetch a role
hamlet_role = session.query(Role).filter_by(character_name="Hamlet").first()
ophelia_role = session.query(Role).filter_by(character_name="Ophelia").first()

print("Hamlet actors:", hamlet_role.actors())
print("Hamlet locations:", hamlet_role.locations())
print("Hamlet lead:", hamlet_role.lead())
print("Hamlet understudy:", hamlet_role.understudy())

print("Ophelia actors:", ophelia_role.actors())
print("Ophelia lead:", ophelia_role.lead())
