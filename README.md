# Django Rest API With JWT
### Create User 
Resquest
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
Resquest
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
Resquest
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
Resquest
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
