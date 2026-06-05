-- Validation checks for products table migration

-- TODO: Check if table exists
-- SELECT EXISTS (
--     SELECT FROM information_schema.tables 
--     WHERE table_name = 'products'
-- );

-- TODO: Verify column count and types
-- SELECT column_name, data_type, is_nullable
-- FROM information_schema.columns
-- WHERE table_name = 'products'
-- ORDER BY ordinal_position;

-- TODO: Check constraints
-- SELECT constraint_name, constraint_type
-- FROM information_schema.table_constraints
-- WHERE table_name = 'products';

-- TODO: Verify indexes
-- SELECT indexname, indexdef
-- FROM pg_indexes
-- WHERE tablename = 'products';
