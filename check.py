import vlc
import time
import sys


def play_and_check(url):
    try:
        instance = vlc.Instance('--quiet')
        player = instance.media_player_new()
        media = instance.media_new(url)
        player.set_media(media)
        player.play()
        player.audio_set_volume(50)

        # Wait for the playback status to change (play or fail)
        for _ in range(5):  # You can adjust the number of retries or the duration as needed
            state = player.get_state()
            if state == vlc.State.Playing:
                return "playing"
            elif state == vlc.State.Error:
                return "failed"
            time.sleep(1)

        player.stop()
        return "failed"  # If the status is not determined within the wait time

    except Exception as e:
        return str(e)


# Check if a command-line argument is provided
if len(sys.argv) < 2:
    sys.exit(1)

# Get the stream URL from the command-line argument
url = sys.argv[1]

print(play_and_check(url))
