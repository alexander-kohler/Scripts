for %%x in (*.mp4) do ffmpeg -i %%x -map_channel 0.1.0 -map_channel 0.1.0 -c:v copy stereo_%%x
pause

