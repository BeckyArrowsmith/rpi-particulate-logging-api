# Particulate API

You'll need to run two terminal windows to run with dynamodb local and wsgi:

`$ sls wsgi serve`

`$ sls dynamodb start`

Test calls:

` $ export BASE_DOMAIN=http://localhost:5000`

` $ curl -H "Content-Type: application/json" -X POST ${BASE_DOMAIN}/logs -d '{"logId": "1", "data": "some data"}' `


` $ curl -H "Content-Type: application/json" -X GET ${BASE_DOMAIN}/logs/1`

You may need to install dynamodb local: `$ sls dynamodb install`