# Translation-Service

A translation dictionary REST API using Django and PostgreSQL.

# API Endpoints

## GET (/api/translation)

- **query params**: `language` (list separated by commas)
- **response**: existing translations for the given list of languages, sorted by `key`
- **rendering format**: `JSON`, `csv`

