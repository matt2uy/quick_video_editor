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

# how do you handle a prompt from cmd? "Overwrite video? type y/n..."

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
# wait for process to finish first? search: "os.system wait for process"
os.system('''ffplay output.mp4''')
#
'''
1.5. make the graphics? (numbers, boxes, etc.)

2. user will traverse video and mark timestamps (is there a way to "preview" the video? is there another ffmpeg video editor to check?)
	- play video: 
		- ffplay full_match.mp4
		- https://ffmpeg.org/ffplay.html
	- how to use pause/play? other functions?
	- show the edits made without creating a new file?

	- general wiki: https://www.reddit.com/r/editors/wiki/ffmpeg
	- more info: https://video.stackexchange.com/questions/tagged/ffmpeg?sort=votes&pageSize=15
3. somehow show the changes to the user before processing?

4. convert timestamps to ffmpeg commands

5. return the complete video -> available for download?

'''
### after the "overlay": make a cut