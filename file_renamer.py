import glob
import os
import uuid
'''
Drop this file in the directory containing files you wish to rename.
For each file that contains an exclamation point, it will rename
the file by removing everything up to and including the first
exclamation point.

The file generates a log report summarizing the successfully
renamed files as well as any files where an OSError exception was raised.
'''
def make_report(x):
    # x is a list
    status_log_filename = 'renamer_log_' + str(uuid.uuid4()) + '.txt'
    f = open(status_log_filename, 'w')
    for item in x:
        f.write(item)
        f.write('n')
    f.close()

def main():
    status_log = []
    for f in glob.glob('*.*'):
        if ('file_renamer' in f) or ('!' not in f):
            pass
        else:
            try:
                target = f.find('!')
                new_filename = f[target+1:]
                os.rename(f, new_filename)
                status_log.append('Renamed %s as %s' %(f, new_filename))
            except OSError:
                status_log.append('An error occured with file %s' %f)

if __name__ == '__main__':
    main()
    make_report(status_log)