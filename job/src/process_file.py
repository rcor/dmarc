import sys
import os
from zipfile import ZipFile
import xml.etree.ElementTree as ET

def uncompresFile(origin,dest):
    with ZipFile(origin,'r') as zObject:
        zObject.extractall(dest)


def loadData(path):
    return 0

def getFiles(dir_path,ext):
    res = []
    for path in os.listdir(dir_path):
    # check if current path is a file
        if path != None and ext in path:
            if os.path.isfile(os.path.join(dir_path, path)):
                res.append(path)
    return res

def process_file(file):
    with open(file,'r',encoding='utf-8') as xml_file:
        cache = xml_file.read()
        data = ET.fromstring(cache)
        metadata = report_metadata(data)
        metadata['file_name']=xml_file.name.split('/')[-1]
        policy=policy_published(data)
        records=reported_records(data)
        print(metadata)
        print(policy)
        print(records)

def reported_records(data):
    records=data.findall('./record')
    metadata_records=[]
    for record in records:
        source_ip=record.find('row/source_ip')
        count=record.find('row/count')

        policy_evaluated_disposition=record.find('row/policy_evaluated/disposition')
        policy_evaluated_dkim=record.find('./row/policy_evaluated/dkim')
        policy_evaluated_spf=record.find('./row/policy_evaluated/spf')

        identifiers_header_from=record.find('./identifiers/header_from')

        auth_results_dkim_domain=record.find('./auth_results/dkim/domain')
        auth_results_dkim_result=record.find('./auth_results/dkim/result')
        auth_results_dkim_selector=record.find('./auth_results/dkim/selector')
        auth_results_spf_domain=record.find('./auth_results/spf/domain')
        auth_results_spf_result=record.find('./auth_results/spf/result')
        metadata={
            'source_ip':source_ip.text, 
            'count':count.text,

            'policy_evaluated_disposition':policy_evaluated_disposition.text,
            'policy_evaluated_dkim':policy_evaluated_dkim.text,
            'policy_evaluated_spf':policy_evaluated_spf.text,

            'identifiers_header_from':identifiers_header_from.text,

            'auth_results_dkim_domain':auth_results_dkim_domain.text,
            'auth_results_dkim_result':auth_results_dkim_result.text,
            'auth_results_dkim_selector':auth_results_dkim_selector.text,
            'auth_results_spf_domain':auth_results_spf_domain.text,
            'auth_results_spf_result':auth_results_spf_result.text
        }
        print(metadata)
        metadata_records.append(metadata)
    return metadata_records
        
def report_metadata(data):
    report_id=data.findall("./report_metadata/report_id")[0]
    org_name=data.findall("./report_metadata/org_name")[0]
    date_range_begin=data.findall("./report_metadata/date_range/begin")[0]
    date_range_end=data.findall("./report_metadata/date_range/end")[0]
    metadata = {
        'report_id':report_id.text,
        'org_name':org_name.text,
        'date_range_begin':date_range_begin.text,
        'date_range_end':date_range_end.text
    }
    return metadata

def policy_published(data):
    domain=data.findall("./policy_published/domain")[0]
    adkim=data.findall("./policy_published/adkim")[0]
    aspf=data.findall("./policy_published/aspf")[0]
    p=data.findall("./policy_published/p")[0]
    sp=data.findall("./policy_published/sp")[0]
    pct=data.findall("./policy_published/pct")[0]
    metadata = {
        'domain':domain.text,
        'adkim':adkim.text,
        'aspf':aspf.text,
        'p':p.text,
        'sp':sp.text,
        'pct':pct.text
    }
    return metadata
