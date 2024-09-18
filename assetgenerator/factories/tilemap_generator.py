from PIL import Image
import math
import argparse

def create_tile_map(image_paths, tile_width):
    # Load all images
    images = [Image.open(p) for p in image_paths]

    # Ensure all images are the same size
    tile_w, tile_h = images[0].size
    for img in images:
        if img.size != (tile_w, tile_h):
            img.thumbnail((tile_w, tile_h), Image.ANTIALIAS)

    # Calculate the dimensions of the tile map
    num_images = len(images)
    width = tile_width
    height = math.ceil(num_images / tile_width)

    # Create a new blank image
    map_width = width * tile_w
    map_height = height * tile_h
    tile_map = Image.new('RGBA', (map_width, map_height))

    # Paste images into the tile map
    for index, img in enumerate(images):
        x = (index % width) * tile_w
        y = (index // width) * tile_h
        tile_map.paste(img, (x, y))

    return tile_map

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a tile map from images.')
    parser.add_argument('images', nargs='+', help='List of image file paths')
    parser.add_argument('--width', type=int, default=8, help='Number of tiles in width')
    parser.add_argument('--output', type=str, default='tile_map.png', help='Output file name')

    args = parser.parse_args()

    tile_map = create_tile_map(args.images, args.width)
    tile_map.save(args.output)
    print(f"Tile map saved as {args.output}")

