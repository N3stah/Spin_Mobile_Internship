import os
import psycopg2
from dotenv import load_dotenv

# Construct the absolute path to the .env file in the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')

# Load environment variables explicitly from that path
load_dotenv(dotenv_path=env_path, override=True)


class DatabaseManager:
    """Encapsulates PostgreSQL database connection and queries."""

    def __init__(self):
        # Fetch credentials and .strip() invisible spaces
        self.db_name = os.getenv("DB_NAME", "").strip()
        self.db_user = os.getenv("DB_USER", "").strip()
        self.db_password = os.getenv("DB_PASSWORD", "").strip()
        self.db_host = os.getenv("DB_HOST", "").strip()
        self.db_port = os.getenv("DB_PORT", "").strip()
        self.connection = None

    def connect(self):
        """Establish a connection to the PostgreSQL database."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            print("✓ Successfully connected to the database.")
        except psycopg2.OperationalError as e:
            print(f"⚠ Database connection failed: {e}")

    def fetch_customers(self):
        """Retrieve and display all customers from the database."""
        try:
            # A cursor carries your SQL to the DB and brings the results back
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, name, email FROM customers;")

            # fetchall() returns a list of tuples: [(1, 'Mark', '...'), (2, 'Judy', '...')]
            records = cursor.fetchall()

            print("\n--- Customer List ---")
            for row in records:
                print(f"[{row[0]}] {row[1]} - {row[2]}")

            cursor.close()
        except Exception as e:
            print(f"⚠ Failed to fetch customers: {e}")

    def close(self):
        """Safely close the database connection."""
        if self.connection:
            self.connection.close()
            print("✓ Database connection closed.")


# Quick Manual Test
if __name__ == "__main__":
    db = DatabaseManager()
    db.connect()

    # Only try to fetch if the connection actually succeeded!
    if db.connection:
        db.fetch_customers()
        db.close()