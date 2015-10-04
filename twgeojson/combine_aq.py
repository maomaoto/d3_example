import json
import os

if __name__ == "__main__":
	fin = open(".\\air_quality_site.json", "r")
	sin = fin.read()
	fin.close()
	din = json.loads(sin)
	print(type(din))
	#print(din)
	
	fin = open(".\\air_quality_20151004_1900.json", "r")
	sin = fin.read()
	fin.close()
	dict_quality = json.loads(sin)
	
	sites = {}
	for site in din:
		sites[site["SiteName"]] = {"Lon": site["TWD97Lon"], "Lat": site["TWD97Lat"]}
	
	for itr in dict_quality:
		try:
			sites[itr["SiteName"]]["value"] = int(itr["PM2.5"])
		except:
			sites[itr["SiteName"]]["value"] = 0
		
	#print(sites)
	

	
	fout = open(".\\combine.json", "w")
	sout = json.dumps(sites,sort_keys=True, indent=4)
	fout.write(sout)
	fout.close()
	