#-*- coding: utf-8 -*-

import pymssql
import json

class config:
	output_file = r"output.json"
	sql = '''
		select *
		from tbl
	'''

def db_connect():
	return pymssql.connect(server='STAGE1', user='user', password='pwd', database='dbname', charset='utf8')  


def main():
	with db_connect() as conn:
		with open(config.output_file, 'w') as fout:
			cur = conn.cursor(as_dict=True)
			cur.execute(config.sql)  
			row = cur.fetchone()

			trans_data(row, fout, cur)
	print('Done')

def trans_data(row, fout, cur):
	buffer_size = 1000
	display_size = 10000

	idx = 0
	doc = []
	while row:
		doc.append(json.dumps(row, ensure_ascii=False) + '\n')
		row = cur.fetchone() 
		idx += 1
		
		if len(doc) == buffer_size:
			fout.writelines(doc)
			doc.clear()

		if (idx % display_size) == 0:
			print('Rows : {0}'.format(idx))
	
	if len(doc) > 0:
		fout.writelines(doc)
		doc.clear()

	print('rows : {0}'.format(idx))



if __name__ == '__main__':
	main()
