# Photo uniqueizer

This Python script processes images and makes them unique using the Pillow library. It is designed to generate variations of images for creative purposes or other use cases where unique versions of an image are needed.

## Features
- Uses the Pillow library to modify images.
- Applies subtle changes to make each image unique.
- Supports various image formats (JPEG, PNG, etc.).
- Easy to integrate and extend for other photo manipulation tasks.

## Requirements

- Python 3.x
- Pillow library

1. **Clone the repository**:
    ```bash
    git clone https://github.com/dimakostenko19/photo-uniqueization.git
    cd photo_unique
    ```

2. **You can install the required dependencies using**:
    ```bash
    pip install -r requirements.txt

3. **Path configuration**:
    Replace `base_path` with the path to the base image and `overlay_path` with the path to the image that will be overlaid.

4. **Run script**:
    ```bash
    python main.py
    ```