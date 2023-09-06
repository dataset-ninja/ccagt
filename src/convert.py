# https://data.mendeley.com/datasets/wg4bpm33hj/2

import glob
import os
import shutil
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from supervisely.io.json import load_json_file
from tqdm import tqdm

import src.settings as s
from dataset_tools.convert import unpack_if_archive


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "Cervical Cells"
    dataset_path = "/mnt/d/datasetninja-raw/ccagt/wg4bpm33hj-2"
    images_folder = "images"
    anns_folder = "masks"
    batch_size = 30
    ds_name = "ds"

    # test = load_json_file(dataset_path + "/CCAgT_COCO_OD.json")
    # image_np = sly.imaging.image.read(dataset_path + "/masks/B/B_4043_-282240_56160.png")[:, :, 0]
    # aaaaa = np.unique(image_np)

    def create_ann(image_path):
        labels = []

        # image_np = sly.imaging.image.read(image_path)[:, :, 0]
        # img_height = image_np.shape[0]
        # img_wight = image_np.shape[1]

        ann_subfolder = image_path.split(images_folder)[-1]
        mask_path = anns_path + ann_subfolder.replace(".jpg", ".png")

        if file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
            img_height = mask_np.shape[0]
            img_wight = mask_np.shape[1]
            unique_pixels = np.unique(mask_np)[1:]
            for curr_pixel in unique_pixels:
                mask = mask_np == curr_pixel
                ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
                for i in range(1, ret):
                    obj_mask = curr_mask == i
                    curr_bitmap = sly.Bitmap(obj_mask)
                    obj_class = idx_to_class.get(curr_pixel)
                    curr_label = sly.Label(curr_bitmap, obj_class)
                    labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    idx_to_class = {
        1: sly.ObjClass("nucleus", sly.Bitmap),
        2: sly.ObjClass("cluster", sly.Bitmap),
        3: sly.ObjClass("satellite", sly.Bitmap),
        4: sly.ObjClass("nucleus out of focus", sly.Bitmap),
        5: sly.ObjClass("overlapped nuclei", sly.Bitmap),
        6: sly.ObjClass("non-viable nucleus", sly.Bitmap),
        7: sly.ObjClass("leukocyte nucleus", sly.Bitmap),
    }

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=list(idx_to_class.values()))
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_path = os.path.join(dataset_path, images_folder)
    anns_path = os.path.join(dataset_path, anns_folder)

    images_pathes = glob.glob(images_path + "/*/*.jpg")

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

    for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
        img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(img_names_batch))
    return project
