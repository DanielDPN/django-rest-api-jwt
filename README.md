# Django Rest API With JWT
### Create User 
Request
```sh
curl -X POST \
  http://localhost:8000/api/v1/auth/register/ \
  -H 'content-type: application/json' \
  -d '{
    	"username": "new_user",
    	"password": "new_pass",
    	"email": "new_user@mail.com"
      }'
```
### Login
Request
```sh
curl -X POST \
  http://localhost:8000/api/v1/auth/login/ \
  -H 'content-type: application/json' \
  -d '{
    	"username": "new_user",
    	"password": "new_pass"
      }'
```
Response
```sh
{
    token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Im5ld191c2VyIiwiZXhwIjoxNTQwNDkyMTQ2LCJlbWFpbCI6Im5ld191c2VyQG1haWwuY29tIn0.8_8S-5MYY-gXkkJ-emT97s-aW8JhMEGnOyahS20uPtQ"
}
```
### Create Token
Request
```sh
curl -X POST \
  http://localhost:8000/api-token-auth/ \
  -H 'content-type: application/json' \
  -d '{
        "username": "new_user",
        "password": "new_pass"
      }'
```
Response
```sh
{
    token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Im5ld191c2VyIiwiZXhwIjoxNTQwNDkyMTQ2LCJlbWFpbCI6Im5ld191c2VyQG1haWwuY29tIn0.8_8S-5MYY-gXkkJ-emT97s-aW8JhMEGnOyahS20uPtQ"
}
```
### Songs
Request
```sh
curl -X GET \
  http://localhost:8000/api/v1/songs/ \
  -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Im5ld191c2VyIiwiZXhwIjoxNTQwNDkyMTQ2LCJlbWFpbCI6Im5ld191c2VyQG1haWwuY29tIn0.8_8S-5MYY-gXkkJ-emT97s-aW8JhMEGnOyahS20uPtQ' \
```
Response
```sh
[
    {
        "title": "Kiss from a rose",
        "artist": "Seal"
    },
    {
        "title": "Gotham city",
        "artist": "R Kelly"
    },
    {
        "title": "World greatest",
        "artist": "R Kelly"
    },
    {
        "title": "Always",
        "artist": "James Ingram"
    }
]
```
### Find Song
Request
```sh
curl -X GET \
  http://localhost:8000/api/v1/songs/1/ \
  -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Im5ld191c2VyIiwiZXhwIjoxNTQwNTU3Mjc3LCJlbWFpbCI6Im5ld191c2VyQG1haWwuY29tIn0.zCPIfm25UD3ySF7ivxfKwBEIaz4x68U8CY0pRCkJWTg' \
```
Response
```sh
{
    "title": "Kiss from a rose",
    "artist": "Seal"
}
```
### Create Song
Request
```sh
curl -X POST \
  http://localhost:8000/api/v1/songs/ \
  -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Im5ld191c2VyIiwiZXhwIjoxNTQwNTU3Mjc3LCJlbWFpbCI6Im5ld191c2VyQG1haWwuY29tIn0.zCPIfm25UD3ySF7ivxfKwBEIaz4x68U8CY0pRCkJWTg' \
  -H 'content-type: application/json' \
  -d '{
        "title": "Lifelines",
        "artist": ""
      }'
```
Response
```sh
{
    "title": "Lifelines",
    "artist": ""
}
```
### Update Song
Request
```sh
curl -X PUT \
  http://localhost:8000/api/v1/songs/5/ \
  -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Im5ld191c2VyIiwiZXhwIjoxNTQwNTU3Mjc3LCJlbWFpbCI6Im5ld191c2VyQG1haWwuY29tIn0.zCPIfm25UD3ySF7ivxfKwBEIaz4x68U8CY0pRCkJWTg' \
  -H 'content-type: application/json' \
  -d '{
        "title": "Lifelines",
        "artist": "A-ha"
      }'
```
Response
```sh
{
    "title": "Lifelines",
    "artist": "A-ha"
}
```
### Remove Song
Request
```sh
curl -X DELETE \
  http://localhost:8000/api/v1/songs/5/ \
  -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Im5ld191c2VyIiwiZXhwIjoxNTQwNTU3Mjc3LCJlbWFpbCI6Im5ld191c2VyQG1haWwuY29tIn0.zCPIfm25UD3ySF7ivxfKwBEIaz4x68U8CY0pRCkJWTg' \
```