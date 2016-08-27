drop table if exists submissions;
create table submissions (
  id integer primary key autoincrement,
  date text,
  note text not null,
  email_address text not null
);
