import os
#import subprocess

def generate_text(title):

    text = open("multivariable.tex", "w")

    text.write("\\documentclass{xourse}\n")
    text.write("\\title{" + title + "}\n")
    text.write("\\begin{document}\n")
    text.write("\\begin{abstract}\n")
    text.write("This is the testing ground for the UMTYMP Multivariable Calculus book.\n")
    text.write("\\end{abstract}\n")
    text.write("\\maketitle\n")

    for week in os.listdir("./schedule/"):
        if os.path.isdir("./schedule/" + week):
            text.write("\\input{./schedule/" + week + "/activities_list.tex}\n")
            #subprocess.call("./schedule/" + week + "/TOPICS.py")    #I haven't tested this yet, don't have TOPICS.py in all weeks yet. Might want to use import or another method. Do I really want this here? I don't know.

    text.write("\\end{document}")

    return;

def generate_week(name, topics, online_hw, written_hw, professional_hw):
    
    #generates list of activities for this week.

    activities_list = []
    
    activities_list.append("\\part{" + name + "}\n")

    for section in topics:
        path = "../../content/" + section + "/"
        for file in os.listdir(path):
            if file.endswith(".tex"):
                activities_list.append("\\activity{" + section + "/" + file + "}\n")

    long_path = os.path.abspath('.')
    current_week = os.path.basename(long_path)

    #generates homework problem sets

    online_hw_list = []

    for problem in online_hw:
                    online_hw_list.append("\\input{../../content/" + problem + "}\n")

    if len(online_hw_list) > 0:
        online_hw = open("online_hw.tex", "w")

        online_hw.write("\\documentclass{ximera}\n")
        online_hw.write("\\title{Online Homework}\n")
        online_hw.write("\\begin{document}\n")
        online_hw.write("\\begin{abstract}\n")
        online_hw.write("\\end{abstract}\n")
        online_hw.write("\\maketitle\n")
        online_hw.write("%Will not compile on its own. Compile through the main text.\n")
        online_hw.write("\\section{Online Problems}\n")

        online_hw.writelines(online_hw_list)

        online_hw.write("\\end{document}")

        online_hw.close()
            
        activities_list.append("\\activity{./schedule/" + current_week + "/online_hw.tex}\n")

    written_hw_list = []

    for problem in written_hw:
        written_hw_list.append("\\input{../../content/" + problem + "}\n")
    
    if len(written_hw_list) > 0:
        written_hw = open("written_hw.tex", "w")

        written_hw.write("\\documentclass{ximera}\n")
        written_hw.write("\\title{Written Homework}\n")
        written_hw.write("\\begin{document}\n")
        written_hw.write("\\begin{abstract}\n")
        written_hw.write("\\end{abstract}\n")
        written_hw.write("\\maketitle\n")
        written_hw.write("%Will not compile on its own. Compile through the main text.\n")
        written_hw.write("\\section{Written Problems}\n")

        written_hw.writelines(written_hw_list)

        if len(professional_hw) > 0:
            for pro_problem in professional_hw:
                written_hw.writelines(["\\section{Professional Problem}\n", "\\input{../../content/" + pro_problem + "}\n"])

        written_hw.write("\\end{document}")

        written_hw.close()
            
        activities_list.append("\\activity{./schedule/" + current_week + "/written_hw.tex}\n")

    #generates collection of all problems

    online_problem_list = []

    for section in topics:
        path = "../../content/" + section + "/problems/online/"
        for filename in os.listdir(path):
            online_problem_list.append("\\input{../../content/" + section + "/problems/online/" + filename + "}\n")

    written_problem_list = []
    
    for section in topics:
        path = "../../content/" + section + "/problems/written/"
        for filename in os.listdir(path):
            written_problem_list.append("\\input{../../content/" + section + "/problems/written/" + filename + "}\n")

    if len(online_problem_list) > 0 or len(written_problem_list) > 0:
        all_problems = open("all_problems.tex","w")

        all_problems.write("\\documentclass{ximera}\n")
        all_problems.write("\\title{Extra Problems}\n")
        all_problems.write("\\begin{document}\n")
        all_problems.write("\\begin{abstract}\n")
        all_problems.write("\\end{abstract}\n")
        all_problems.write("\\maketitle\n")
        all_problems.write("%Will not compile on its own. Compile through the main text.\n")
        
        if len(online_problem_list) > 0:
            all_problems.write("\\section{Online Problems}\n")

            all_problems.writelines(online_problem_list)

        if len(written_problem_list) > 0:
            all_problems.write("\\section{Written Problems}\n")

            all_problems.writelines(written_problem_list)

        all_problems.write("\\end{document}")

        all_problems.close()
            
        activities_list.append("\\activity{./schedule/" + current_week + "/all_problems.tex}\n")
            
    activities = open("activities_list.tex", "w")
    activities.writelines(activities_list)
    activities.close()

    return;

