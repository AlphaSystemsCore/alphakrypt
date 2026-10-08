table_definition = [
    """
    CREATE TYPE roles AS EMUN ('admin', 'user', 'moderator', 'developer') 
    """,
    """
    CREATE TYPE users_status AS 
    """,
    """
    CREATE TABLE users(
        user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        middle_name VARCHAR(),
        email TEXT UNIQUE NOT NULL,
        role to define later DEFAULT 'user',
        credential_id UUID NOT NULL,
        status to define later,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ,
        delete_at TIMESTAMPTZ
        FOREIGN KEY (credential_id) REFERENCES credential(credential_id)

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

    """
    CREATE TABLE files_metadata(
    file_metadata_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_id UUID NOT NULL,
    original_filename TEXT NOT NULL,
    storage_key TEXT NOT NULL,
    MIME_TYPE VARCHAR(100) NOT NULL,
    size VARCHAR(50) NOT NULL,
    checksum TEXT NOT NULL,
    status TEXT NOT NULL, 
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ,
    deleted_at TIMESTAMPTZ
    FOREIGN KEY (owner_id) REFERENCES users(user_id)
    );
    """
]