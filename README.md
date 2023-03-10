# mov2gif
MP4/AVI movie file to animated GIF file converter

### Install

    pip install git+https://github.com/tantanGH/mov2gif.git

[Windowsユーザ向けPython導入ガイド](https://github.com/tantanGH/distribution/blob/main/windows_python_for_x68k.md)

### Usage

    mov2gif [options] <input-movie-file> <output-gif-file>

Input movie file can be .mp4 or .avi either.

    options:
        -r [percent]   ... resize factor in percent (default:25)
        -d [msec]      ... duration time in msec (default:50)
        -c x1 y1 x2 y2 ... crop image after resize (default:None)
        -l [loop]      ... loop count (default:1) 0 is endless
        -s [frames]    ... skip first N frames (default:0)
        -t [frames]    ... trim last N frames (default:0)

Note that you need to add mov2gif installed folder to your PATH environment variable.
