import logging
import sys
import urllib
import vlc
import time
# import MySQLdb
# from time import time
# import resource

# import faulthandler
# faulthandler.enable()

# logging.basicConfig(level=logging.DEBUG)

total = 0
# resource.setrlimit(resource.RLIMIT_STACK,
#                    (resource.RLIM_INFINITY, resource.RLIM_INFINITY))


# def connectDB():
#     global db

#     # Connect
#     # db = MySQLdb.connect(host="localhost",
#     #                     user="anil",
#     #                     passwd="oops!",
#     #                     db="tarana_2020_restructured")
#     local_db = MySQLdb.connect(host="localhost",
#                                user="root",
#                                passwd="password",
#                                db="tarana_2020_restructured")

#     cursor = local_db.cursor()
#     db = local_db
#     return cursor


# def getStreams(cursor, country_uid):
#     global total

#     # query = 'SELECT uid, http_status, url FROM streams order by uid DESC LIMIT 5'
#     query = 'SELECT station.uid, station.name, streams.uid, streams.url FROM streams \
#             INNER JOIN station ON station.uid = streams.station_uid  \
#             WHERE station.country_uid = "%s" \
#             GROUP BY streams.url \
#             ORDER BY station.id ASC ' % (country_uid)

#     # Execute SQL select statement
#     cursor.execute(query)
#     total = cursor.rowcount

#     # Commit your changes if writing
#     # In this case, we are only reading data
#     # db.commit()

#     # Get the number of rows in the resultset
#     # numrows = cursor.rowcount
#     # print "NUM ROWS " +  str(numrows)
#     # for x in range(0, numrows):
#     #     row = cursor.fetchone()
#     #     print row[0], "-->", row[1]
#     return cursor.fetchall()


# def streamStatus(url):
#     # url = 'http://103.16.47.70:7444/;stream.nsv'
#     code = urllib.urlopen(url, 4).getcode()
#     print(code)

#     # if code == 200:  #Edited per @Brad's comment
#     if str(code).startswith('2') or str(code).startswith('3'):
#         print('Stream is working')
#     else:
#         print('Stream is dead')
#     return str(code)


def createVLCInstance():
    # define VLC instance
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
    return instance


def playStream(instance, url):
    # define VLC instance
    # instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

    # Define VLC player
    player = instance.media_player_new()

    # Define VLC media
    media = instance.media_new(url)

    media.add_option('start-time=0.0')
    media.add_option('stop-time=5.0')

    # Set player media
    player.set_media(media)

    # Set volume for media 0-100
    player.audio_set_volume(10)

    # Play the media
    player.play()

    # print ("ANIL *******")
    # Sleep for 5 sec for VLC to complete retries.
    # time.sleep(3)
    # pause(3)
    # cursor.execute('SELECT SLEEP(5)')
    # print ("ANIL ******* END **** ")

    # Get current state.
    state = str(player.get_state())

    # Find out if stream is working.
    if state == "vlc.State.Error" or state == "State.Error":
        print('Stream is dead. Current state = {}'.format(state))
        player.stop()
    else:
        print('Stream is working. Current state = {}'.format(state))
        player.stop()

    print("VLC STATUS " + state)

    if state == "State.Playing":
        return 1
    elif state == "State.Opening":
        print("@@@ WAITING FOR 5 MORE SECS @@@")
        # time.sleep(5)
        # pause(5)

    if state == "State.Playing":
        return 1

    print("VLC STATUS " + state)

    return 0


def pause(secs):
    init_time = time()
    while time() < init_time+secs:
        pass


# def updateStatus(url, status, cursor):
#     query = 'UPDATE streams SET working_temp = "' + \
#         str(status) + '" WHERE url = "' + url + '"'
#     print(query)
#     cursor.execute(query)
#     db.commit()


def verifyURL():
    # country_name = sys.argv[1]
    # country_uid = sys.argv[2]
    # start_index = sys.argv[3]
    # end_index = sys.argv[4]
    # print("COUNTRY UID: " + country_uid)
    # print("COUNTRY NAME " + country_name)
    # cursor = connectDB()
    # instance = createVLCInstance()
    # result = getStreams(cursor, country_uid)
    # print("TOTAL ROWS " + str(total))
    # for x in range(int(start_index) - 1, int(end_index)):
    #     # for x in range(0, 5):
    #     print('STREAM NO: ' + str(x + 1))
    #     row = result[x]
    #     print(row[0], "-->", row[1])
    #     station_uid = row[0]
    #     station_name = row[1]
    #     stream_uid = row[2]
    #     stream_url = row[3]

    #     print("station_uid --> " + station_uid)
    #     print("station_name --> " + station_name)
    #     # print ("stream_uid --> " + stream_uid)
    #     print("stream_url --> " + stream_url)

    #     # http_status = streamStatus(stream_url)
    #     # print "HTTP STATUS " + http_status
    #     vlc_status = playStream(instance, stream_url, cursor)
    #     # updateStatus(stream_url, vlc_status, cursor)
    #     print("VLC STATUS " + str(vlc_status))
    #     print("----------------------------------")
    # print("*** VERIFICATION COMPLETED ***")
    instance = createVLCInstance()
    vlc_status = playStream(instance, 'http://radio.bongonet.net:8008/')
    print(vlc_status)


verifyURL()
