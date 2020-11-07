import speedtest   
st = speedtest.Speedtest() 

print("Your Download speed is", st.download()) 

print("Your Upload speed is", st.upload()) 

st.get_servers([])
print(st.results.ping) 
