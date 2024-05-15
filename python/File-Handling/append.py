goal_list   = ["Python","HTML", "CSS"]
goal_list += ["Django","Database"]

file = open ("python/File-Handling/newnote.txt", "a")

for goal in goal_list:
     file.write(f"master{goal}\n")
    
file.close()