#!/bin/sh
curl -X POST http://localhost:8888/v1/parent/1/child -d '{"hello":"world"}'
