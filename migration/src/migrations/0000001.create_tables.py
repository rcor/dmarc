from yoyo import step
import os
__depends__ = {}

steps = [
    step("CREATE TABLE metadata (metadata_id VARCHAR(20), org_name VARCHAR(20), file_name VARCHAR(20), date_begin timestamp, date_end timestamp, PRIMARY KEY (metadata_id))",
         "DROP TABLE metadata"),
    step("""CREATE TABLE reports (
                report_id serial,metadata_id VARCHAR(20) NOT NULL,
                source_ip VARCHAR(20), 
                _count NUMERIC, 
                policy_evaluated_disposition VARCHAR(20),
                policy_evaluated_dkim VARCHAR(20),
                policy_evaluated_spf VARCHAR(20),
                identifiers_header_from VARCHAR(20),
                auth_results_dkim_domain VARCHAR(20),
                auth_results_dkim_result VARCHAR(20),
                auth_results_dkim_selector VARCHAR(20),
                auth_results_spf_domain  VARCHAR(20),
                auth_results_spf_result VARCHAR(20),
                FOREIGN KEY (metadata_id)
                     REFERENCES metadata (metadata_id) 
          ) """,
          "DROP TABLE reports"),
]
