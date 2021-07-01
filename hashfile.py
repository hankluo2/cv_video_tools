from pathlib import Path
from math import log10, ceil


def make_single_hierachicle_hash(root, pattern='*', dest=None):
    rootp = Path(root).glob('*')
    bool_dir = [item.is_dir() for item in rootp]
    cls_cnt = ceil(log10(bool_dir.count(True)))
    print(cls_cnt)

    max_ = 1
    for item in rootp:
        if item.is_dir():
            max_ = max(max_, len(item.glob(pattern)))
    file_digit_len = ceil(log10(max_))
    print(file_digit_len)


make_single_hierachicle_hash(r'D:\d513\PosteriorII\ACO')
