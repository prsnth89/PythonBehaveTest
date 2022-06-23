import subprocess
if __name__ == '__main__':
    s=subprocess.run('behavex -t login1,login2 --parallel-processes 2 --parallel-scheme feature')