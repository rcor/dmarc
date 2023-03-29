from yoyo import step
import os
__depends__ = {}

steps = [
     step("CREATE TABLE report (report_id VARCHAR(20), org_name VARCHAR(20), file_name VARCHAR(20), date_begin timestamp, date_end timestamp, PRIMARY KEY (report_id))",
         "DROP TABLE report"),
     step("""CREATE TABLE POLICY(
               policy_id serial,
               report_id VARCHAR(20) NOT NULL,
               domain VARCHAR(20),
               adkim VARCHAR(20),
               aspf VARCHAR(20),
               p VARCHAR(20),
               sp VARCHAR(20),
               pct VARCHAR(20),
               FOREIGN KEY (report_id)
                     REFERENCES report (report_id) 
           )
          """,
          "DROP TABLE POLICY;"),
     step("""CREATE TABLE reports_info (
                reports_info_id serial,report_id VARCHAR(20) NOT NULL,
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
                FOREIGN KEY (report_id)
                     REFERENCES report (report_id) 
          ) """,
          "DROP TABLE reports"),
]
