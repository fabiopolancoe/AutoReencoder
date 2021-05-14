# AutoReencoder
Script to automatically reencode multimedia files using Python and ffmpeg.

**NOTE: This only works on Linux systems**

## Usage:
If you run `main.py`, you should install ffmpeg first in your system. You can directly run the command without needing to call Python, but you must have Python3 installed.

```sh
./main.py <input> <output>
```

On the other hand, the latest `areencode` binary already includes ffmpeg bundled with it so you won't need anything else than the pure ELF file.

```
./areencode <input> <output>
```

If you get a Permission Denied error by running the binary, don't use sudo, just add execution permission:

```
chmod +x areencode
```

You can also use `areencode` globally (in any directory) either by adding the folder where the file is to PATH or by moving (with the help of sudo) it to /usr/local/bin.

### Reencoding multimedia files
This tool is able to convert any media type supported by ffmpeg (audio to video, video to audio, audio to other format, etcetera)

¿What's the difference between AutoReencoder and vanilla ffmpeg then? AutoReencoder is made for just converting file formats, so you won't be able to do something else with it.

This script takes two arguments: "input" and "output" (never-used-before argument names, I know). What the tool does is to find in the current folder all files whose filename ends with `<input>`
and convert them to the same filename but now with `<output>` as extension and format. So you can pass "mp4" as first argument and "mp3" as the second one, and it will convert all mp4 files in the current directory
to mp3, obviously if you only want to convert ONE file, you can cheat and pass `"filename.extension"` and `"filename.new_extension"` as parameters.

Here's an example:

<video with="400" height="275" src="test.mp4" autoplay loop />
