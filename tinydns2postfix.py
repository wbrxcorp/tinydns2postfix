#!/usr/bin/python2
import sys,optparse

def main(secondary_mx_address, zone_files):
    mx_records = []
    if not hasattr(zone_files, "__iter__"): zone_files = [zone_files]
    for zone_file in zone_files:
        for line in open(zone_file):
            if line[0] == '@':
                mx_records.append(line.strip().split(':'))

    domains = dict()
    for mx_record in mx_records:
        domain = mx_record[0][1:]
        ip_address = mx_record[1]
        name = mx_record[2]
        if name.endswith("."): name = name[:-1]
        priority = int(mx_record[3])
        if domain not in domains:
            domains[domain] = dict()

        if ip_address == secondary_mx_address:
            domains[domain]["act_as_secondary"] = True
        elif "primary_mx_name" is not domains[domain] or priority < domains[domain]["primary_mx_priority"]:
            domains[domain]["primary_mx_name"] = name
            domains[domain]["primary_mx_priority"] = priority

    for k,v in domains.items():
        if "act_as_secondary" not in v: continue
        #else
        print "%s\trelay:[%s]" % (k, v["primary_mx_name"])

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: %s <secondary mx address> <zone files>"
    main(sys.argv[1], sys.argv[2:])
