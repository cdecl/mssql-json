#-*- coding: utf-8 -*-

import pymssql
import json

def db_connect():
	return pymssql.connect(server='SERVER-NAME', user='', password='', database='', charset='utf8')  

def main():
	output_file = r"d:\a.json"
	sql = '''
			select *
			from tblname
		'''
		
	with db_connect() as conn:
		with open(output_file, 'w') as fout:
			cur = conn.cursor(as_dict=True)
			# cur.execute('select top 100 * from tbl_BBS_Detail')  
			cur.execute(sql)  
			row = cur.fetchone()

			while row:  
				fout.write(json.dumps(row, ensure_ascii=False))
				fout.write('\n')
				row = cur.fetchone()  

	print('Done')

if __name__ == '__main__':
	main()
