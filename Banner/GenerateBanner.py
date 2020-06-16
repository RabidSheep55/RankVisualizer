import json
import numpy as np

_, x = np.meshgrid(np.arange(25), np.arange(1, 10))

# Mix array 200 times
for i in range(200):
    # 20% chance for large mix
    if np.random.rand() < 0.8:
        d = 1
    else:
        d = 2
    j = np.random.randint(len(x) - d )
    i = np.random.randint(len(x[0])-1) + 1
    (x[j, i], x[j+d, i]) = (x[j+d, i], x[j, i])

out = {}
for i in range(len(x)):
    out[str(i)] = x[i, :].tolist()

with open("data.json", 'w') as file:
    json.dump(out, file)
