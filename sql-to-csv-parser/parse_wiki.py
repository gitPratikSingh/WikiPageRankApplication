import ast
import csv
import os
import re
import time

SCHEMAS = {}


def is_create_statement(line):
    return line.startswith('CREATE TABLE')


def is_field_definition(line):
    return line.strip().startswith('`')


def is_insert_statement(line):
    return line.startswith('INSERT INTO')


def get_mysql_name_value(line):
    value = None
    result = re.search(r'\`([^\`]*)\`', line)
    if result:
        value = result.groups()[0]
    return value


def get_value_tuples(line):
    values = line.partition(' VALUES ')[-1].strip().replace('NULL', "''")
    if values[-1] == ';':
        values = values[:-1]

    return ast.literal_eval(values)


def write_file(output_directory, table_name, schema, values, init):
    file_name = os.path.join(output_directory, '%s.csv' % (table_name,))
    
    with open(file_name, 'a', encoding='utf8', newline='') as write_file:
        writer = csv.DictWriter(write_file, fieldnames=schema)
        if init == True:
            print ('header!')
            writer.writeheader()
        for value in values:
            #print (value)
            writer.writerow(dict(zip(schema, value)))


def parse_file(file_name, output_directory):
    
    current_table_name = None
    i=0
    add_header=True

    with open(file_name, 'r', encoding='utf8') as read_file:
        print ('calculating the row count')
        value = len(list(read_file))
        print (value)
    
    with open(file_name, 'r', encoding='utf8') as read_file:
     
        for line in read_file:
            i+=1
    
            if is_insert_statement(line):
                current_table_name = get_mysql_name_value(line)
                current_schema = SCHEMAS[current_table_name]
                values = get_value_tuples(line)    
                write_file(output_directory, current_table_name, current_schema, values, add_header)
                if add_header == True:
                    add_header = False
                
            
            elif is_create_statement(line):
                current_table_name = get_mysql_name_value(line)
                SCHEMAS[current_table_name] = []
            
            elif current_table_name and is_field_definition(line):
                field_name = get_mysql_name_value(line)
                SCHEMAS[current_table_name].append(field_name)
            
                
            if i%10==0 or i==value :
                print ('last row processed %d, out of %d' % (i, value)) 
                
    
parse_file('simplewiki-20170901-page.sql', 'output')
parse_file('simplewiki-20170901-pagelinks.sql', 'output')
