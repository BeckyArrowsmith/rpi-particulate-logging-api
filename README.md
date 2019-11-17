# Particulate API

Run `$ sls wsgi serve` for local development

Test calls:

` $ export BASE_DOMAIN=localhost:5000`

` $ curl -H "Content-Type: application/json" -X POST ${BASE_DOMAIN}/logs -d '{"logId": "1", "data": "some data"}' `


` $ curl -H "Content-Type: application/json" -X GET ${BASE_DOMAIN}/logs/1`
