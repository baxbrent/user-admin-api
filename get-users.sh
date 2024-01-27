#!/bin/bash

curl http://localhost:8888/users | python3 -m json.tool
