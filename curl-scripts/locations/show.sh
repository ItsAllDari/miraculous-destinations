#!/bin/bash

curl "http://localhost:8000/locations/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
