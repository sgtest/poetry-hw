from tqdm import tqdm
count = 0
for i in tqdm(range(100)):
    count += i
print(count)
