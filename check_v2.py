import vlc
import time
import sys


def play_and_check(url, duration=5):
    try:
        instance = vlc.Instance('--quiet')
        player = instance.media_player_new()
        media = instance.media_new(url)
        player.set_media(media)
        player.play()
        player.audio_set_volume(50)

        start_time = time.time()
        while (time.time() - start_time) < duration:
            state = player.get_state()
            if state == vlc.State.Error:
                player.stop()
                return "failed"
            elif state == vlc.State.Playing:
                time.sleep(1)
            else:
                time.sleep(0.1)  # Adjust sleep time for faster response

        if player.get_state() != vlc.State.Playing:
            player.stop()
            return "failed"  # Stream stopped before the specified duration
        else:
            player.stop()
            return "playing"  # Stream played for the specified duration

    except Exception as e:
        return str(e)


# Check if a command-line argument is provided
if len(sys.argv) < 2:
    sys.exit(1)

# Get the stream URL from the command-line argument
url = sys.argv[1]

print(play_and_check(url, duration=5))
