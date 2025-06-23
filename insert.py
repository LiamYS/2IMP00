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
                MERGE (m: Model {id: row.id})
                SET m.likes = CASE WHEN row.likes <> '' THEN toInteger(row.likes) ELSE NULL END,
                    m.downloads = CASE WHEN row.downloads <> '' THEN toInteger(row.downloads) ELSE NULL END,
                    m.pipeline_tag = CASE WHEN row.pipeline_tag <> '' THEN row.pipeline_tag ELSE NULL END,
                    m.license = CASE WHEN row.license <> '' THEN row.license ELSE NULL END,
                    m.library_name = CASE WHEN row.library_name <> '' THEN row.library_name ELSE NULL END,
                    m.model_type = CASE WHEN row.model_type <> '' THEN row.model_type ELSE NULL END,
                    m.created_at = CASE WHEN row.created_at <> '' THEN row.created_at ELSE NULL END
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
