from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "CCAgT"
PROJECT_NAME_FULL: str = "CCAgT: Images of Cervical Cells with AgNOR Stain Technique v2.0"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_3_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Research.Biomedical()]
CATEGORY: Category = Category.Medical(extra=Category.Biology())

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2022-06-01"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://data.mendeley.com/datasets/wg4bpm33hj/2"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = None
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/ccagt"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/wg4bpm33hj-2.zip"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "nucleus": [230, 25, 75],
    "cluster": [60, 180, 75],
    "nucleus out of focus": [255, 225, 25],
    "satellite": [0, 130, 200],
    "overlapped nuclei": [245, 130, 48],
    "non-viable nucleus": [145, 30, 180],
    "leukocyte nucleus": [70, 240, 240],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = [
    "https://ieeexplore.ieee.org/document/9183262",
    "https://linkinghub.elsevier.com/retrieve/pii/S0895611121000835",
]
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[
    Union[str, List[str], Dict[str, str]]
] = "https://github.com/johnnv1/CCAgT-utils"

CITATION_URL: Optional[str] = "https://data.mendeley.com/datasets/wg4bpm33hj/2"
AUTHORS: Optional[List[str]] = [
    "João Gustavo Atkinson Amorim",
    "André Matias",
    "Tainee Bottamedi",
    "Vinícius Sanches",
    "Ane Francyne Costa",
    "Fabiana Onofre",
    "Alexandre Onofre",
    "Aldo Wangenheim",
]

ORGANIZATION_NAME: Optional[
    Union[str, List[str]]
] = "Universidade Federal de Santa Catarina, Brazil"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://ufsc.br/"

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = None
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings