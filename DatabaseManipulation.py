import sqlite3

connected = sqlite3.connect('Database.db')
cursor = connected.cursor()

def check_for_table(table):
    """
    Checks if the given table exists in the database. If it does not exist, creates it.

    Args:
        table_name (str): The name of the table to check.

    Returns:
        bool: True if the table existed, False if it did not.
    """
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'"
    cursor.execute(query)

    if not cursor.fetchone():
        create_table_query = f"""
            CREATE TABLE {table} (
                id          INTEGER PRIMARY KEY,
                name        TEXT NOT NULL,
                description TEXT NOT NULL,
                programmers TEXT NOT NULL,
                link        TEXT NOT NULL
            )
        """
        cursor.execute(create_table_query)
        connected.commit()

        return False

    return True
    
def get_table(table):
    """
    Retrieves the first record in the given table.

    Args:
        table (str): The name of the table to retrieve the record from.

    Returns:
        tuple: The first record in the given table. If the table is empty, returns None.
    """
    check_for_table(table)
    cursor.execute(f"SELECT * FROM {table}")

    return cursor.fetchone()

def remove_record(table_name, id):
    """
    Adds a new record to the given table.

    Args:
        table_name (str): The name of the table to add the record to.
        name (str): The name of the resource.
        description (str): A description of the resource.
        programmers (str): A string containing the names of the resource's programmers, separated by commas.
        link (str): The URL of the resource.

    Returns:
        None
    """
    check_for_table(table_name)

    cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (id,))
    connected.commit()

def add_record(table_name, name, description, programmers, link):
    """
    Removes an existing record to the given table.

    Args:
        table_name (str): The name of the table to remove the record from.
        name (str): The name of the resource.
        description (str): A description of the resource.
        programmers (str): A string containing the names of the resource's programmers, separated by commas.
        link (str): The URL of the resource.

    Returns:
        None
    """
    check_for_table(table_name)

    cursor.execute(f"INSERT INTO {table_name} (name, description, programmers, link) VALUES (?, ?, ?, ?)", (name, description, programmers, link))
    connected.commit()

def update_record(table_name, id, property, value):
    """
    Updates a record in the given table with the given property and value.

    Args:
        table_name (str): The name of the table to update the record in.
        id (int): The id of the record to update.
        property (str): The name of the record's property to update.
        value (str): The new value of the record's property.

    Returns:
        bool: True if the record was successfully updated, False if it was not.
    """
    if not check_for_table(table_name):
        return False

    cursor.execute(f"UPDATE {table_name} SET ? = ? WHERE id = ?", (property, value, id))
    connected.commit()

    return True

def get_records(table_name):
    """
    Retrieves all records in the given table.

    Args:
        table_name (str): The name of the table to retrieve the records from.

    Returns:
        list: A list of tuples, where each tuple is a record in the given table.
    """
    check_for_table(table_name)
    
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    
    return result

def get_record(table_name, id):
    """
    Retrieves a record from the given table with the given id.

    Args:
        table_name (str): The name of the table to retrieve the record from.
        id (int): The id of the record to retrieve.

    Returns:
        tuple: The record with the given id, or None if no record was found.
    """
    check_for_table(table_name)
    
    cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (id,))
    result = cursor.fetchone()
    
    return result
