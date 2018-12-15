#-*- coding: utf-8 -*-

import pymssql
import json

class config:
	output_file = r"output.json"
	sql = '''
			select *
			from tblname
	'''

def db_connect():
	return pymssql.connect(server='SERVER-NAME', user='', password='', database='', charset='utf8')  

def main():
	with db_connect() as conn:
		with open(config.output_file, 'w') as fout:
			cur = conn.cursor(as_dict=True)
			cur.execute(config.sql)  
			row = cur.fetchone()

			trans_data(row, fout, cur)
	print('Done')

def trans_data(row, fout, cur):
	idx = 0
	while row:  
		fout.write(json.dumps(row, ensure_ascii=False), '\n')
		idx += 1

		if (idx % 100000) == 0:
			print('rows : {0}'.format(idx))
		row = cur.fetchone() 

	print('rows : {0}'.format(idx))

if __name__ == '__main__':
	main()
