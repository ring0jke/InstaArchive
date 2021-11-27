import time

import instagrapi

user_name = 'ENTER UR LOGIN HERE'
password = 'AND UR PASSWORD HERE!'

cl = instagrapi.Client()
cl.login(user_name, password)
print('We are in,getting all media ids')
user_id = cl.user_id_from_username(user_name)
media = cl.user_medias(user_id, amount=1000)
print('Got {} medias to archive'.format(len(media)))
for each in media:
    time.sleep(1, 5)
    cl.media_archive(each.id, revert=False)
    print('Media {} archived'.format(each.id))
