import random as rd

def generate_ip():
    d = []
    for _ in range(4):
        d.append(str(rd.randint(0, 255)))
    return '.'.join(d)

print(generate_ip())
