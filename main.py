import hydra
from pathlib import Path
from makevideo import makeVideo as mvd


@hydra.main(config_path='./config', config_name='video')
def main(cfg):
    dfs_copier(cfg.input_root, cfg.output_root, cfg)


def dfs_copier(input_root, output_root, cfg):
    """A dfs video dataset file structure deep copier, to deep-copy the frame file structure
    into a newly constructed video file structure.

    Args:
        input_root (str): root of source data
        output_root (str): root of dest data
        cfg (dict): hydra configured dictionary
    """
    src_root = Path(input_root)  # frame input dir
    dest_root = Path(output_root)  # output dir

    sub_roots = subdir_exists(src_root)

    if not sub_roots:  # reached leaf node: frames only
        # print("Subdir detected.")
        if list(src_root.glob(f'*.{cfg.format}')):
            dest_video = dest_root.parent / f'{dest_root.stem}.{cfg.video_format}'
            mvd(input_root, str(dest_video), cfg.fps, cfg.format, cfg.frame_shift)
        return

    for sroot in sub_roots:
        dest_sroot = dest_root / sroot.stem

        if subdir_exists(sroot):
            dest_sroot.mkdir(parents=True, exist_ok=True)

        dfs_copier(str(sroot), str(dest_sroot), cfg)


def subdir_exists(path: Path):
    sub_nodes = sorted(list(path.glob('*')))
    sub_roots = [node for node in sub_nodes if node.is_dir()]

    return sub_roots


if __name__ == '__main__':
    main()
