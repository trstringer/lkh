import os
import sys

def main():
    file_name = os.path.expanduser('~/.ssh/known_hosts')

    if not os.path.isfile(file_name):
        print('Unable to locate {}'.format(file_name))
        sys.exit(1)

    with open(file_name) as known_hosts_file:
        known_hosts = known_hosts_file.readlines()
        for line in known_hosts:
            host_name_or_names = line.split()[0]
            host_names = host_name_or_names.split(',')
            if len(host_names) == 1:
                print(host_names[0])
            else:
                print('{} ({})'.format(host_names[0], ', '.join(host_names[1:])))

