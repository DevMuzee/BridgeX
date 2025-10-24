-- SELECT column_name, data_type
-- FROM information_schema.columns
-- WHERE table_name = 'users_config'

-- SELECT * FROM users_config

--- getting all the table in a database
-- SELECT table_schema, table_name
-- FROM information_schema.tables
-- WHERE table_type= 'BASE TABLE'
-- ORDER BY table_schema, table_name

--getting a table name in public schema
SELECT table_name
FROM information_schema.tables
WHERE table_schema ='public'
ORDER BY table_name