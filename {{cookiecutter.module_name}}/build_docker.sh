#!/bin/bash
echo "Building docker image {{cookiecutter.module_name}}"
docker build . -t {{cookiecutter.project_name}}_{{cookiecutter.module_name}}:latest
