import argparse
import cv2
import sys

from PIL import Image

def convert_movie_to_gif(movie_file_name,gif_file_name,resize_pct=25,duration=50,crop=None,loop=1):

    # Open the movie file
    video = cv2.VideoCapture(movie_file_name)

    # Get the width and height of the video frames
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Get the frame rate
    fps = video.get(cv2.CAP_PROP_FPS)

    # Get the total number of frames
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Retrieve the fourcc code of the video
    fourcc_int = int(video.get(cv2.CAP_PROP_FOURCC))

    # Convert the fourcc code to a human-readable format
    fourcc_str = fourcc_int.to_bytes(4, 'little').decode('utf-8')

    # length in seconds
    length = total_frames / fps

    print(f"    movie name: {movie_file_name}")
    print(f"        format: {fourcc_str}")
    print(f"         width: {width}")
    print(f"        height: {height}")
    print(f"           fps: {fps:.5f}")
    print(f"  total frames: {total_frames}")
    print(f"  total length: {length:.2f}s")
    print(f"")
    print(f"      gif name: {gif_file_name}")

    images = []

    image_size = (width * resize_pct // 100, height * resize_pct // 100)

    while(video.isOpened()):

        # Read the next frame from the input file
        ret, frame = video.read()

        if ret:
            # Get the raw bytes of the frame
            raw_bytes = frame.tobytes()
            raw_bytes_rgb = bytearray(len(raw_bytes))
            for i in range(len(raw_bytes)//3):
                raw_bytes_rgb[i*3+0] = raw_bytes[i*3+2]
                raw_bytes_rgb[i*3+1] = raw_bytes[i*3+1]
                raw_bytes_rgb[i*3+2] = raw_bytes[i*3+0]
            im = Image.frombytes("RGB", (width, height), bytes(raw_bytes_rgb), decoder_name='raw') \
                      .resize(image_size).quantize(method=1,colors=256)
            if crop is None:
                images.append(im)
            else:
                images.append(im.crop(crop))

        else:
            break

        print(".", end="", flush=True)

    video.release()

    images[0].save(gif_file_name, format="gif", save_all=True, append_images=images[1:], duration=duration, loop=loop)

    print("Done.")


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("infile",help="input movie file (MP4/AVI)")
    parser.add_argument("outfile",help="output GIF file")
    parser.add_argument("-s","--resize",help="resize 1-100% (default:25)",type=int,default=25)
    parser.add_argument("-c","--crop",help="crop image (x1,y1,x2,y2)",type=int, nargs=4)
    parser.add_argument("-d","--duration",help="duration time in msec (default:50)",type=int,default=50)
    parser.add_argument("-l","--loop",help="loop count (default:1) 0 ... endless",type=int)

    args = parser.parse_args()

    if args.crop is not None and len(args.crop) != 4:
        print("crop options requires 4 parameters - x1,y1,x2,y2")
        sys.exit(1)

    # execute conversion in script mode
    convert_movie_to_gif( args.infile, args.outfile, args.resize, args.duration, args.crop, args.loop )
