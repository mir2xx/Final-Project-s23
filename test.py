from manager import Manager
m=Manager()
m.generate_password("google","gman",14)
m.generate_password("youtube","gman",13)
m.save()
print(m.load)