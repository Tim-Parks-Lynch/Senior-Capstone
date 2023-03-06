DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  company TEXT NOT NULL,
  loc TEXT NOT NULL
);

INSERT INTO 
        jobs(id, title, company, loc)
VALUES
        (1, "Test Title", "Test Company", "Test Location");