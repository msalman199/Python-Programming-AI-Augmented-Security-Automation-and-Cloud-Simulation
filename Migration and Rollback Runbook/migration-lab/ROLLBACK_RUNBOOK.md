# Database Migration Rollback Runbook

## Overview
This runbook provides step-by-step procedures for rolling back database migrations safely.

## Pre-Rollback Checklist

- [ ] Identify the migration to rollback
- [ ] Verify backup exists and is valid
- [ ] Check current database state
- [ ] Notify stakeholders of rollback operation
- [ ] Ensure maintenance window is active
- [ ] Document reason for rollback

## Rollback Procedure

### Step 1: Assess Current State
```bash
# Check migration history
psql -c "SELECT * FROM migration_history ORDER BY executed_at DESC LIMIT 5;"

# Verify current schema version
psql -c "\dt"
