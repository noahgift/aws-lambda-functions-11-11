#!/usr/bin/env bash

aws lambda invoke 
	--function-name bucketcounter \
	--payload '{"number": 1}' \
	response.json