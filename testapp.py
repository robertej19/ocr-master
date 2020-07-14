import subprocess



class command_class:
	def __init__(self,command_name,command_string,expected_output):
		self.name = command_name
		self.command = command_string
		self.expect_out = expected_output





def test_function(command):
	process = subprocess.Popen(command.command,
		stdout=subprocess.PIPE, 
		stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()


	if command.expect_out != '0':
		if stdout == command.expect_out:
			return(stdout,stderr)
		else:
			return(stdout, stderr + "unexpected sdtout of: " + stdout)
	else:
		return(stdout,stderr)


rm_sqlite_db = command_class('Remove Old SQLite DB',
								['rm','utils/CLAS12OCR.db'],
								'0')


create_sqlite_db = command_class('Create SQLite DB',
								['python2', 'utils/create_database.py','--lite=utils/CLAS12OCR.db'],
								'0')

submit_scard_1 = command_class('Submit scard 1 on client',
								['python2', 'client/src/SubMit.py','--lite=utils/CLAS12OCR.db','-u=robertej','client/scard_type1.txt'],
								'0')

submit_scard_2 = command_class('Create scard 2 on client',
								['python2', 'client/src/SubMit.py','--lite=utils/CLAS12OCR.db','-u=robertej','client/scard_type2.txt'],
								'0')

verify_submission_success = command_class('Verify scard submission success',
								['sqlite3','utils/CLAS12OCR.db','SELECT user FROM submissions WHERE user_submission_id=1'],
								'robertej\n')


command_sequence = [rm_sqlite_db,create_sqlite_db, submit_scard_1, submit_scard_2,verify_submission_success]


def run_through_tests(command_sequence):
	err_sum = 0 
	for command in command_sequence:
		out, err = test_function(command)
		print('Testing command: {0}'.format(command.name))
		if not err:
			print('... success')
			print(out)
		else:
			print('... fail, error message:')
			print(err)
			err_sum += 1
			
	return err_sum



status = run_through_tests(command_sequence)
if status > 0:
	exit(1)
else:
	exit(0)


"""
cd ../server/src
python2 Submit_UserSubmission.py -b 2 --lite=../../utils/CLAS12OCR.db
sqlite3 ../../utils/CLAS12OCR.db 'SELECT user FROM SUBMISSIONS';
#which condor_submit if val = 0, do not submit, print not found message
"""