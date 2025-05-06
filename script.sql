-- Create users table
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email TEXT NOT NULL,
    name TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Create chat_sessions table
CREATE TABLE chat_sessions (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    title TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create chat_messages table
CREATE TABLE chat_messages (
    id UUID PRIMARY KEY,
    session_id UUID NOT NULL,
    content TEXT,
    role TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES chat_sessions(id)
);

-- Add indexes to improve query performance
CREATE INDEX idx_chat_sessions_user_id ON chat_sessions(user_id);
CREATE INDEX idx_chat_messages_session_id ON chat_messages(session_id);

-- Add unique constraint to prevent duplicate emails
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);