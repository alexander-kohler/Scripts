for /R %%A in (*.mp4, *.avi, *.mov, *.wmv, *.ts, *.m2ts, *.mkv, *.mts) do (
        echo Processing "%%A"
        ffmpeg -hwaccel auto -i "%%A" -map 0:a? -map 0:s? -map 0:v -c:v hevc_nvenc -rc constqp -qp 24 "%%A~dnpA_CRF%ffmpeg_qv%_HEVC.mkv"
        	:: -map 0:a? wildcard all audiostreams?
		:: -map 0:s? wildcard all subtitle streams
		:: 
        echo Processed %%A
    )

pause