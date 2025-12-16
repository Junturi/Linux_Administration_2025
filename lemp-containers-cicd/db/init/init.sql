CREATE DATABASE IF NOT EXISTS cicd_db;

USE cicd_db;

CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nickname VARCHAR(50) NOT NULL,
            message TEXT NOT NULL,
            client_id VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_created (created_at),
            INDEX idx_nickname (nickname)
);