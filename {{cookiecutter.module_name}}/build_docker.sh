#!/bin/bash
echo "Building docker image {{cookiecutter.module_name}}"
docker build . -t zephyr_{{cookiecutter.module_name}}:latest
