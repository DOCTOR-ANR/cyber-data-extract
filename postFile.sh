#!/bin/bash

curl -F file=@examples/$1 http://localhost:5000/topology

