import numpy as np
from pathlib import Path
import cv2

def resize(subset):
    # data = np.loadtxt(open(Path().resolve().parent.absolute() / 'archive' / 'train_df.csv', 'rt'), dtype=str, usecols=(0), skiprows=1, delimiter=',')
    parent_dir = Path().resolve() / 'models' / 'research' / 'object_detection' / 'images'
    data = np.loadtxt(open(parent_dir / f'{subset}_labels.csv', 'rt'), dtype=str, usecols=(0), skiprows=1, delimiter=',')
    print(data.shape)

    # print(data[0:10])
    # for i in range(len(data)):
    #     if not (Path().resolve() / 'models' / 'research' / 'object_detection' / 'images' / 'train_original' / (data[i] + '.jpg')).exists():
    #         data[i] = ''
    # print(data[0:10])
    # data = np.unique(data[data != ''])
    data = np.unique(data)

    print(data[0:10])
    # data = data
    for i in range(len(data)):
        # print(data[i])
        # print(str(parent_dir / 'train_original' / (data[i] + '.jpg')))
        img = cv2.imread(str(parent_dir / 'train_original' / data[i]))
        dim = (img.shape[1] // 6, img.shape[0] // 6)
        resized = cv2.resize(img, dim)
        # target_path = Path().resolve() / 'models' / 'research' / 'object_detection' / 'images' / 'train_final' / (data[i] + '.bmp')
        # target_path = 'models/research/object_detection/images/train/'+data[i]+'.bmp' 
        target_path = str(parent_dir / f'{subset}_final' / (data[i][:-4] + '.bmp'))
        cv2.imwrite(target_path, resized)
        print(f'Resizing {i} of {len(data)} images: {target_path}')

resize('train')
resize('test')
print('FINISHED')


# print(data[:, 0].shape, data[:, 0][:, np.newaxis].shape, data[:, 1:].shape)
# data = np.hstack((np.hstack((data[:, 0][:, np.newaxis], w, h, c)), data[:, 1:]))

# # filtered_data = np.zeros(data.shape)

# print(data[0:10])

# for i in range(len(data)):
#     data[i, 0] += '.jpg'
#     if not (Path().resolve() / 'models' / 'research' / 'object_detection' / 'images' / 'train' / data[i, 0]).exists():
#         data[i, 0] = ''
# print(data[0:10])
# data = data[data[:, 0] != '']

# print(data[0:10])
# print(data[0,0])
# print(data.shape)
# np.savetxt(Path().resolve() / 'models' / 'research' / 'object_detection' / 'images' / 'train_labels.csv', data, delimiter=',', header='filename,width,height,class,xmin,ymin,xmax,ymax', fmt='%s', comments='')