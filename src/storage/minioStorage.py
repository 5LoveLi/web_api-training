import io


def save_file(data, path):
    with open(path, 'wb') as f:
        f.write(data)


def upload_video_minio(file, name_file):
    path = 'C:/Users/User/Desktop/videoStore/video/' + name_file + '.mp4'

    return path



def upload_preview_minio(file_preview, name_file):
    path = 'C:/Users/User/Desktop/videoStore/preview/' + name_file + '.jpg'

    return path