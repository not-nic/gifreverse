import subprocess
import requests
import time

def reverse_gif(input_gif):
    output_gif = f"{input_gif}_reverse.gif"
    
    try:
        subprocess.call(['ffmpeg', '-i', input_gif, '-vf', 'reverse', output_gif])
        print(f"Successfully reversed '{input_gif}' and saved as '{output_gif}'")
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":    
    while True:
        gif_url = input("What gif is next: ")
        
        r = requests.get(gif_url, allow_redirects=True)
        timestamp = time.time()
        
        filename = f"{timestamp}.gif"
        open(filename, "wb").write(r.content)
        
        reverse_gif(filename)