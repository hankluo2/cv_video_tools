import cv2
from pathlib import Path
import argparse


def makeVideo(input, output, fps):
    filelist = list(Path(input).glob('*.jpg'))

    filelist.sort(key=lambda x: int(str(x.stem)))
    filelist = [str(path) for path in filelist]

    size = cv2.imread(filelist[0]).shape[:2][::-1]
    video = cv2.VideoWriter(output, cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), fps, size, True)
    # video = cv2.VideoWriter(path + '/video.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size, True)

    for item in filelist:
        print(item)
        if item.endswith('.jpg'):
            print(item)
            img = cv2.imread(item)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
    print('Video successfully made.')


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='', help='Input frames path')
    parser.add_argument('--output', type=str, default='', help='Video output path')
    parser.add_argument('--fps', type=int, default=3, help='frame per second')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    # path = './optflow'
    opt = parse()
    makeVideo(opt.input, opt.output, opt.fps)
