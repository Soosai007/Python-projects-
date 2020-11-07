import time
from playsound import playsound

seconds=int(input("How many seconds to wait?"))

for i in range(seconds):
    print(str(seconds - i) + " Seconds Left")
    time.sleep(1)

playsound('boom.mp3')
print("Boom Time is Up ")

