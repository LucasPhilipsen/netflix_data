import matplotlib.pyplot as plt
import netflix as nt

plt.hist(nt.anos90['duration'])
plt.xlabel("Movies Duration")
plt.ylabel("Number of Movies")
plt.title("Distribuation Of Movies Durations")

show_graph = plt.show()
