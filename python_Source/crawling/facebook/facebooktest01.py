#coding=utf-8

#project interpreter에서 facebook-sdk 설치하기
import facebook

graph = facebook.GraphAPI(access_token="EAAFYTaMh9ZCIBAPeUHNQ0wEnPnZCKxMgnZClgESyX5Cdv73ohO2ajMZCWBesT8nytJ5OIBpo8DOyvgcIca9g5UJQZAkI8XwZCEAbQgSm0zwuZCZBQMW1vEeztOaVNMmFUS6jcDdd3kaquDGJtj5BIy63j7By5eFFiX70jVVsbz2tbZCZCfbgUoZAsCzF1qbQk8sM2ajZA7WhJXlyDsZC9GFnmgGPz"
                          , version="3.0")

site_info = graph.get_object(id="me", fields=["id", "name"])

print(site_info)        #'name': '유지은', 'id': '2202665160008650'

