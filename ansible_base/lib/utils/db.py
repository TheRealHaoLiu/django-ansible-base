from django.db import connection
from django.db.migrations.executor import MigrationExecutor


def migrations_are_complete():
    executor = MigrationExecutor(connection)
    plan = executor.migration_plan(executor.loader.graph.leaf_nodes())
    return not bool(plan)
