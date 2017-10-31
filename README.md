# QuoteFetcher
A simple web application that fetches quotes from an API and displays it to the user. Created with Pyramid.
## API
### Querying requests/sessions
#### Sessions
* `GET` `/api/sessions` - returns every `session` in the database formatted as a `json` :
```
     {
         "sessions": [
              {
                  "session1_id": "<session1_id>",
                  "requests": ["request1_info", "request2_info, ...]
              },
              {
                  "session2_id": "<session2_id>",
                  "requests": ["request1_info", "request2_info, ...]
              },
              ...
          ]
     }
```
* `GET` `/api/sessions/<id>` - returns a `session` corresponding to `<id>`:
```
     {
            "session_id": "<id>",
            "requests:": ["request1_info", "request2_info, ...]
     }
```
#### Requests
* `GET` `/api/requests` - returns every `request` in the database formatted as a `json`:
Example:
```
     {
         "requests": [
             {
                 "session_id": "b2668fa6-e3f1-4bd2-8123-06e46dae5725",
                 "page url": "/",
                 "date": "2017-10-31",
                 "time": "00:19:04.645899"
             },
             {
                 "session_id": "ddc9188a-ae1f-467c-bdd5-caf9e945bb85",
                 "page url": "/quotes",
                 "date": "2017-10-31",
                 "time": "00:19:04.645899"
             },
             ...
```
* `GET` `/api/requests/<uid>` - returns a `request` corresponding to `<uid>`
* `GET` `/api/requests/session/<session_id>` - returns every `request` corresponding to `<session_id>`
* `GET` `/api/requests/date/<date>` - returns every `request` during `<date>` in the form `YYYY-MM-DD`


