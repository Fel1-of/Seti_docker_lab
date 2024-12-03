CREATE TABLE IF NOT EXISTS redirects
(
  source_id SERIAL PRIMARY KEY,
  target_id INTEGER NOT NULL
);

.mode csv
.separator "\t"
.import /dev/stdin redirects
