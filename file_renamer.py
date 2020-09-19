import glob
import os
from datetime import datetime
'''
Drop this file in the directory containing files you wish to rename.
For each file that contains an exclamation point, it will rename
the file by removing everything up to and including the first
exclamation point.

The file generates a log report summarizing the successfully
renamed files as well as any files where an OSError exception was raised.
'''
def make_report(l: list):
    current_time = datetime.now()
    status_log_filename = 'renamer_log_' + \
                          current_time.strftime("%Y-%m-%d_%H-%M-%S") + \
                          '.txt'
    with open(status_log_filename, 'w') as f:
        for item in l:
            f.write(item + '\n')

def main():
    status_log = []
    for old_filename in glob.glob('*.*'):
        if '!' in old_filename:
            try:
                target = old_filename.find('!')
                new_filename = old_filename[target+1:]
                os.rename(old_filename, new_filename)
                status_log.append(f'Renamed {old_filename} as {new_filename}.')
            except OSError:
                status_log.append(f'An error occured with file {old_filename}.')
    make_report(status_log)

if __name__ == '__main__':
    main()
