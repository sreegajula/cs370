with open('movement', 'rb') as f:
    data = f.read()

prev = 30

new_data = []

for i in range(len(data)):
    prev = prev ^ data[i]
    new_data.append(prev)

with open("script", "wb") as f:
    f.write(bytes(new_data))
