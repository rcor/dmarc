from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE metadata (metadata_id VARCHAR(20), org_name VARCHAR(20), file_name VARCHAR(20), date_begin timestamp, date_end timestamp, PRIMARY KEY (id))",
         "DROP TABLE metadata"),
    step("CREATE TABLE reports (report_id serial,metadata_id VARCHAR(20) NOT NULL,, FOREIGN KEY (metadata_id) REFERENCES metadata (metadata_id) ) ","DROP TABLE reports"),
]


