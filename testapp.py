import subprocess


process = subprocess.Popen(['rm', 'utils/CLAS12OCR.db'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

print(stdout)

process = subprocess.Popen(['python2', 'utils/create_database.py','--lite=utils/CLAS12OCR.db'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

print(stdout)


"""
cd utils
rm CLAS12OCR.db
python2 create_database.py --lite=CLAS12OCR.db
cd ../client
python2 src/SubMit.py --lite=../utils/CLAS12OCR.db -u=robertej scard_type1.txt
python2 src/SubMit.py --lite=../utils/CLAS12OCR.db -u=robertej scard_type2.txt
cd ..
cd utils
sqlite3 CLAS12OCR.db 'SELECT user FROM SUBMISSIONS';
cd ../server/src
python2 Submit_UserSubmission.py -b 2 --lite=../../utils/CLAS12OCR.db
sqlite3 ../../utils/CLAS12OCR.db 'SELECT user FROM SUBMISSIONS';
#which condor_submit if val = 0, do not submit, print not found message
"""