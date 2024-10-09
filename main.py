from PIL import Image, ImageEnhance

def add_filter(img_path):
    with Image.open(img_path) as img:
        # crop the image
        width, height= img.size
        cropped_img = img.crop((2,2,width-2,height-2))
        
        # mirror image
        flipped_img = cropped_img.transpose(Image.FLIP_LEFT_RIGHT)
        

        sharpness_enhancer = ImageEnhance.Sharpness(flipped_img)
        sharpnes_img = sharpness_enhancer.enhance(1.2)

        brightness_enhancer = ImageEnhance.Brightness(sharpnes_img)
        brightness_img = brightness_enhancer.enhance(1.05)

        contrasted_enhancer = ImageEnhance.Contrast(brightness_img)
        contrasted_img = contrasted_enhancer.enhance(1.01)

        color_enhancer = ImageEnhance.Color(contrasted_img)
        final_img = color_enhancer.enhance(1.05)
        
        return final_img


def overlay(base_path, overlay_path):
    with Image.open(overlay_path) as overlay:
        base_img = add_filter(base_path)

        over_width = overlay.width
        over_height = round(overlay.height*2)
        new_over = overlay.resize((over_width, over_height))
        
        new_over = new_over.convert("RGBA")
        
        alpha = new_over.split()[3]
        alpha = alpha.point(lambda p: p * 0.01)

        new_over.putalpha(alpha)
        base_img.paste(new_over, (1, 300), new_over)
        return base_img
<<<<<<< HEAD
img = add_filter(base_path)
=======
>>>>>>> b387f44e9592dd88bf2b9ca0f54b5eb9dfcce65e
img = overlay(base_path, overlay_path)
img.save("output.png")