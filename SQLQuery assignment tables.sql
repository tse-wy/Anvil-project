
--table 1 for available tickets

create table tickets(
ticket_type char(100) primary key,
available_tickets int,
price_per_ticket int
);

insert into tickets (ticket_type, available_tickets, price_per_ticket)
values ('economy', 30, 100),
       ('premium_economy', 20, 200),
       ('first_class', 10, 300);

select * from tickets 

--table 2 for customer
--decimal for £value to keep it as a numeric value for future function


-- Create the flight_customer table
CREATE TABLE flight_customer (
    first_name varchar(100),
    last_name varchar(100),
    email varchar(100) unique,
    number_of_tickets_booked int,
    economy int,
    premium_economy int,
    first_class int,
    price_total int,
    discount_total int,
    unique_ticket_code varchar(20) primary key,
    foreign key (email) references users(email)
);

select * from flight_customer

insert into flight_customer (first_name, last_name, email, number_of_tickets_booked, economy, premium_economy, first_class, price_total, discount_total, unique_ticket_code)
values ('John', 'Doe', 'johndoe@hotmail.com', 1, 0, 0, 0, 100, 100, 'UTC112233'),
       ('Jane', 'Doe', 'janedoe@gmail.com', 5, 0, 4, 1, 110, 660, 'UTC445566');

--table 3 for feedback -- refer to anvil guide to implement, this may be the join table

CREATE TABLE feedback (
    first_name varchar(100),
    last_name varchar(100),
    email varchar(100),
    number_of_tickets_booked int,
    unique_ticket_code varchar(20),
    feedback varchar(300),
    response varchar(300),
    foreign key (email) references users(email)
);
select * from feedback

INSERT INTO feedback (first_name, last_name, email, number_of_tickets_booked, unique_ticket_code, feedback, response)
VALUES ('John', 'Doe', 'johndoe@hotmail.com', 1, 'UTC112233', 'I paid twice by mistake', NULL);	   
--VALUES ('Bart', 'Simpson', 'bartsimpson@gmail.com', NULL, 'UTC112233','Cannot book ticket', 'All tickets are sold out');
--VALUES ('Peter', 'Griffin', 'petergiffin@hotmail.co.uk', NULL,2 , 'How to book a ticket', NULL);


select * from feedback

--dummy feedback table


 
CREATE TABLE feedback_dummy (
    first_name varchar(100),
    last_name varchar(100),
    email varchar(250) primary key,
    number_of_tickets_booked int,
    unique_ticket_code varchar(20),
	subject_fb varchar (70),
    feedback varchar(300),
    response varchar(300)
);
INSERT INTO feedback_dummy (first_name, last_name, email, number_of_tickets_booked, unique_ticket_code, subject_fb, feedback, response)
--VALUES ('John', 'Doe', 'johndoe@hotmail.com', 1, 'UTC112233', 'I paid twice by mistake', 'I paid twice by mistake', NULL);
--VALUES ('Bart', 'Simpson', 'bartsimpson11@gmail.com', NULL, 0, 'Cannot book ticket', 'Cannot book ticket', 'All tickets are sold out');
--VALUES ('Peter', 'Griffin', 'petergiffin@hotmail.co.uk', NULL,2, 'How to book ticket', 'How to book a ticket', NULL);
 select * from feedback_dummy


create table dummy_tickets_1(
ticket_type char(100) primary key,
available_tickets int,
price_per_ticket int 
);

create table dummy_flight_customer (
first_name varchar(100),
last_name varchar(100),
email varchar (250) unique,
pass_w varchar (250),
number_of_tickets_booked int,
economy int,
premium_economy int,
first_class int,
price_total decimal(10, 2),
discount_total decimal(10, 2),
unique_ticket_code varchar(20) primary key
);


select * from dummy_flight_customer
drop table dummy_flight_customer

---
select * from tickets
select * from flight_customer
select * from feedback

select * from flight_customer where number_of_tickets_booked = 5

select * from flight_customer where price_total > 500 or number_of_tickets_booked = 1

select * from flight_customer order by discount_total asc;

select * from flight_customer order by discount_total desc;

select * from feedback order by last_name asc;

select avg (available_tickets) as average_available_tickets
from tickets; --avg tickets that are available

select avg (price_total) as average_total_price
from flight_customer; --avg price total

select avg(discount_total) as average_discount_total
from flight_customer; --avg discount

select fc.first_name, fc.last_name, fc.email, fc.number_of_tickets_booked, fc.unique_ticket_code, fb.subject_fb, fb.feedback, fb.response
from flight_customer fc
inner join feedback fb on fc.unique_ticket_code = fb.unique_ticket_code
where fc.unique_ticket_code = 'please enter code'; --used for retrieving the specific info via the ticket code e.g UTC112233 joining feedback fc tables

--group bys
select ticket_type, avg (available_tickets) as avg_available_tickets
from tickets
group by ticket_type;

--Group by flight customers by number of tickets booked and calculating the average price total and discount total 
select number_of_tickets_booked, avg(price_total) as avg_price_total, avg(discount_total) as avg_discount_total
from flight_customer
group by number_of_tickets_booked;

--Grouping feedback by subject and calculating the no. of feedbacks for each subject fb
select subject_fb, count(*) as feedback_count
from feedback
group by subject_fb;

 -- join find the feedback with a customer that has paid and have a unique code
select fc.first_name, fc.last_name, fc.email, fb.subject_fb, fb.feedback
from flight_customer fc
inner join feedback fb on fc.unique_ticket_code = fb.unique_ticket_code;

--Assigning user access

CREATE TABLE users (
    first_name varchar(100),
    last_name varchar(100),
    email varchar(100) primary key,
    password varchar(100) not null,
    user_role varchar(50)
);
select * from users

insert into users (first_name, last_name, email, password, user_role)
--values ('John', 'Doe', 'johndoe@hotmail.com', 'letmein12345', 'customer');
--values ('Jane', 'Doe', 'janedoe@gmail.com', 'letmein54321', 'customer');
--values (null, null, 'Admin1', 'adminpass','admin');
--values ('Bart', 'Simpson', 'bartsimpson@gmail.com', 'password123', 'customer');
--VALUES ('Peter', 'Griffin', 'petergiffin@hotmail.co.uk', 'password123', 'customer');


--query for joinging user and feedback tables based on email to get feedback details
select u.first_name, u.last_name, u.email, f.subject_fb, f.feedback, f.response
from users u
join feedback f on u.email = f.email;

--join user and flight_customer table based on email to get customer and ticket booking details
select u.first_name, u.last_name, u.email, fc.number_of_tickets_booked, fc.economy, fc.premium_economy, fc.first_class
from users u
join flight_customer fc on u.email = fc.email;


-- retreive booking details by each unique code, including the fb if it is there. and include all booking info
select fc.first_name, fc.last_name, fc.email, fc.number_of_tickets_booked, fc.economy, fc.premium_economy, fc.first_class, f.subject_fb, f.feedback, f.response
from flight_customer fc
inner join feedback f on fc.unique_ticket_code = f.unique_ticket_code;


create table dummy_users (
    first_name varchar(100),
    last_name varchar(100),
    email varchar(100) primary key,
    password varchar(100) not null,
    user_role varchar(50)
);

select * from dummy_users


--view

-- Create a view to calculate the total number of tickets booked
CREATE VIEW vw_total_tickets_booked
AS
SELECT SUM(number_of_tickets_booked) AS total_tickets_booked
FROM flight_customer;

-- Query the view to retrieve the total number of tickets booked
SELECT total_tickets_booked
FROM vw_total_tickets_booked;

select * from dummy_feedback
