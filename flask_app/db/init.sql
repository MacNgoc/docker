ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'Abc123az';
FLUSH PRIVILEGES;


DROP DATABASE IF EXISTS db_flask;
CREATE DATABASE db_flask;
use db_flask;

CREATE TABLE user (
  firstname VARCHAR(20),
  lastname VARCHAR(20)
);

INSERT INTO user
  (firstname, lastname)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');