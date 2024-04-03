DROP DATABASE order_up_dev;
DROP USER order_up;

CREATE USER order_up WITH PASSWORD '9uCxydbt';
CREATE DATABASE order_up_dev WITH OWNER order_up;

