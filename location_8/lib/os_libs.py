
def check_mkdirs(dir:str):
    import os
    
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        pass


def get_git_branch():
    import os, subprocess
    
    now_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # git -C [path] rev-parse --abbrev-ref HEAD
        command = ["git", "-C", now_dir, "rev-parse", "--abbrev-ref", "HEAD"]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    
    except subprocess.CalledProcessError as e:
        print(f"Error Appeared: {e}")
        return None
