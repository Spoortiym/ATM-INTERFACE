import mysql.connector
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
db_config = {
    'host': os.environ.get('MYSQL_HOST', 'localhost'),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'password': os.environ.get('MYSQL_PASSWORD', '#Spoorti8088'),
    'port': int(os.environ.get('MYSQL_PORT', 3306))
}

def init_db():
    try:
        # First connect without database to create it if it doesn't exist
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create database if it doesn't exist
        db_name = os.environ.get('MYSQL_DATABASE', 'atm_db')
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                card_number VARCHAR(16) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                pin VARCHAR(4) NOT NULL,
                balance DECIMAL(10,2) DEFAULT 0.00,
                account_type VARCHAR(20) NOT NULL,
                blocked BOOLEAN DEFAULT FALSE,
                blocked_time DATETIME,
                pin_attempts INT DEFAULT 0
            )
        """)
        
        # Create transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                card_number VARCHAR(16) NOT NULL,
                transaction_type VARCHAR(20) NOT NULL,
                amount DECIMAL(10,2) NOT NULL,
                balance DECIMAL(10,2) NOT NULL,
                transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (card_number) REFERENCES users(card_number)
            )
        """)
        
        # Insert a test user if none exists
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO users (card_number, password, pin, balance, account_type)
                VALUES ('1234567890123456', 'test123', '1234', 1000.00, 'Savings')
            """)
        
        conn.commit()
        logger.info("Database initialized successfully")
        
    except mysql.connector.Error as err:
        logger.error(f"Database initialization error: {err}")
        raise
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    init_db() 