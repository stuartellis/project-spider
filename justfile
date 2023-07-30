#!/usr/bin/env just --justfile
#
# Project Configuration for Just Task Runner
#
# See: https://just.systems/man/en/

alias check := pre-commit-check
alias down := pspider-down
alias up := pspider-up

# Lists available recipes
default:
    @just --list

# Shows system information
info:
    @echo "CPU Architecture: {{ arch() }}"
    @echo "OS Type: {{ os_family() }}"
    @echo "OS: {{ os() }}"

# Runs pre-commit on all files
pre-commit-check:
    @pre-commit run --all-files

# Stops Docker Compose for backend
pspider-down:
    @docker compose -f docker/apps/project-spider-backend/docker-compose.yml --env-file .env down

# Starts Docker Compose for backend
pspider-up:
    @docker compose -f docker/apps/project-spider-backend/docker-compose.yml --env-file .env up
