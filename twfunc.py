import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)


def main():
    show_timeline()


def show_tweet(name, tweetnum):
    Account = name  # 取得したいユーザーのユーザーIDを代入
    tweets = api.user_timeline(Account, count=tweetnum, page=1)
    num = 0  # ツイート数を計算するための変数
    for tweet in tweets:
        print('=' * 30)  # =を80個表示
        print('twid : ', tweet.id)               # tweetのID
        print('user : ', tweet.user.screen_name)  # ユーザー名
        print('date : ', tweet.created_at)      # 呟いた日時
        print(tweet.text)                  # ツイート内容
        print('favo : ', tweet.favorite_count)  # ツイートのいいね数
        print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
        print('ツイート数 : ', num)  # ツイート数
        print('=' * 30)  # =を80個表示
        num += 1  # ツイート数を計算


def show_tweet_remove_rep(name, tweetnum):
    Account = name  # 取得したいユーザーのユーザーIDを代入
    tweets = api.user_timeline(Account, count=tweetnum, page=1)
    num = 0  # ツイート数を計算するための変数
    for tweet in tweets:
        if(tweet.text.find('@') < 0):
            try:
                print('=' * 30)  # =を80個表示
                print('twid : ', tweet.id)               # tweetのID
                print('user : ', tweet.user.screen_name)  # ユーザー名
                print('date : ', tweet.created_at)      # 呟いた日時
                print(tweet.text)                  # ツイート内容
                print('favo : ', tweet.favorite_count)  # ツイートのいいね数
                print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
                print('ツイート数 : ', num)  # ツイート数
            except BaseException:
                print('ERROR')
        print('=' * 30)  # =を80個表示
        num += 1  # ツイート数を計算


def show_tweet_remove_rep_fav(name, tweetnum):
    Account = name  # 取得したいユーザーのユーザーIDを代入
    tweets = api.user_timeline(Account, count=tweetnum, page=1)
    num = 0  # ツイート数を計算するための変数
    for tweet in tweets:
        print('=' * 30)  # =を80個表示
        print('twid : ', tweet.id)               # tweetのID
        print('user : ', tweet.user.screen_name)  # ユーザー名
        print('date : ', tweet.created_at)      # 呟いた日時
        print(tweet.text)                  # ツイート内容
        print('favo : ', tweet.favorite_count)  # ツイートのいいね数
        print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
        print('ツイート数 : ', num)  # ツイート数
        if(tweet.text.find('@') < 0):
            try:
                api.create_favorite(tweet.id)
                print('Yes favorite')
            except BaseException:
                print('ERROR')
        print('=' * 30)  # =を80個表示
        num += 1  # ツイート数を計算


def search_tw(name, tweetnum, search_str):
    tweets = tweepy.Cursor(api.user_timeline, screen_name=name).items(tweetnum)
    num = 0  # ツイート数を計算するための変数
    cnt = 0
    for tweet in tweets:
        # print('=' * 30)  # =を80個表示
        # print('twid : ', tweet.id)               # tweetのID
        # print('user : ', tweet.user.screen_name)  # ユーザー名
        # print('date : ', tweet.created_at)      # 呟いた日時
        # print(tweet.text)                  # ツイート内容
        # print('favo : ', tweet.favorite_count)  # ツイートのいいね数
        # print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
        # print('ツイート数 : ', num)  # ツイート数
        if(tweet.text.find(search_str) >= 0):
            cnt += 1
        # print('=' * 30)  # =を80個表示
        num += 1  # ツイート数を計算
        print("cnt=" + str(cnt) + "num=" + str(num))
    return cnt


def sum_tw(name):
    tweets = tweepy.Cursor(api.user_timeline, screen_name=name).items()
    num = 0  # ツイート数を計算するための変数
    cnt = 0
    print("Now loading")
    for tweet in tweets:
        # print('=' * 30)  # =を80個表示
        # print('twid : ', tweet.id)               # tweetのID
        # print('user : ', tweet.user.screen_name)  # ユーザー名
        # print('date : ', tweet.created_at)      # 呟いた日時
        # print(tweet.text)                  # ツイート内容
        # print('favo : ', tweet.favorite_count)  # ツイートのいいね数
        # print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
        # print('ツイート数 : ', num)  # ツイート数
        num += 1  # ツイート数を計算
    print("sum=" + str(num))
    return cnt


def show_timeline():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


if __name__ == "__main__":
    main()
