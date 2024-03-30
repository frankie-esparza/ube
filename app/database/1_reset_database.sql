DROP USER order_up;
DROP DATABASE order_up_dev;

CREATE USER order_up WITH PASSWORD '9uCxydbt';
CREATE DATABASE order_up_dev WITH OWNER order_up;

