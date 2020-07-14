rm -rf clas12-test
mkdir clas12-test
cd clas12-test

git clone git@github.com:robertej19/client.git
git clone git@github.com:robertej19/server.git
git clone git@github.com:robertej19/utils.git

/usr/bin/python2 utils/create_database.py --lite=utils/CLAS12OCR.db
/usr/bin/python2 client/src/SubMit.py --lite=utils/CLAS12OCR.db -u=testuser client/scards/scard_type1.txt
cd server/src
/usr/bin/python2 Submit_UserSubmission.py --lite=../../utils/CLAS12OCR.db -b 1 -w -s -t 
