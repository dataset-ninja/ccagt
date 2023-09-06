The authors of the **CCAgT: Images of Cervical Cells with AgNOR Stain Technique v2.0** dataset recognize the significance of cervical cancer, which ranks as the second most common cancer among women and poses a substantial threat to public health. Early detection methods are imperative to combat this deadly disease. Cytology stands as a promising noninvasive alternative to biopsy for diagnosing malignant lesions, providing essential insights into cell characteristics. The process involves staining slides to visualize cell nuclei for accurate diagnosis. This dataset explores the use of silver-stained slides, specifically employing the <i>Argyrophilic Nucleolar Organizer Regions</i> (AgNOR) method, which exhibits substantial potential for diagnosing lesion malignancy. It's important to note that this method remains underexplored, especially in the context of computational approaches.

Factors contributing to this challenge include inadequate or nonexistent screening measures leading to late-stage detection and limited availability or affordability of standard treatment options. Infection by the <i>Human Papillomavirus</i> (HPV) serves as a primary cause of cervical cancer. Early detection and appropriate treatment can result in a cure; however, early detection remains a formidable task. Biopsy remains the gold standard for cancer and pre-cancerous lesion detection, although its invasive nature limits its use to extreme cases.

The authors note that cancer cells typically exhibit abnormal DNA content, a condition known as aneuploidy, which is associated with tumorigenesis. Increased protein synthesis in aneuploid cells characterizes the transition from normal to malignant cells. Argyrophilic Nucleolar Organizer Regions (AgNORs) can serve as valuable markers for quantifying cell proliferation, differentiation, and malignant transformation. AgNORs offer the advantage of simplicity and cost-effectiveness in detecting cell proliferation. Reports highlight the diagnostic and prognostic potential of AgNORs in cervical cytology. One diagnostic approach involves counting NORs, which are easily identifiable through the AgNOR staining technique. NORs are loops of DNA in cell nuclei containing ribosomal RNA genes, making them identifiable through AgNOR staining due to their interaction with argyrophilic nuclear proteins. While manual evaluation of AgNORs is commonly practiced, it is prone to issues like variation in visual perception, varying levels of cytologist expertise, slow processing times, and human errors.

The methodology of gaining the images encompasses several key steps. Initially, fields are generated from whole-slide images, followed by data splitting into training (52%), validation (35%), and test (13%) sets. Note, that **splits are not pre-defined**. The next step involves training a neural network, and finally, the results are evaluated.

The images were obtained from examinations conducted on women treated at the Gynecology and Colposcopy Outpatient Clinic at the Federal University of Santa Catarina (HU-UFSC). These women had cytological alterations in previous exams, leading to further gynecological exams, colposcopy, and biopsies. For image acquisition, a ZEISS Axio Scanner.Z1 with a Hitachi HV-F202SCL as the imaging device was utilized. Image processing resulted in single image files with dimensions of approximately 232,000 x 169,000 pixels, with pixel dimensions of 0.111μm x 0.111μm. Image fields were generated, and a histogram analysis was performed to eliminate fields corresponding to slide borders.

There are three categories labeled with corresponding classes: *nucleus*, *cluster*, and *satellite*

<img src="https://github.com/supervisely/supervisely/assets/78355358/3d0d8732-daf7-4350-b181-a5c22752c665" alt="image" width="400">

In version 2, there are a total of 7 categories with added distinctions between previous classes: *nucleus out of focus*, *overlapped nuclei*, *non-viable nucleus*, and *leukocyte nucleus*.

Each slide can have some differences in the stain coloration, it can be seen that an image created from different images of different slides:

<img src="https://github.com/supervisely/supervisely/assets/78355358/2708d2f0-586e-49ec-8d11-b0464c9eac8c" alt="image" width="800">

9339 images with a resolution of 1600×1200 where each pixel is 0.111µmX0.111µm were obtained from 15 different slides, having at least one label per image. Have more than sixty-three thousand annotations.

The research was approved by the UFSC Research Ethics Committee (CEPSH), protocol number 57423616.3.0000.0121. All patients involved were informed about the objectives of the study, and those who agreed to participate signed an informed consent form.