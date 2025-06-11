from neo4j import GraphDatabase

URI = "neo4j://localhost"
AUTH = ("neo4j", "")
with GraphDatabase.driver(URI, auth=AUTH) as driver:
    try:
        # Drop existing database
        print("Dropping existing database...")
        driver.session().run("""
            MATCH (n)
                CALL (n) {
                DETACH DELETE n
            } IN TRANSACTIONS
        """)

        # Create constraints
        print("Creating constraints...")
        driver.session().run("""
            CREATE CONSTRAINT model_id IF NOT EXISTS
            FOR (m: Model) REQUIRE m.id IS UNIQUE;
        """)

        # Import models
        print("Importing models...")
        driver.session().run("""
            LOAD CSV WITH HEADERS FROM 'file:///models.csv' AS row FIELDTERMINATOR '|'
            CALL (row) {
                MERGE (m: Model {id: row.id, likes: toInteger(row.likes), downloads: toInteger(row.downloads), created_at: row.created_at})
            } IN CONCURRENT TRANSACTIONS
        """)

        # Import relationships
        print("Importing relationships...")
        driver.session().run("""
            LOAD CSV WITH HEADERS FROM 'file:///models.csv' AS row FIELDTERMINATOR '|'
            CALL (row) {
                WITH row, split(row.base_model, ',') AS base_models
                UNWIND base_models AS base_model
                MATCH (m: Model {id: row.id})
                MATCH (n: Model {id: base_model})
                MERGE (m)-[r:USES_BASE]->(n)
            } IN TRANSACTIONS
            ON ERROR CONTINUE
        """)

    except Exception as e:
        print(e)
