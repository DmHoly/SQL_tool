# Database SQL Tools

This repository contains a suite of tools and scripts for managing and interacting with SQL databases using SQLAlchemy. It includes examples of creating complex database structures, performing CRUD operations, reading metadata, and generating SQL queries dynamically.

## Features

- **Database Schema Creation**: Scripts to create complex database schemas with multiple levels of relationships using SQLAlchemy.
- **CRUD Operations**: Examples of Create, Read, Update, and Delete operations on the database.
- **Metadata Extraction**: Scripts to extract and display metadata from the database.
- **Dynamic SQL Query Generation**: Generate SQL queries based on the database metadata.
- **Graph Visualization**: Visualize database schema relationships as a graph using NetworkX and Matplotlib.

## Getting Started

### Prerequisites

- Python 3.7+
- SQLAlchemy
- SQLite (or any other SQL database you prefer)
- NetworkX
- Matplotlib

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/database-sql-tools.git
    cd database-sql-tools
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

### Directory Structure (to be updated)

- `schemas/`: Scripts to create various database schemas.
- `data/`: Sample data and scripts to insert data into the database.
- `metadata/`: Scripts to extract and display database metadata.
- `queries/`: Scripts to generate dynamic SQL queries based on metadata.
- `visualization/`: Scripts to visualize database schema relationships.

## Example Scripts

### generate_query.py

This script reads the metadata from your database and generates a SQL `SELECT` query based on the relationships and foreign keys. Here is an example of how it works:

```python
To be updated
