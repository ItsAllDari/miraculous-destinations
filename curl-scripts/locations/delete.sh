#!/bin/bash

curl "http://localhost:8000/locations/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
