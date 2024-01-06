import vlc
import requests
import json
import time


def read_radio_stations_from_file():
    try:
        with open('./src/v1/india.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print('Error reading radio_stations.json:', e)
        return []


def http_check(radio):
    jsonData = json.loads(radio['streams'])
    try:
        response = requests.head(jsonData[0], timeout=5)
        content_type = response.headers.get('content-type', '')
        return response.status_code >= 200 or response.status_code < 400 and content_type.startswith('audio/')
    except requests.exceptions.RequestException:
        print('HTTP not working for =====> ', radio['name'])
        return False


def vlc_check(radio):
    # jsonData = json.loads(radio['streams'])
    print(radio)
    try:
        player = vlc.Instance().media_player_new()
        player.set_media(vlc.Instance().media_new(url))
        player.play()
        player.audio_set_volume(50)
        state = str(player.get_state())
        print(str(player.get_state()))
        if state == "State.Playing":
            player.stop()
            return True
        else:
            player.stop()
            return False

    except Exception:
        return False


def check_radio_stream_status():
    radio_stations = read_radio_stations_from_file()
    if not radio_stations:
        print('No radio stations found in radio_stations.json.')
        return

    working_stations = []

    for radio in radio_stations:
        if vlc_check('http://radio.bongonet.net:8008/'):
            print(f'Radio stream is working for {radio}')
            working_stations.append(radio)
        time.sleep(5)
    # Save results to a JSON file if there are any working stations
    if working_stations:
        with open('working_stations.json', 'w') as file:
            json.dump(working_stations, file, indent=2)
        print('Results have been saved to "working_stations.json".')
    else:
        print('No working stations found.')


check_radio_stream_status()
