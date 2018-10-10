create table dummy(
  dummy_id SERIAL PRIMARY KEY,
  new_name varchar(255),
  rudest_animal varchar(255),
  hotdog_sandwich varchar(255),
  one_more varchar(255),
  extra text,
  time_submit text
);

insert into dummy(new_name, rudest_animal, hotdog_sandwich, one_more, extra, time_submit) values ('Mickey Mouse', 'tiger', 'yes', 'no', ' ', '2018-07-29 09:17:13.812189');
