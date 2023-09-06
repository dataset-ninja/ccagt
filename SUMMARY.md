**CCAgT: Images of Cervical Cells with AgNOR Stain Technique v2.0** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the biomedical research. 

The dataset consists of 9090 images with 59036 labeled objects belonging to 7 different classes including *nucleus*, *cluster*, *nucleus out of focus*, and other: *satellite*, *leukocyte nucleus*, *non-viable nucleus*, and *overlapped nuclei*.

Images in the CCAgT dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. The dataset was released in 2022 by the Universidade Federal de Santa Catarina, Brazil.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/ccagt/raw/main/visualizations/horizontal_grid.webm)
