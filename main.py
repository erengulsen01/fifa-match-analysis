import matplotlib.pyplot as plt



file=open("data/fifa-yusuf.txt", "r")



eren_dict={}
yusuf_dict={}


eren_gol = 0
yusuf_gol = 0
eren_win = 0
yusuf_win = 0
berabere = 0
x=file.read()
x = x.split("\n")
for i in range(len(x)):
    x[i] = x[i].replace("-"," ").strip("\n")
    list1 = x[i].split(" ")
    if list1[1] in eren_dict:
        eren_dict[list1[1]] += 1
    else:
        eren_dict[list1[1]] = 1
    
    if list1[5] in yusuf_dict:
        yusuf_dict[list1[5]] += 1
    else:
        yusuf_dict[list1[5]] = 1



    eren_g = int(list1[2])
    yusuf_g = int(list1[3])
    if eren_g> yusuf_g:
        eren_win += 1
    elif yusuf_g > eren_g:
        yusuf_win += 1
    elif eren_g ==  yusuf_g:
        berabere += 1
    eren_gol += eren_g
    yusuf_gol += yusuf_g

print("Maç sayısı:", len(x))

eren_dict = dict(sorted(eren_dict.items(), key=lambda x:x[1], reverse=True))
yusuf_dict = dict(sorted(yusuf_dict.items(), key=lambda x:x[1], reverse=True))

for team in eren_dict:
    print("Eren {} takımıyla {} kez oynadı".format(team,eren_dict[team]))

for team in yusuf_dict:
    print("Yusuf {} takımıyla {} kez oynadı".format(team,yusuf_dict[team]))

print("Eren'in gol sayısı:", eren_gol, "Maç başı gol:", f"{eren_gol/len(x):.2f}")
print("Yusuf'un gol sayısı:", yusuf_gol, "Maç başı gol:", f"{yusuf_gol/len(x):.2f}")
print("Eren'in galibiyeti: {}, Yusuf'un galibiyeti: {}, Berabere: {} ".format(eren_win,yusuf_win,berabere))
plt.style.use("classic")

fig, ax = plt.subplots()
team = list(eren_dict.keys())
counts= list(eren_dict.values())


ax.bar(team,counts)

ax.set_ylabel('match played')
ax.set_title('teams played')
plt.savefig("Teams")
plt.show()




