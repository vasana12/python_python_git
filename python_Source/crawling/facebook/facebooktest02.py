import facebook

obj = facebook.GraphAPI(access_token="EAAFYTaMh9ZCIBAPeUHNQ0wEnPnZCKxMgnZClgESyX5Cdv73ohO2ajMZCWBesT8nytJ5OIBpo8DOyvgcIca9g5UJQZAkI8XwZCEAbQgSm0zwuZCZBQMW1vEeztOaVNMmFUS6jcDdd3kaquDGJtj5BIy63j7By5eFFiX70jVVsbz2tbZCZCfbgUoZAsCzF1qbQk8sM2ajZA7WhJXlyDsZC9GFnmgGPz"
                          , version="3.0")

res = obj.get_connections(id="me", connection_name = "posts", limit=10)
f = open("facebook_posts.txt", "wt")
print(res)
for data in res["data"]:
    print(data)
    #print(data['id'],end=',')
    #print(data['created_time'], end=',')
    #print(data['message'])