#!/bin/sh
curl -X POST http://localhost:8888/v1/parent/1/child/2 -d '{"hello":"world"}'
