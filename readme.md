# Pose2COCO Converter

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)

Reproduction Guide for Converting OpenPose Annotations to COCO Format

---

### Directory Structure
Ensure your directories are structured as follows before running the scripts:

```
Project_Root/
│
├── OpenPose_JSONs/                     # Directory containing all OpenPose JSON files
│   ├── file1.json
│   ├── file2.json
│   └── ... (all your OpenPose output JSONs)
│
├── Template/
│   └── NFD_root-15.json                # The base COCO JSON annotation template
│
├── Remapped_COCO_Output/               # Directory where the final COCO JSON file will be saved
│   └── NFD_root-15.json                # (Will be overwritten by the script)
│
└── Scripts/
    ├── json_copy.py                    # Script for remapping and converting annotations
    └── file_handler.py                 # Script for managing and cleaning files
```

### Step-by-Step Instructions to Run the Scripts

1. **Set Up Your Environment**:
   - Make sure you have Python 3.x installed on your system.
   - Ensure that `json` and `os` Python libraries are available (these are part of the Python standard library, so no need for extra installations).

2. **Generate OpenPose Annotations**:
   - Use [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) to annotate your images. Save the output JSON files in the `OpenPose_JSONs` directory.

3. **Edit Paths in `json_copy.py`**:
   - Open `json_copy.py` in a text editor.
   - Update the following paths:
     ```python
     path_to_json_files = 'Path/To/Your/OpenPose_JSONs/'  # Replace with the path to your OpenPose JSONs
     with open('Path/To/Your/Template/NFD_root-15.json') as f:  # Replace with the path to your COCO template
     with open('Path/To/Your/Remapped_COCO_Output/NFD_root-15.json', 'w') as f:  # Replace with output path
     ```
   - Save the file after updating the paths.

4. **Run the `json_copy.py` Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `json_copy.py` is located:
     ```bash
     cd Path/To/Your/Scripts/
     ```
   - Run the script using Python:
     ```bash
     python json_copy.py
     ```
   - The script will read each JSON file from `OpenPose_JSONs`, remap the keypoints, and update the COCO JSON file in `Remapped_COCO_Output`.

5. **(Optional) Clean Up Files Using `file_handler.py`**:
   - If you need to clean up redundant files, update paths in `file_handler.py` to your file directories.
   - Run the script in a similar manner:
     ```bash
     python file_handler.py
     ```
   - This script will delete unnecessary image and JSON files based on the criteria specified.

### Notes on Running the Scripts
- **Script Execution Order**: Always run `json_copy.py` first to perform the keypoint remapping and COCO annotation conversion.
- **Backup Your Data**: Before running `file_handler.py`, make sure to back up your data to avoid accidental deletions.

### Verification
- Open the remapped COCO JSON file in `Remapped_COCO_Output` and inspect the annotations to ensure they follow the COCO keypoint format.

---
