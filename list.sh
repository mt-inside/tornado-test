#!/bin/sh
curl -X GET 'http://localhost:8888/v1/parent/1/child?hello=world'
curl -X GET 'http://localhost:8888/v1/parent/abc/child?hello=world'
