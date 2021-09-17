import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

count = int(input('How>>'))
id = input('Who>>')
cnt = 0
for tweet in tweepy.Cursor(api.user_timeline, id).items(count):
    # 見映えのため区切る
    print('-------------------------------------------')
    # ユーザ名表示
    print('name:' + tweet.user.name + 'cnt:' + str(cnt))
    # 内容表示
    print(tweet.text)
    # try:
    #     api.create_favorite(tweet.id)
    #     print('Yes favorite')
    # except BaseException:
    #     print('ERROR')
    cnt += 1
