import os
import shutil

def parse_text_file(text_file):
    #parses a curriculum file to produce title and groups necessary to make text. Prints as it interprets for error checking.
    
    print("This is how your curriculum file is being interpreted:\n")
    
    tf = open(text_file)
    line = tf.readline()
    while line and line != "TITLE\n":
        line = tf.readline()
    title = tf.readline()
    title = title.strip('\n')
    print("title:")
    print(title)

    line = tf.readline()
    line = line.strip()
    assert line == ""
    print("")
    line = tf.readline()
    line = line.strip()
    groups = []
    while line:                         #this block of code processes one group at a time
        assert line and line != ""
        name = line
        print("new group:")
        print(name)
        line = tf.readline()
        line = line.strip()
        assert line == "TOPICS", "I think you have something besides 'TOPICS' after " + name
        print("TOPICS")
        line = tf.readline()
        line = line.strip()
        topics = []
        while line != "" and os.path.exists("./content/" + line):
            print(line)
            topics.append(line)
            line = tf.readline()
            line = line.strip()
        assert line == "ONLINE HOMEWORK", "I think you have something besides 'ONLINE HOMEWORK' after your topics in " + name + ", or one of your topics paths doesn't exist"
        print(line)
        line = tf.readline()
        line = line.strip()
        online_hw = []
        while line != "" and os.path.exists("./content/" + line):
            print(line)
            online_hw.append(line)
            line = tf.readline()
            line = line.strip()
        assert line == "WRITTEN HOMEWORK", "I think you have something besides 'WRITTEN HOMEWORK' after your online homework in " + name + ", or one of your online homework paths doesn't exist"
        print(line)
        line = tf.readline()
        line = line.strip()
        written_hw = []
        while line != "" and os.path.exists("./content/" + line):
            print(line)
            written_hw.append(line)
            line = tf.readline()
            line = line.strip()
        assert line == "PROFESSIONAL HOMEWORK", "I think you have something besides 'PROFESSIONAL HOMEWORK' after your written homework in " + name + ", or one of your written homework paths doesn't exist"
        line = tf.readline()
        line = line.strip()
        professional_hw = []
        while line != "" and os.path.exists("./content/" + line):
            print(line)
            professional_hw.append(line)
            line = tf.readline()
            line = line.strip()
        group = {"name": name, "topics": topics, "online_hw": online_hw, "written_hw": written_hw, "professional_hw": professional_hw}
        groups.append(group)
        assert line == "", "I think you have something extra after your professional homework in " + name + ", or one of your professional paths doesn't exist"
        print("")
        line = tf.readline()
        line = line.strip()

    tf.close()

    print("If this doesn't look right, check the formatting in your curriculum file. Note that professional problems will be listed under Written Problems, since they will be in the same activity.")

    return [title, groups]

def generate_text(title_and_groups):
    #generates the entire text.
    
    title = title_and_groups[0]
    groups = title_and_groups[1]

    text = open("multivariable.tex", "w")

    text.write("\\documentclass{xourse}\n")
    text.write("\\title{" + title + "}\n")
    text.write("\\graphicspath{")
    text.write("{./}")
    for g in groups:
        group_folder = "".join(c for c in g["name"] if c.isalpha() or c.isdigit())
        text.write("{./auto_generated_text/" + group_folder + "/graphics/}")
    text.write("}\n")
    text.write("\\begin{document}\n")
    text.write("\\begin{abstract}\n")
    text.write("This is the testing ground for the UMTYMP Multivariable Calculus book.\n")
    text.write("\\end{abstract}\n")
    text.write("\\maketitle\n\n")
    
    for group in groups:
        text.write("\n\\part{" + group["name"] + "}\n\n")
        activities = generate_group(group)
        for activity in activities:
            text.write("\\activity{" + activity + "}\n")
    

    text.write("\\end{document}")

    return title

def generate_hw(group, online_hw, written_hw, professional_hw):
    #generates homework problem sets
    
    activities = []
    
    if len(online_hw) > 0:
        olhw_file = open("./auto_generated_text/" + group + "/online_hw.tex", "w")
        activities.append("./auto_generated_text/" + group + "/online_hw.tex")
    
        olhw_file.write("\\documentclass{ximera}\n")
        olhw_file.write("\\graphicspath{{./auto_generated_text/" + group + "/graphics/}{./graphics/}}\n")
        olhw_file.write("\\title{Online Homework}\n")
        olhw_file.write("\\begin{document}\n")
        olhw_file.write("\\begin{abstract}\n")
        olhw_file.write("\\end{abstract}\n")
        olhw_file.write("\\maketitle\n\n")
    
        for problem in online_hw:
            path = "./content/" + problem
            with open(path) as f:
                for line in f:
                    olhw_file.write(line)
            olhw_file.write("\n\n")

        olhw_file.write("\\end{document}")
        olhw_file.close()

    if len(written_hw) > 0 or len(professional_hw) > 0:
        whw_file = open("./auto_generated_text/" + group + "/written_hw.tex", "w")
        activities.append("./auto_generated_text/" + group + "/written_hw.tex")
    
        whw_file.write("\\documentclass{ximera}\n")
        whw_file.write("\\graphicspath{{./auto_generated_text/" + group + "/graphics/}{./graphics/}}\n")
        whw_file.write("\\title{Written Homework}\n")
        whw_file.write("\\begin{document}\n")
        whw_file.write("\\begin{abstract}\n")
        whw_file.write("\\end{abstract}\n")
        whw_file.write("\\maketitle\n\n")
    
        if len(written_hw) > 0:
            whw_file.write("\\section{Written Homework}\n\n")
            for problem in written_hw:
                path = "./content/" + problem
                with open(path) as f:
                    for line in f:
                        whw_file.write(line)
                whw_file.write("\n\n")

        if len(professional_hw) > 0:
            whw_file.write("\\section{Professional Problem}\n\n")
            for problem in professional_hw:
                path = "./content/" + problem
                with open(path) as f:
                    for line in f:
                        whw_file.write(line)
                whw_file.write("\n\n")
        
        whw_file.write("\\end{document}")
        whw_file.close()
    
    return activities

def generate_all_problems(group, topics):
    #generates activity with all problems from topics
    
    activities = []

    online_problem_list = []
    
    for section in topics:
        path = "./content/" + section + "/problems/online/"
        for filename in os.listdir(path):
            if filename.endswith(".tex"):
                online_problem_list.append("./content/" + section + "/problems/online/" + filename)

    written_problem_list = []

    for section in topics:
        path = "./content/" + section + "/problems/written/"
        for filename in os.listdir(path):
            if filename.endswith(".tex"):
                written_problem_list.append("./content/" + section + "/problems/written/" + filename)

    if len(online_problem_list) > 0 or len(written_problem_list) > 0:
        all_problems = open("./auto_generated_text/" + group + "/all_problems.tex","w")
        activities.append("./auto_generated_text/" + group + "/all_problems.tex")
    
        all_problems.write("\\documentclass{ximera}\n")
        all_problems.write("\\graphicspath{{./auto_generated_text/" + group + "/graphics/}{./graphics/}}\n")
        all_problems.write("\\title{Practice Problems}\n")
        all_problems.write("\\begin{document}\n")
        all_problems.write("\\begin{abstract}\n")
        all_problems.write("\\end{abstract}\n")
        all_problems.write("\\maketitle\n")
        
        if len(online_problem_list) > 0:
            all_problems.write("\\section{Online Problems}\n")
            
            for problem in online_problem_list:
                with open(problem) as f:
                    for line in f:
                        all_problems.write(line)
                all_problems.write("\n\n")
        
        if len(written_problem_list) > 0:
            all_problems.write("\\section{Written Problems}\n")
            
            for problem in written_problem_list:
                with open(problem) as f:
                    for line in f:
                        all_problems.write(line)
                all_problems.write("\n\n")
    
        all_problems.write("\\end{document}")
        
        all_problems.close()

    return activities

def generate_topics(group, topics):
    #copies topics files into auto_generated_text
    
    activities = []
    
    for section in topics:
        path = "./content/" + section + "/"
        for file in os.listdir(path):
            if file.endswith(".tex"):
                copy = open("./auto_generated_text/" + group + "/" + file,"w")
                activities.append("./auto_generated_text/" + group + "/" + file)
                with open(path + file) as f:
                    for line in f:
                        if "graphicspath" in line:
                            copy.write("\\graphicspath{{./auto_generated_text/" + group + "/graphics/}{./graphics/}}\n")
                        else:
                            copy.write(line)
                copy.close()
            if file == "graphics" and os.path.isdir(path + "graphics/"):
                dest = "./auto_generated_text/" + group + "/graphics/"
                for g in os.listdir(path + "graphics"):
                    shutil.copy(path + "graphics/" + g , dest)
    return activities

def generate_group(group):
    #builds all of the relevant files in auto_generated_text
                                    
    topics = group["topics"]
    online_hw = group["online_hw"]
    written_hw = group["written_hw"]
    professional_hw = group["professional_hw"]
    name = group["name"]
    name = "".join(c for c in group["name"] if c.isalpha() or c.isdigit())
    group["directory"] = name
    
    directory = "./auto_generated_text/" + name
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    if not os.path.exists(directory + "/graphics"):
        os.makedirs(directory + "/graphics")
    
    activities = generate_topics(name, topics) + generate_hw(name, online_hw, written_hw, professional_hw) + generate_all_problems(name, topics)

    return activities

