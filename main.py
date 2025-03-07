from PIL import Image
import time

def rgb_to_ascii(r, g, b):
    # Normalize RGB values
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0
    # Map to ASCII color
    ascii_palette = {0: ' ', 1: '.', 2: ':', 3: 'o', 4: '8', 5: '#', 6: '@'}
    ascii_value = int((r_norm + g_norm + b_norm) / 3 * 6)
    return ascii_palette[ascii_value]

def main():
    with Image.open("linus.jpg") as im:
        # Resize for better visualization (optional)
        width, height = im.size
        new_width = 50  # Adjust for better aspect ratio
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.55)  # 0.55 corrects aspect distortion
        im = im.resize((new_width, new_height))

        rgb_im = im.convert("RGB")

        #print(width, height)

    for y in range(im.height):
        for x in range(im.width):
            r, g, b = rgb_im.getpixel((x, y))
            print(rgb_to_ascii(r, g, b), end="")  # Print character without newline
        print()  # Move to the next line



if __name__ == "__main__":
    main()