import time
import random
import instagrapi

user_name = 'USERNAME_HERE'
password = 'PASSWORD_HERE'
cl = instagrapi.Client()
cl.login(user_name, password)
print('We are in,getting all media ids')
user_id = cl.user_id_from_username(user_name)
media = cl.user_medias(user_id, amount=1000)
print('Got {} medias to archive'.format(len(media)))
for each in media:
    delay = random.randrange(3, 13, 1)
    print('Current Delay:', delay)
    time.sleep(delay) # So instagramm will think its a human actions not a bot. To avoid rate-limit error
    cl.media_archive(each.id, revert=False)
    print('Media {} archived'.format(each.id))

