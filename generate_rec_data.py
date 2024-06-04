import os, glob

train_data_dir = "./data/rec/train/imgs"
train_data_list = glob.glob(train_data_dir + "/*.jpg")
train_data_list_txt = "./data/rec/train/train_list.txt"

with open(train_data_list_txt, "w", encoding="utf-8") as f:
    for train_data in train_data_list:
        basename = os.path.basename(train_data)
        label = basename.split(".")[0]
        f.write(basename + "\t" + label + "\n")


eval_data_dir = "./data/rec/eval/imgs"
eval_data_list = glob.glob(train_data_dir + "/*.jpg")
eval_data_list_txt = "./data/rec/eval/eval_list.txt"

with open(eval_data_list_txt, "w", encoding="utf-8") as f:
    for eval_data in eval_data_list:
        basename = os.path.basename(eval_data)
        label = basename.split(".")[0]
        f.write(basename + "\t" + label + "\n")
