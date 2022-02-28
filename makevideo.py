import cv2
from pathlib import Path
import argparse
import time


def makeVideo(input, output, fps, format='png', frame_shift=0):
    since = time.time()
    filelist = sorted(list(Path(input).glob(f'*.{format}')))[frame_shift:]

    # filelist.sort(key=lambda x: int(str(x.stem)))
    filelist = [str(path) for path in filelist]

    size = cv2.imread(filelist[0]).shape[:2][::-1]
    video = cv2.VideoWriter(output, cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), fps, size, True)
    # video = cv2.VideoWriter(output, cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size, True)

    for item in filelist:
        if item.endswith(f'.{format}'):
            img = cv2.imread(item)
            if size != img.shape[:2][::-1]:
                img = cv2.resize(img, (size))
            # cv2.imshow('video', img)
            # cv2.waitKey(50)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
    duration = time.time() - since
    print(f'Video successfully generated at {output}, processing time: {duration:.1f}s')


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        type=str,
                        default='/home/roxy/lab/Traffics/TrafficMonitor/runs/detect/exp20/det',
                        help='Input frames path')
    parser.add_argument('--output', type=str, default='./015.mp4', help='Video output path')
    parser.add_argument('--fps', type=int, default=20, help='frame per second')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    # path = './optflow'
    opt = parse()
    makeVideo(**vars(opt))
