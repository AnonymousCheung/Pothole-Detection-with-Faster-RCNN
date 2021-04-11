import numpy as np
from pathlib import Path

data = np.loadtxt(open(Path().resolve().parent.absolute() / 'archive' / 'train_df.csv', 'rt'), dtype=str, usecols=(0, 2, 3, 4, 5), skiprows=1, delimiter=',')

data[:, -2:] = data[:, -2:].astype(int) + data[:, -4:-2].astype(int)
print(data[0:10])

w = (np.ones(len(data))[:, np.newaxis]*3680).astype(int)
h = (np.ones(len(data))[:, np.newaxis]*2760).astype(int)
c = np.full(len(data), "pothole", dtype='|S12')[:, np.newaxis]

print(w.shape, h.shape, c.shape)

print(data[:, 0].shape, data[:, 0][:, np.newaxis].shape, data[:, 1:].shape)
data = np.hstack((np.hstack((data[:, 0][:, np.newaxis], w, h, c)), data[:, 1:]))

# filtered_data = np.zeros(data.shape)

print(data[0:10])

for i in range(len(data)):
    data[i, 0] += '.bmp'
    if not (Path().resolve() / 'models' / 'research' / 'object_detection' / 'images' / 'train_original' / data[i, 0]).exists():
        data[i, 0] = ''
print(data[0:10])
data = data[data[:, 0] != '']

print(data[0:10])
# print(data[0,0])
print(data.shape)
np.savetxt(Path().resolve() / 'models' / 'research' / 'object_detection' / 'images' / 'train_labels.csv', data[:3200], delimiter=',', header='filename,width,height,class,xmin,ymin,xmax,ymax', fmt='%s', comments='')
np.savetxt(Path().resolve() / 'models' / 'research' / 'object_detection' / 'images' / 'test_labels.csv', data[3200:], delimiter=',', header='filename,width,height,class,xmin,ymin,xmax,ymax', fmt='%s', comments='')