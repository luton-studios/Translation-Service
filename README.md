# Translation-Service

A translation dictionary REST API using Django and PostgreSQL.

# API Endpoints

## GET (/api/translation)

- **query params**: `language` (list separated by commas)
- **response**: existing translations for the given list of languages, sorted by `key`
- **rendering format**: `JSON`, `csv`

## csv upload (/api/upload-csv)

- **format**: `key`, `language`, `phrase`
- **response**: sucess or failure
- insert new translations into db and/or modify existing translations
  - if an existing translation is updated, all previous translations of the same key will be cleared



