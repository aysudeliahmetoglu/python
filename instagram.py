# Get instance
import instaloader

# Login or load session

L = instaloader.Instaloader()
L.login(username, password)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context,"hsdyalova")

# Print list of followees

for followee in profile.get_followers():
    follow_list = []
    count = 0
    follow_list.append(followee.username)
    # file = open("hsdyalovatakipci.txt", "a+")
    # file.write(follow_list[count])
    # file.write("\n")
    # file.close()
    print(follow_list[count])
    count = count + 1