drop table rm_login;
drop table client_login;
drop table client_wallet;
drop table transactions;
drop table holdings;
drop table client;
drop table rm;
drop table industry;
drop table product;


create table product
(product_id integer primary key,
product_name text,
unit_daily_credit_award numeric,
ESG_Rating text,
Sharpe_ration numeric);

create table industry
(industry_id integer primary key,
 industry_name text,
base_credit numeric);

create table rm
(rm_id numeric primary key,
rm_email text,
rm_name text,
rm_team text,
group_name text,
area_name text,
country_name text
pwd text);

create table client
(
client_id serial primary key,
client_name text,
industry_id integer references industry,
rm_id integer references rm,
pwd text);

create table holdings
(holding_id serial primary key,
product_id integer references product,
units_held numeric,
client_id integer references client,
daily_credit_award numeric);

create table transactions
(transaction_id serial primary key,
product_id integer references product,
units_traded numeric,
trade_type text,
time_stamp timestamp,
client_id integer references client);

create table rm_login
(
rm_id integer references rm,
username text primary key,
password text
);

create table client_login
(client_id integer references client,
username text primary key,
pwd text);

create table client_wallet
(
client_wallet_id serial primary key,
client_id integer references client,
total_daily_credit_award numeric,
total_credit numeric,
date_updated timestamp
);