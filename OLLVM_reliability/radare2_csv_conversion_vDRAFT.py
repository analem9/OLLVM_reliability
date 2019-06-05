#!/usr/bin/python3
import sys
import r2pipe
import json
import os
from itertools import repeat
import csv


# ------------------------------------------------------------------------------------------------------------------------------------
# This script intends to decide, thanks to the output data it generates, which sorting criterion to use in the radar2_analysis-v2.py 
# ------------------------------------------------------------------------------------------------------------------------------------

################################################## USER SECTION #######################################################
# Choose the analysis and listing commands you want to apply to the input file
ANALYSIS_CMD        = "aa"
LISTING_CMD         = "aflj~{}"
#######################################################################################################################



# opening the input executable file
# print("Opening the input executable file")
r2 = r2pipe.open(str(sys.argv[1])) 



# basic analysis and listing commands
r2.cmd(ANALYSIS_CMD)
aflj_output = r2.cmd(LISTING_CMD)



# loading and processing the json output
# print("Loading and processing the json output...")
aflj_json           = json.loads(aflj_output) #ici il faut rajouter un .decode() qqch
aflj_lines_number   = len(aflj_json)
# print (aflj_output)


"""
    Version 1 => Building complete_aflj_data_array array without the callrefs and datarefs keys and values
    :structure: array of arrays:
                [
                    [name_0, offset_0, nbbs_0, ... , type_0],
                    [name_1, offset_1, nbbs_1, ... , type_1],
                    ...
                    [name_n, offset_n, nbbs_n, ... , type_n]
                ]
    :size: n = number of output lines of the aflj r2 command
"""
# complete_aflj_data_array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for i in repeat(None, aflj_lines_number)]

# for line in range(aflj_lines_number):
#     complete_aflj_data_array[line][0]=aflj_json[line]['name']
#     complete_aflj_data_array[line][1]=aflj_json[line]['offset']
#     complete_aflj_data_array[line][2] = aflj_json[line]['nbbs']
#     complete_aflj_data_array[line][3] = aflj_json[line]['size']
#     complete_aflj_data_array[line][4]=aflj_json[line]['calltype']
#     complete_aflj_data_array[line][5]=aflj_json[line]['realsz']
#     complete_aflj_data_array[line][6]=aflj_json[line]['diff']
#     complete_aflj_data_array[line][7]=aflj_json[line]['cc']
#     complete_aflj_data_array[line][8]=aflj_json[line]['indegree']
#     complete_aflj_data_array[line][9]=aflj_json[line]['nargs']
#     complete_aflj_data_array[line][10]=aflj_json[line]['difftype']
#     complete_aflj_data_array[line][11]=aflj_json[line]['edges']
#     complete_aflj_data_array[line][12]=aflj_json[line]['outdegree']
#     complete_aflj_data_array[line][13]=aflj_json[line]['cost']
#     complete_aflj_data_array[line][14]=aflj_json[line]['nlocals']
#     complete_aflj_data_array[line][15]=aflj_json[line]['ebbs']
#     complete_aflj_data_array[line][16]=aflj_json[line]['type']
#     # complete_aflj_data_array[line][17]=aflj_json[line]['datarefs']
#     # complete_aflj_data_array[line][17]=aflj_json[line]['callrefs']
# print (complete_aflj_data_array)





"""
    Version 2 => Convert directly from json to csv all json keys and values
              => IT AWFULLY CONVERTED THE CALLREFS AND DATAREFS INTO THE CSV FORMAT
"""
# csv_formated = open('/tmp/csv_formated.csv', 'w')

# csvwriter = csv.writer(csv_formated)
# count =0
# for elt in aflj_json:
#     if count == 0:
#         header = elt.keys()
#         csvwriter.writerow(header)
#         count+=1
#     csvwriter.writerow(elt.values())
# csv_formated.close()





"""
    Version 3 => Convert directly from json to csv without callrefs and datarefs keys and values
"""
# csv_formated_again = "./version3.csv"
# csv = open(csv_formated_again, "w")
# columnTitleRow = "offset, name, size, realsz, cc, cost, nbbs, edges, ebbs, calltype, type, diff, difftype, indegree, outdegree, nargs, nlocals\n"
# csv.write(columnTitleRow)
# for output in aflj_json:
#     pass





"""
    Version 4 => Convert directly from json to csv with callrefs' J and C numbers,
                 and datarefs values number
"""
# csv_formated_again = "./version3.csv"
# csv = open(csv_formated_again, "w")
# columnTitleRow = "offset, name, size, realsz, cc, cost, nbbs, edges, ebbs, calltype, type, diff, difftype, indegree, outdegree, nargs, nlocals, C refs, J refs, datarefsNb\n"
# csv.write(columnTitleRow)


"""
    Version 5 => Print in the terminal in csv-looking format
"""


# columnTitleRow = "calltype, realsz, diff, name, cc, indegree, ,nargs, difftype, edges, outdegree, nlocals, datarefs, cost, cref_c, cref_j, offset, ebbs, nbbs, type, size \n"
# print (columnTitleRow)
# for output in aflj_json:
#     row = ""
#     for element in output:
#         J_count = 0
#         C_count = 0
#         if (element == "callrefs"):
#         # count the number of J and C
#             if (output[element] == "[]"): # if there is no callref
#                 row+=str(0) + ", " + str(0) + ", "
#             else: # if there is at least one callref
#                 for cref in range(0, len(output[element])):
#                 # for each {type: type_value, addr: addr_value, at: at_value}
#                     # print(output[element][cref])
#                     if ((output[element][cref]['type']) == 'J'):
#                         J_count+=1
#                         # print (output[element][cref]['type'], J_count)
#                     else: 
#                         C_count+=1
#                         # print (output[element][cref]['type'], C_count)  
#                     # print("########end#########")
#                     row+= str(C_count) + ", " + str(J_count) + ", "
                
#             # print (row)
#                 # print (output[element])
#         if (element == "datarefs"):
#         # count the number of elements in the datarefs list
#             drefs_count = 0
#         # just print it properly
#         row+= str(output[element]) + ", "
#     print (row + "\n")



# columnTitleRow = "calltype, realsz, diff, name, cc, indegree, nargs, difftype, edges, outdegree, cost, datarefs, nlocals, cref_c, cref_j, offset, ebbs, nbbs, type, size \n"
# parameters = ["calltype", "realsz", "diff", "name", "cc", "indegree", "nargs", "difftype", "edges", "outdegree", "nlocals", "cost", "offset", "ebbs", "nbbs", "type", "size"]

# print (columnTitleRow)
# for output in aflj_json:
#     row = ""
#     for element in output:
#         J_count = 0
#         C_count = 0
#         if (element == "callrefs"):
#         # count the number of J and C
#             if (len(output[element]) == 0): # if there is no callref
#                 # row+=str(0) + ", " + str(0) + ", "
#                 row+= "N\A, N\A, "
#             else: # if there is at least one callref
#                 for cref in range(0, len(output[element])):
#                 # for each {type: type_value, addr: addr_value, at: at_value}
#                     # print(output[element][cref])
#                     if ((output[element][cref]['type']) == 'J'):
#                         J_count+=1
#                         # print (output[element][cref]['type'], J_count)
#                     else: 
#                         C_count+=1
#                         # print (output[element][cref]['type'], C_count)  
#                     # print("########end#########")
#                     row+= str(C_count) + ", " + str(J_count) + ", "
#         if (element == "datarefs"):
#         # count the number of elements in the datarefs list
#             if (len(output[element]) == 0): # if there is no dataref
#                 row+= "nodataref, "
#             else:
#                 row+=str(len(output[element])) + "dr" + ", "
#         if (element in parameters):
#         # just print it properly
#             row+= str(output[element]) + ", "
#         else:
#             row+= "sipaasdararefoucallref, "
#     print (row + "\n")


# ca marche ca mais c est pas elegant
# columnTitleRow = "programName,calltype, realsz, diff, name, cc, indegree, nargs, difftype, edges, outdegree, cost, nlocals, offset, ebbs, nbbs, type, size, datarefs, cref_c, cref_j\n"
# parameters = ["calltype", "realsz", "diff", "name", "cc", "indegree", "nargs", "difftype", "edges", "outdegree", "nlocals", "cost", "offset", "ebbs", "nbbs", "type", "size"]

# print (columnTitleRow)
# for output in aflj_json:
#     row1 = str(sys.argv[1]) + ","
#     row2 = ""
#     for element in output:
#         J_count = 0
#         C_count = 0
#         if (element in parameters):
#         # just print it properly
#             row1+= str(output[element]) + ","
#         else:
#             if (element == "callrefs"):
#             # count the number of J and C
#                 if (len(output[element]) == 0): # if there is no callref
#                     # row1+=str(0) + ", " + str(0) + ", "
#                     row2+= "N\A,N\A,"
#                 else: # if there is at least one callref
#                     for cref in range(0, len(output[element])):
#                     # for each {type: type_value, addr: addr_value, at: at_value}
#                         if ((output[element][cref]['type']) == 'J'):
#                             J_count+=1
#                         else: 
#                             C_count+=1
#                     row2+= str(C_count) + "," + str(J_count) + ","
#             if (element == "datarefs"):
#             # count the number of elements in the datarefs list
#                 if (len(output[element]) == 0): # if there is no dataref
#                     row2+= "nodataref,"
#                 else:
#                     row2+=str(len(output[element])) + ","
#     print (row1 + row2)


# for line in range(aflj_lines_number):
#     complete_aflj_data_array[line][0]=aflj_json[line]['name']
#     complete_aflj_data_array[line][1]=aflj_json[line]['offset']
#     complete_aflj_data_array[line][2] = aflj_json[line]['nbbs']

# for line in range(aflj_lines_number):
#     row = str(sys.argv[1]) + ","
#     row+= str(aflj_json[line]['calltype']) + "," + str(aflj_json[line]['realsz']) + "," + str(aflj_json[line]['diff']) + "," +str(aflj_json[line]['name']) + "," + str(aflj_json[line]['cc'] + "," + str(aflj_json[line]['indegree']) + "," + str(aflj_json[line]['nargs']) + ","+ str(aflj_json[line]['difftype']) + "," + str(aflj_json[line]['edges'])+ ","+str(aflj_json[line]['outdegree']) + "," + str(aflj_json[line]['cost']) + "," + str(aflj_json[line]['nlocals'])+ ","+str(aflj_json[line]['offset'])+ ","+str(aflj_json[line]['ebbs'])+ ","+str (aflj_json[line]['nbbs'])+ ","+str(aflj_json[line]['type'])+ ","+str(aflj_json[line]['size'])
#     print(row)

# columnTitleRow = "programName,calltype, realsz, diff, name, cc, indegree, nargs, difftype, edges, outdegree, cost, nlocals, offset, ebbs, nbbs, type, size, datarefs, cref_c, cref_j\n"
# parameters = ["calltype", "realsz", "diff", "name", "cc", "indegree", "nargs", "difftype", "edges", "outdegree", "nlocals", "cost", "offset", "ebbs", "nbbs", "type", "size"]

# print (columnTitleRow)
# for output in aflj_json:
#     row1 = str(sys.argv[1]) + ","
#     row2 = ""
#     for element in output:
#         J_count = 0
#         C_count = 0
#         if (element in parameters):
#         # just print it properly
#             row1+= str(output[element]) + ","
#         else:
#             if (element == "callrefs"):
#             # count the number of J and C
#                 if (len(output[element]) == 0): # if there is no callref
#                     # row1+=str(0) + ", " + str(0) + ", "
#                     row2+= "N\A,N\A,"
#                 else: # if there is at least one callref
#                     for cref in range(0, len(output[element])):
#                     # for each {type: type_value, addr: addr_value, at: at_value}
#                         if ((output[element][cref]['type']) == 'J'):
#                             J_count+=1
#                         else: 
#                             C_count+=1
#                     row2+= str(C_count) + "," + str(J_count) + ","
#             if (element == "datarefs"):
#             # count the number of elements in the datarefs list
#                 if (len(output[element]) == 0): # if there is no dataref
#                     row2+= "nodataref,"
#                 else:
#                     row2+=str(len(output[element])) + ","
#     print (row1 + row2)

columnTitleRow = "programName,calltype,realsz,diff,name,cc,indegree,nargs,difftype,edges,outdegree,cost,nlocals,offset,ebbs,nbbs,type,size,datarefsNb,cref_c,cref_j\n"
print (columnTitleRow)
for line in range(aflj_lines_number):
    print(str(sys.argv[1]), end='')
    print (",", end='')
    print (aflj_json[line]['calltype'], end='')
    print (",", end='')
    print(aflj_json[line]['realsz'], end='')
    print (",", end='')
    print(aflj_json[line]['diff'], end='')
    print (",", end='')
    print(aflj_json[line]['name'], end='')
    print (",", end='')
    print(aflj_json[line]['cc'], end='')
    print (",", end='')
    print(aflj_json[line]['indegree'], end='')
    print (",", end='')
    print(aflj_json[line]['nargs'], end='')
    print (",", end='')
    print(aflj_json[line]['difftype'], end='')
    print (",", end='')
    print(aflj_json[line]['edges'], end='')
    print (",", end='')
    print(aflj_json[line]['outdegree'], end='')
    print (",", end='')
    print(aflj_json[line]['cost'], end='')
    print (",", end='')
    print(aflj_json[line]['nlocals'], end='')
    print (",", end='')
    print(aflj_json[line]['offset'], end='')
    print (",", end='')
    print(aflj_json[line]['ebbs'], end='')
    print (",", end='')
    print(aflj_json[line]['nbbs'], end='')
    print (",", end='')
    print(aflj_json[line]['type'], end='')
    print (",", end='')
    print(aflj_json[line]['size'], end='')
    if 'datarefs' in aflj_json[line].keys():
        print (",", end='')
        print(len(aflj_json[line]['datarefs']), end='')
    if 'callrefs' in aflj_json[line].keys():
        print (",", end='')
        if len(aflj_json[line]['callrefs'])== 0:
            print(''',''')
        else:
            J_count = 0
            C_count = 0
            for elt in range(len(aflj_json[line]['callrefs'])): 
                if aflj_json[line]['callrefs'][elt]['type'] == "C":
                    C_count+=1
                if aflj_json[line]['callrefs'][elt]['type'] == "J":
                    J_count+=1
            print (C_count, end='')
            print(",", end='')
            print (J_count)
    else:
        print('')
   
