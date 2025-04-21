CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,             -- e.g., "Rams"
    market TEXT,                    -- e.g., "Los Angeles"
    full_name TEXT UNIQUE,          -- e.g., "Los Angeles Rams"
    alias TEXT,                     -- e.g., "LA"
    abbreviation TEXT,              -- e.g., "LAR"
    conference TEXT,                -- e.g., "NFC"
    division TEXT                   -- e.g., "West"
    wins INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0,       -- Total wins/losses in the season
    ties INTEGER DEFAULT 0,        -- Total ties in the season
);

CREATE TABLE games (
    id TEXT PRIMARY KEY,            -- Sportradar Game ID
    week INTEGER NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    home_score INTEGER,
    away_score INTEGER,
    status TEXT                     -- e.g., "scheduled", "completed"
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL     -- bcrypt or similar
);

CREATE TABLE user_picks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    week INTEGER NOT NULL,
    team_name TEXT NOT NULL,        -- e.g., "Los Angeles Rams"
    result TEXT DEFAULT 'pending'   -- 'win', 'loss', 'pending'
);

CREATE INDEX idx_user_picks_user_week ON user_picks(user_id, week);
CREATE INDEX idx_games_week ON games(week);
