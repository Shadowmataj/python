from internet_speed_twitter_bot import  InternetSpeedTwitterBot

PROMISED_DOWNLOAD_SPEED = 200
PROMISED_UPLOAD_SPEED = 20

bot =  InternetSpeedTwitterBot()

bot.get_internet_speed()
if bot.down < PROMISED_DOWNLOAD_SPEED or bot.up < PROMISED_UPLOAD_SPEED:
    bot.tweet_at_provider(promise_up=PROMISED_UPLOAD_SPEED, promise_down=PROMISED_DOWNLOAD_SPEED)


