from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)     # add a provideer for extra fields (here internet)

fake_french = Faker("fr-FR")
fake_french.add_provider(internet)     # add a provideer for extra fields (here internet)

print("*** Generate some generic random elements")
print(f"- Name: {fake.name()}")
print(f"- Address:\n{fake.address()}")
print(f"- Phone Number: {fake.phone_number()}")
print(f"- IPv4 Private: {fake.ipv4_private()}")
print(f"- IPv4 Public: {fake.ipv4_public()}")

print()
print("*** Generate some generic random elements specific to French")
print(f"- Name: {fake_french.name()}")
print(f"- Address:\n{fake_french.address()}")
print(f"- Phone Number: {fake_french.phone_number()}")
print(f"- IPv4 Private: {fake_french.ipv4_private()}")
print(f"- IPv4 Public: {fake_french.ipv4_public()}")


print()
print("*** Generate 20 UNIQUE first names")
names = sorted([fake_french.unique.first_name() for i in range(20)])

for i, name in enumerate(names):
    print(f"{i+1}. {name}")
    