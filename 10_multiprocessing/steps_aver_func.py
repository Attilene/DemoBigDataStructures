import csv

def steps_aver(file: str) -> dict:
    tag_steps = dict()
    with open(file, 'r') as fp:
        reader = csv.reader(fp, delimiter=';')
        header = next(reader)
        for row in reader: 
            if row[1] not in tag_steps:
                tag_steps[row[1]] = [0, 0]
            tag_steps[row[1]][0] += int(row[2])
            tag_steps[row[1]][1] += 1
    
#     tag_steps_aver = dict()
#     for tag, steps in tag_steps.items():
#         sums = steps[0]
#         count = steps[1]
#         tag_steps_aver[tag] = sums / count
    
    return tag_steps

def unite_steps_aver(all_files_results: list) -> dict:
    all_steps_aver_buf = dict()
    
    for result in all_files_results:
        for tag, steps in result.items():
            if tag not in all_steps_aver_buf:
                all_steps_aver_buf[tag] = [0, 0]
            all_steps_aver_buf[tag][0] += steps[0]
            all_steps_aver_buf[tag][1] += steps[1]
     
    all_steps_aver_dict = dict()
    for tag, steps in all_steps_aver_buf.items():
        sums = steps[0]
        count = steps[1]
        all_steps_aver_dict[tag] = sums / count
    
    return all_steps_aver_dict
