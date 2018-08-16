#change the title of the text here
title = "Multivariable Calculus"

weeks = []

#edit materials for the first week here
name = "Week 0: Review"
topics = [ "ch00_review/1_vectors" , "ch00_review/2_dotProd", "ch00_review/3_crossProd", "ch00_review/4_matrices" , "ch00_review/5_planes"]
online_hw = []
written_hw = []
professional_hw = []

weeks.append({"name": name, "topics": topics, "online_hw": online_hw, "written_hw": written_hw, "professional_hw": professional_hw})

#edit materials for the second week here
name = "Week 1: Coordinate Systems"
topics = [ "ch01_coordinate_systems/1_review" , "ch01_coordinate_systems/2_cylindrical_coords", "ch01_coordinate_systems/3_spherical_coords"]
online_hw = []
written_hw = []
professional_hw = []

weeks.append({"name": name, "topics": topics, "online_hw": online_hw, "written_hw": written_hw, "professional_hw": professional_hw})

#you probably don't want to change the code below here

import generate_materials as gm

import os

topics = [ "chCURL_curl/N.1_curl_comp" , "chCURL_curl/N.2_curl_geo", "chCURL_curl/N.3_curl_connect"]

online_hw = [ "chCURL_curl/N.3_curl_connect/problems/online/problem1.tex",
             "chCURL_curl/N.2_curl_geo/problems/online/problem1.tex",
             "chCURL_curl/N.2_curl_geo/problems/online/problem2.tex",
             "chCURL_curl/N.2_curl_geo/problems/online/problem3.tex",
             "chCURL_curl/N.3_curl_connect/problems/online/problem2.tex",
             "chCURL_curl/N.3_curl_connect/problems/online/problem3.tex",
             "chCURL_curl/N.3_curl_connect/problems/online/problem4.tex",
             "chCURL_curl/N.3_curl_connect/problems/online/problem5.tex",
             "chCURL_curl/N.3_curl_connect/problems/online/problem6.tex"]

written_hw = [ "chCURL_curl/N.1_curl_comp/problems/written/problem1.tex",
              "chCURL_curl/N.2_curl_geo/problems/written/problem1.tex",
              "chCURL_curl/N.3_curl_connect/problems/written/problem1.tex"]

professional_hw = [ "chCURL_curl/N.1_curl_comp/problems/professional/problem1.tex"]

gm.generate_hw("week_CURL", online_hw, written_hw, professional_hw)

gm.generate_all_problems("week_CURL", topics)

gm.generate_topics("week_CURL", topics)

gm.generate_group(weeks[0])
gm.generate_group(weeks[1])

gm.generate_text(title, weeks)

