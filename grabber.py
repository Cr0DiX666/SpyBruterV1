import os
try:
	from socket import gethostbyname,gaierror
	from concurrent.futures import ThreadPoolExecutor
	from threading import Thread
	from colorama import *
except ImportError:exit('module not found !\nfix with type this command\n\npython -m pip install colorama')

if not os.path.exists("results"):os.makedirs("results")
init(autoreset=True)
merah = Fore.LIGHTRED_EX
kuning = Fore.LIGHTYELLOW_EX
hijau = Fore.LIGHTGREEN_EX
biru = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
cyan = Fore.LIGHTCYAN_EX
hitam = Fore.LIGHTBLACK_EX
putih = Fore.LIGHTWHITE_EX
reset = Fore.RESET
error = 0
success = 0
total = 0

def persen(j,t):
	return j/t*100

def toip(host):
	global error,success,total
	try:
		total += 1
		if "http://" in host:host = host.replace("http://","")
		if "https://" in host:host = host.replace("https://","")
		if "/" in host:host = host.replace("/","")
		ip = gethostbyname(host)
		if not os.path.exists("results/ips.txt"):open(f"results/ips.txt","a+").write("")
		if not os.path.exists("results/error_ips.txt"):open(f"results/error_ips.txt","a+").write("")
		if ip in open("results/ips.txt").read():pass
		else:
			open(f"results/ips.txt","a+").write(f"{ip}\n")
			success += 1
	except gaierror:
		error += 1
		open(f"results/error_ips.txt","a+").write(f"{host}\n")


try:
	os.system("cls" if os.name == "nt" else "clear")
	print(f"\n{putih}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n{putih}MMMMMMMMMMMMMMMMMMMN{cyan}dhdm{putih}NMMMMMMMMMMMMMMMMM\n{putih}MMMMMMMMMMMMMMMN{cyan}mhysssssyh{putih}NMMMMMMMMMMMMMMM\n{putih}MMMMMMMMMMMN{cyan}mdyssssssyssss{putih}NN.+hNMMMMMMMMMM\n{putih}MMMMMMMMN{cyan}dhysssssyh{putih}dmm{cyan}ssss{putih}NN   `/ymMMMMMMM\n{putih}MMMMN{cyan}mhyssssssy{putih}dmy/.ym{cyan}ssss{putih}NN+.     -odMMMM\n{putih}MN{cyan}dhysssssyh{putih}mms:`   ym{cyan}ssss{putih}NMMMms-`    .+hM\n{putih}M{cyan}dssssyhd{putih}mdo-       ym{cyan}ssss{putih}NMMMM{cyan}hmmy/`   `{putih}M\n{putih}M{cyan}dssss{putih}md/.    `:o`  ym{cyan}ssss{putih}NMMMM{cyan}yssy{putih}dd    {putih}M\n{putih}M{cyan}dssss{putih}Ns   `/yNMd`  ym{cyan}ssss{putih}NMMMM{cyan}ysss{putih}hd    {putih}M\n{putih}M{cyan}dssss{putih}No   sNdo-    ym{cyan}ssss{putih}dmmNN{cyan}ysss{putih}hd    {putih}M\n{putih}M{cyan}dssss{putih}No   ..    `:sNm{cyan}yssssssssssss{putih}hd    {putih}N\n{putih}M{cyan}dssss{putih}No       `oNMMMm{cyan}ssssyssssssss{putih}hd    {putih}N\n{putih}M{cyan}dssss{putih}No         `:omm{cyan}ysss{putih}mMNNm{cyan}{cyan}ysss{putih}hd    {putih}N\n{putih}M{cyan}dssss{putih}No   oho:`    sm{cyan}ysss{putih}NMMMM{cyan}ysss{putih}hd    {putih}N\n{putih}M{cyan}dssss{putih}mo   :hNMM/   sm{cyan}ysss{putih}NMMMM{cyan}ysss{putih}hd    {putih}N\n{putih}M{cyan}dssss{putih}ms`    `:oyo:`sm{cyan}ysss{putih}NMMMM{cyan}ysss{putih}hd    {putih}N\n{putih}M{cyan}dsssshd{putih}my+.     `/sdm{cyan}ssss{putih}NMMMM{cyan}yhmmy:    {putih}N\n{putih}MNh{cyan}ysssssyd{putih}Nmy/.    /m{cyan}ssss{putih}NMMMM{cyan}do-`    {putih}.+M\n{putih}MMMMm{cyan}dysssssyd{putih}mMs   /m{cyan}syhm{putih}MNh+.     {putih}:smMMM\n{putih}MMMMMMMN{cyan}dhysssh{putih}My   /NNMmy:`    `/yNMMMMMM\n{putih}MMMMMMMMMMN{cyan}mhyh{putih}My   .yo-     .+hNMMMMMMMMM\n{putih}MMMMMMMMMMMMMMNM{putih}h.       `:sdMMMMMMMMMMMMM\n{putih}MMMMMMMMMMMMMMMMMM{putih}do- `/yNMMMMMMMMMMMMMMMM\n{putih}MMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMM\n\n{cyan}\tConcept : {putih}RSecxXx.iD a.k.a\n{hijau}\tAuthor : {putih}RSecxXx.iD\n{putih}\t[{hijau}UNLIMITED{putih}] {merah}Domain {putih}to {kuning}IP\n")
	site = open(input(f"{putih}input list site : ")).read().splitlines()
	print(f"{cyan}site in list : {putih}{len(site)}")
	for i in site:
		toip(i)
		print(f"{merah}error : {putih}{error} {cyan}| {hijau}success : {putih}{success} {cyan}| {magenta}total : {putih}{putih}{int(persen(total,len(site)))}% / 100%",flush=True,end="\r")
	print(f"\n{putih}result save in {cyan}({hijau}results/ips.txt{cyan})")
	print(f"{putih}result save in {cyan}({merah}results/error_ips.txt{cyan})")
except KeyboardInterrupt:exit()
except FileNotFoundError:exit(f"{merah}file not found !")
except OSError:exit(f"{merah}error !")