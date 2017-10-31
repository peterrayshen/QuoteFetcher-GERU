# QuoteFetcher
A simple web application that fetches quotes from an API and displays it to the user. Created with Pyramid.
## API
### Querying requests/sessions
#### Sessions
* `/api/sessions` - returns every `session` in the database formatted as a `json` :
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
* `/api/sessions/<id>` - returns a `session` with `<id>`:
```
     {
            "session_id": "<id>",
            "requests:": ["request1_info", "request2_info, ...]
     }
```
