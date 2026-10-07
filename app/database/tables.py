table_definition = [
    """
    CREATE TABLE USERS(
        user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        middle_name VARCHAR(),
        email TEXT UNIQUE NOT NULL,
        credential_id UUID NOT NULL,
        status to define later,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ,
        delete_at TIMESTAMPTZ
        FOREIGN KEY (credential_id) REFERENCES (credential_id)

    """,
    """
    CREATE TABLE credentials(
        credential_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        hashed_password TEXT UNIQUE NOT NULL,
        status to define later
        created_at TIMESTAMPTZ DEFAULT NOW(),
        deleted_at TIMESTAMPTZ,
        updated_at TIMESTAMPTZ,
    )
    """,
]