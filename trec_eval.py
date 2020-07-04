import subprocess

def trec_eval(qrel_file,trec_file):
    command = ['./trec_eval',qrel_file,trec_file]
    output = subprocess.Popen(command,stdout=subprocess.PIPE).communicate()
    return output[0]
