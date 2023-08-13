create table pessoa (
  id uuid DEFAULT uuid_generate_v4() not null,
  apelido varchar(32) not null,
  nome varchar(100) not null,
  nascimento date not null,
  stack varchar(32)[],
  primary key (id)
);