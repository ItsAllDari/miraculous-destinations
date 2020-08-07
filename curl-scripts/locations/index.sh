#!/bin/bash

curl "http://localhost:8000/locations" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
