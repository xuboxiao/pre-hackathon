insert into rm (rm_id,rm_email ,rm_name ,team_name ,group_name ,area_name ,country_name ) values (1,'RM1@db.com','RM1','Team1','Group1','Area1','APAC');
insert into rm (rm_id,rm_email ,rm_name ,team_name ,group_name ,area_name ,country_name ) values (2,'RM2@db.com','RM2','Team2','Group1','Area1','APAC');
insert into rm (rm_id,rm_email ,rm_name ,team_name ,group_name ,area_name ,country_name ) values (3,'RM3@db.com','RM3','Team3','Group2','Area2','APAC');
insert into rm (rm_id,rm_email ,rm_name ,team_name ,group_name ,area_name ,country_name ) values (4,'RM4@db.com','RM4','Team4','Group2','Area2','APAC');


insert into industry (industry_id, industry_name,base_credit ) values (1,'Environmental Services and Recycling',90000);
insert into industry (industry_id, industry_name,base_credit ) values (2,'Forestry',90000);
insert into industry (industry_id, industry_name,base_credit ) values (3,'Waste Management and Green Energy',90000);
insert into industry (industry_id, industry_name,base_credit ) values (4,'Real Estate',0);
insert into industry (industry_id, industry_name,base_credit ) values (5,'Rubber and Tires',0);
insert into industry (industry_id, industry_name,base_credit ) values (6,'Retail Trade and Departmental stores',0);


insert into product (product_id, product_name,unit_daily_credit_award) values (1,'Tox free solutions',1);
insert into product (product_id, product_name,unit_daily_credit_award) values (2,'SolarCity Corporation',1);
insert into product (product_id, product_name,unit_daily_credit_award) values (3,'US Ecology',1);
insert into product (product_id, product_name,unit_daily_credit_award) values (4,'Citic Envirotech Ltd',1);
insert into product (product_id, product_name,unit_daily_credit_award) values (5,'Watawala Plantation',1);
insert into product (product_id, product_name,unit_daily_credit_award) values (6,'Solazyme',1);
insert into product (product_id, product_name,unit_daily_credit_award) values (7,'Goodyear Tires and Rubber',0);
insert into product (product_id, product_name,unit_daily_credit_award) values (8,'Bridgestone Corporation',0);
insert into product (product_id, product_name,unit_daily_credit_award) values (9,'Parkson Retail Group',0);
insert into product (product_id, product_name,unit_daily_credit_award) values (10,'Indiabulls Property Investements',0);

insert into client (client_id,client_name,industry_id,rm_id) values (1000,'Berkshire Hathaway Holdings',1,1);
insert into client (client_id,client_name,industry_id,rm_id) values (2000,'General Electric',3,2);
insert into client (client_id,client_name,industry_id,rm_id) values (3000,'JC Penny',6,3);
insert into client (client_id,client_name,industry_id,rm_id) values (4000,'TATA Group',4,4);

commit;







