import os
from pathlib import Path
import shutil
from ffmpy import FFmpeg


for folderName, subfolders, filenames in os.walk(Path.cwd()):
	print('The current folder is ' + folderName)

	for subfolder in subfolders:
		print('Subfoler of ' + folderName + ': ' + subfolder)

	for filename in filenames:
		print('File inside ' + folderName + ': ' + filename)


		if filename.endswith('.mkv') or filename.endswith('.mp4'):
			ff = FFmpeg(
				inputs={os.path.join(folderName, filename): '-hwaccel auto'},
				outputs={os.path.join(folderName, filename) + 'H265.mkv': '-map 0:a? -map 0:s? -map 0:v -c:v hevc_nvenc -rc constqp -qp 24'}
			)
			ff.cmd
			ff.run()
			"""
			shutil.move()
			"""

	print('')



"""

"""