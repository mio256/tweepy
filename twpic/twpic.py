import socket
import tweepy
import config
import urllib.error
import urllib.request
import os

LIMIT_DUPLICATION = 10
SAVE_LOCATION = "/home/skyadmin/tweepy/savepic/"  # edit here
DELETE_URL = "http://pbs.twimg.com/media/"

# twpic
# time : 20210605
# lang : python3
# code : UTF-8
# auth : mio256

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)
friends_ids = []
host = "127.0.0.1"  # adress on Processing
port = 10001  # port on Processing


def main():
    get_frineds_id()
    creat_folder(SAVE_LOCATION)
    save_pic()


def save_pic():
    skipf = choice("skip?")
    search_limit = int(input("How>>"))

    for friend_len in range(0, len(friends_ids), 100):
        # split 100IDs
        for friend_id in api.lookup_users(
                user_ids=friends_ids[friend_len:friend_len + 100]):
            print('-' * 30)
            print(friend_id.name)
            key_account = friend_id.screen_name
            friend_timeline_range = tweepy.Cursor(
                api.user_timeline, screen_name=key_account).items(search_limit)
            cnt_pic = 0
            cnt_duplication = 0
            for friend_timeline in friend_timeline_range:
                for friend_media in friend_timeline.entities.get("media", [{}]):
                    # checks if there is any media-entity
                    if friend_media.get("type", None) == "photo":
                        # checks if the entity is of the type "photo
                        try:
                            if not skipf:
                                cnt_duplication = 0
                            cnt_pic += 1
                            friend_name = friend_timeline.user.screen_name
                            img_url = friend_timeline.extended_entities['media'][0]['media_url']
                            dst_path = SAVE_LOCATION + friend_name + \
                                "_" + img_url.replace(DELETE_URL, "")
                            if not os.path.exists(dst_path):
                                download_file(img_url, dst_path)
                                print(dst_path + ' cnt:' + str(cnt_pic))
                                send_string(dst_path)  # wrong path
                                cnt_duplication = 0
                            else:
                                print("done" + ' cnt:' + str(cnt_pic))
                                if cnt_duplication >= LIMIT_DUPLICATION:
                                    break
                                cnt_duplication += 1
                        except BaseException:
                            pass
                else:
                    continue
                break


def get_frineds_id():
    # Get all IDs of people you follow
    # Don't just use the cursor to put it in an array
    my_info = api.me()
    for friend_id in tweepy.Cursor(api.friends_ids, user_id=my_info.id).items():
        friends_ids.append(friend_id)


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


def send_string(str):
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((host, port))
    socket_client.send(str.encode('utf-8'))
    socket_client.close()


def creat_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def choice(str):
    flag = input(str + ">>").lower()
    if flag in ['n', 'no', 'N', '0']:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
