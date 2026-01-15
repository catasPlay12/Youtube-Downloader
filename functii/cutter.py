from moviepy.editor import VideoFileClip, AudioFileClip


def trim_video(input_file, start_time, end_time, output_file, progress_callback=None):

    try:
        clip = VideoFileClip(input_file).subclip(start_time, end_time)
        duration = clip.duration

        def update_progress(get_frame, t):
            if progress_callback:
                percent = min(int((t / duration) * 100), 100)
                progress_callback(percent)
            return get_frame(t)

        clip.write_videofile(
            output_file,
            codec="libx264",
            audio_codec="aac",
            progress_bar=False,  # dezactivăm progress bar-ul intern
            verbose=False,
            logger=None,
            write_logfile=False
        )
        clip.close()
        if progress_callback:
            progress_callback(100)
        print(f"Video salvat: {output_file}")
    except Exception as e:
        print(f"Eroare la tăiere video: {e}")


def trim_audio(input_file, start_time, end_time, output_file, progress_callback=None):
    try:
        clip = AudioFileClip(input_file).subclip(start_time, end_time)
        duration = clip.duration

        if progress_callback:
            steps = 100
            for i in range(steps):
                progress_callback(i)

        clip.write_audiofile(output_file, verbose=False, logger=None)
        clip.close()
        if progress_callback:
            progress_callback(100)
        print(f"Audio salvat: {output_file}")
    except Exception as e:
        print(f"Eroare la tăiere audio: {e}")
