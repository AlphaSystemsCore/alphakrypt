table_definition = [
    """
    CREATE TABLE USERS(
        user_id UUID PRIMARY KEY DEFAULT generateuuid(),
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        middle_name VARCHAR(),
        email TEXT UNIQUE NOT NULL,
        hashed_password TEXT,
        status Status,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ,
        delete_at TIMESTAMPTZ,

    """,
]