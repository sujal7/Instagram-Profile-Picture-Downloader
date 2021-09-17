import instaloader
bot1 = instaloader.Instaloader()
username = input("Enter username: ")
print(bot1.download_profile(username,profile_pic_only=True))   # Downloaded in the same folder as program