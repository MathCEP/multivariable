#edit the list of topics below to change the topics covered and homework assigned in the current week. Running this file will update the list of topics, the homework sets, and the list of extra practice problems.

name = "Week 0: Review"

topics = [ "./content/ch00_review/1_vectors" , "./content/ch00_review/2_dotProd", "./content/ch00_review/3_crossProd", "./content/ch00_review/4_matrices" , "./content/ch00_review/5_planes"]

online_hw = []

written_hw = []

professional_hw = []

#you probably don't want to change the code below here...

import sys
sys.path.append('./../..')

import generate_materials as gm

gm.generate_week(name, topics, online_hw, written_hw, professional_hw)
