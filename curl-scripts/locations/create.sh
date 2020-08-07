#!/bin/bash

curl "http://localhost:8000/locations/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "location": {
      "city": "'"${CITY}"'",
      "state": "'"${STATE}"'",
      "country": "'"${COUNTRY}"'"
    }
  }'

echo
