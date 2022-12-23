# TikTok-Parser-API
API for parsing data from TikTok user page and recommended using FastAPI.

# How to use?
**GET** /api/user-page?account=some-account-you-want-to-get-data-from
```
{
    "title": "some title",
    "subtitle": "cool subtitle",
    "followers": "16M",
    "following": "15",
    "likes": "857.5M",
    "bio": "amazing bio",
    "avatar": "best avatar link",
    "videos": [
        {
            "preview": "video 1 cover link",
            "ref": "full video 1 link",
            "watched_count": "83.7K"
        },
        {
            "preview": "video 2 cover link",
            "ref": "full video 2 link",
            "watched_count": "887.3K"
        },
        .
        .
        .
    ]
}
```

**GET** /api/recommend
```
{
    "accounts": [
        "recommended account 1",
        "recommended account 2",
        "recommended account 3",
        "recommended account 4",
        "recommended account 5",
        .
        .
        .
    ]
}
```

**GET** /docs

Interective documentation in your browser.

##### To run API on your localhost you can use *uvicorn* library.
```
uvicorn main:app
```
