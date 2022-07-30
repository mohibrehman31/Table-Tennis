import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import wget


def make_folder(folder_path):
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)


if __name__ == '__main__':
    # Need checksums
    dataset_dir = '../dataset'
    train_video_dir = os.path.join(dataset_dir, 'training', 'videos')
    train_annotation_dir = os.path.join(dataset_dir, 'training', 'annotations')

    test_video_dir = os.path.join(dataset_dir, 'test', 'videos')
    test_annotation_dir = os.path.join(dataset_dir, 'test', 'annotations')

    make_folder(train_video_dir)
    make_folder(train_annotation_dir)
    make_folder(test_video_dir)
    make_folder(test_annotation_dir)
    
    wget.download('https://lab.osai.ai/datasets/openttgames/data/game_1.mp4',train_video_dir)
    wget.download('https://lab.osai.ai/datasets/openttgames/data/test_1.mp4',test_video_dir)
    wget.download('https://lab.osai.ai/datasets/openttgames/data/test_1.zip',train_annotation_dir)
    wget.download('https://lab.osai.ai/datasets/openttgames/data/test_1.zip',test_annotation_dir)

