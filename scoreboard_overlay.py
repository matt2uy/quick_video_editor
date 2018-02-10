# scoreboard overlay

# using ffmpeg commands (or moviepy?)

source_video = "full_match.mp4"
scoreboard_overlay = "scoreboard_overlay.png"

import os
os.system('ffmpeg -version')



### 1. add an overlay 
# to do: get width/height of frame (in pixels) and
# 	add some margin (fixed or percentage?)
#
# add some variables in later
# (triple quotes = the 3rd type of quote)
os.system('''ffmpeg -i full_match.mp4 -i scoreboard_overlay.png -filter_complex "[0:v][1:v] overlay=25:25:enable='between(t,0,5)'" -pix_fmt yuv420p -c:a copy output.mp4''')

'''
2. user will traverse video and mark timestamps

3. somehow show the changes to the user before processing?

4. convert timestamps to ffmpeg commands

5. return the complete video -> available for download?

'''
### after the "overlay": make a cut