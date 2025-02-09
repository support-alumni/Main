DROP SCHEMA IF EXISTS sch_alumni CASCADE;
CREATE SCHEMA sch_alumni;
SET SEARCH_PATH TO sch_alumni;

DROP TABLE IF EXISTS tbl_alumni;
DROP TABLE IF EXISTS tbl_school;
DROP TABLE IF EXISTS tbl_experience;
DROP TABLE IF EXISTS tbl_location;


CREATE TABLE tbl_alumni
(
    aid_pk SERIAL PRIMARY KEY,
    profile_url VARCHAR(255) UNIQUE NOT NULL,
    aalumni VARCHAR(50) NOT NULL,
    alocation VARCHAR(50),
    amajor VARCHAR(50),
    agraduation_year CHAR(4),
    ajob_title VARCHAR(50),
    acertificate VARCHAR(50)
);


CREATE TABLE tbl_school
(
    sid_pk SERIAL PRIMARY KEY,
    aid_fk INT NOT NULL,
    suniversity_name VARCHAR(100),
    suniversity_major VARCHAR(50),
    suniversity_minor VARCHAR(50),
    suniversity_location VARCHAR(100),
    suniversity_start DATE,
    suniversity_end DATE,
    
    CONSTRAINT shcool_fk FOREIGN KEY(aid_fk) REFERENCES tbl_alumni(aid_pk) ON DELETE CASCADE
);


CREATE TABLE tbl_experience
(
    eid_pk SERIAL PRIMARY KEY,
    aid_fk INT NOT NULL,
    etitle VARCHAR(50),
    ecompany_name VARCHAR(50),
    ecompany_location VARCHAR(50),
    ecompany_size INT,
    etitle_start DATE,
    etitle_end DATE,
    
    CONSTRAINT experience_fk FOREIGN KEY(aid_fk) REFERENCES tbl_alumni(aid_pk) ON DELETE CASCADE
);


CREATE TABLE tbl_location
(
    lid_pk SERIAL PRIMARY KEY,
    aid_fk INT NOT NULL,
    lcountry VARCHAR(50),
    lstate VARCHAR(50),
    lzip VARCHAR(10),
    lcity VARCHAR(50),
    
    CONSTRAINT location_fk FOREIGN KEY(aid_fk) REFERENCES tbl_alumni(aid_pk) ON DELETE CASCADE
);
