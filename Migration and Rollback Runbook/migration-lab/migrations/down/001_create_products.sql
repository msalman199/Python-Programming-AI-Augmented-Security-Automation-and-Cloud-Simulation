-- Rollback: Drop products table
BEGIN;
DROP TABLE IF EXISTS products CASCADE;
COMMIT;
