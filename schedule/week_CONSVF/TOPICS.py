#edit the list of topics below to change the topics covered and homework assigned in the current week. Running this file will update the list of topics, the homework sets, and the list of extra practice problems.

name = "Week 9: Curl"

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

#you probably don't want to change the code below here...

import sys
sys.path.append('./../..')

import generate_materials as gm

gm.generate_week(name, topics, online_hw, written_hw, professional_hw)