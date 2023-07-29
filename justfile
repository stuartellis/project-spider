pre-commit-check:
  @pre-commit run --all-files

pspider-down:
  @docker compose -f docker/apps/project-spider-backend/docker-compose.yml --env-file .env down

pspider-up:
  @docker compose -f docker/apps/project-spider-backend/docker-compose.yml --env-file .env up
