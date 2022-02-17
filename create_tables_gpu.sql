drop table if exists Users;
create table Users (
    id integer primary key autoincrement,
    username varchar
);
drop table if exists Manufacturers;
create table Manufacturers(
    id integer primary key autoincrement,
    name varchar
);
drop table if exists GraphicCards;
create table GraphicCards(
    id integer primary key autoincrement,
    name varchar,
    owner_id integer,
    manufacturer_id integer,
    foreign key (owner_id) references Users (id) foreign key (manufacturer_id) references Manufacturers(id)
);
drop table if exists Wishlist;
create table Wishlist(
    id integer primary key autoincrement,
    item_id integer,
    user_id integer,
    amount integer,
    foreign key (item_id) references GraphicCards(id) foreign key (user_id) references Users(id)
);
drop table if exists Specs;
create table Specs(
    gpu_id integer primary key,
    model varchar,
    grade integer,
    foreign key (gpu_id) references GraphicCards(id)
);
drop table if exists UseCases;
create table UseCases (
    id integer primary key autoincrement,
    place varchar
);
drop table if exists User_UseCases;
create table User_UseCases(
    user_id integer,
    use_case_id integer,
    foreign key (user_id) references Users(id) foreign key (use_case_id) references UseCases(id)
);