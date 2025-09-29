"""
Each function in this file is the name of a table or dataset.
"""
import itertools
from .transform import with_bbl, to_csv, skip_fields
from .annual_sales import AnnualSales

def ecb_violations(dataset):
    return with_bbl(to_csv(dataset.files[0].dest), borough='boro')


def dob_violations(dataset):
    return with_bbl(to_csv(dataset.files[0].dest), borough='boro')


def dob_complaints(dataset):
    return to_csv(dataset.files[0].dest)

def dof_sales(dataset):
    return with_bbl(to_csv(dataset.files[0].dest))


def dobjobs(dataset):
    return with_bbl(to_csv(dataset.files[0].dest))


def dob_now_jobs(dataset):
    return with_bbl(skip_fields(to_csv(dataset.files[1].dest), [s.lower() for s in dataset.schemas[1]['skip']]))

def acris(dataset, schema):
    dest_file = next(filter(lambda f: schema['table_name'] in f.dest, dataset.files))
    _to_csv = to_csv(dest_file.dest)
    if 'skip' in schema:
        return skip_fields(_to_csv, [s.lower() for s in schema['skip']])
    else:
        return _to_csv

def dof_annual_sales(dataset):
    return itertools.chain(*[with_bbl(AnnualSales(f.dest)) for f in dataset.files])