import psycopg2
import os

def create_table_db():
    createtable = """
        CREATE TABLE IF NOT EXISTS nasa_projects (
        project_id VARCHAR PRIMARY KEY,
        last_updated TIMESTAMP
    );
    """
    try:
        # Connect to PostgreSQL 
        with psycopg2.connect(
            dbname= os.getenv('DB_NAME'), 
            user= os.getenv('DB_USER'), 
            password= os.getenv('DB_PASSWORD'), 
            host= os.getenv('DB_HOST'), 
            port= os.getenv('DB_PORT')
        ) as conn:
            
            # Create a cursor object 
            with conn.cursor() as cursor:
                cursor.execute(createtable)
                conn.commit()

            print("Table created successfully.")
        
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    
    except Exception as e:
        print(f"Error: {e}")
    
def store_in_db(project_details):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname= os.getenv('DB_NAME'), 
            user= os.getenv('DB_USER'), 
            password= os.getenv('DB_PASSWORD'), 
            host= os.getenv('DB_HOST'), 
            port= os.getenv('DB_PORT')
        )
        cursor = conn.cursor()

        # Insert the project details
        insert_query = """
        INSERT INTO nasa_projects (project_id, last_updated)
        VALUES (%s, %s)
        ON CONFLICT (project_id) DO UPDATE 
        SET last_updated = EXCLUDED.last_updated;
        """
        cursor.executemany(insert_query, project_details)
        
        # Commit the transaction
        conn.commit()

        print(f"{cursor.rowcount} records inserted/updated successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()


