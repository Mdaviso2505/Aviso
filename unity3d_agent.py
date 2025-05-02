import random
import string
def get_user_agent():
    os_version = random.choice([
    "11", "12", "13", "14"
    ])
    device_makes = random.choice([
    "samsung", "google", "oneplus", "xiaomi", "oppo", "vivo", "asus", "realme"
    ])
    samsung_model = random.choice([
    "SM-A156M", "SM-G991B", "SM-A715F", "SM-N986B", "SM-G998B", "SM-A325F",
    "SM-M525F", "SM-S901E", "SM-F916B", "SM-G780G", "SM-A136B", "SM-N975F",
    "SM-G973F", "SM-G950F", "SM-A525F", "SM-A102U", "SM-G935F", "SM-N960F",
    "SM-A115F", "SM-G570F", "SM-A135F", "SM-N975U", "SM-G965F", "SM-A515F",
    "SM-S908B", "SM-G970F", "SM-N975W", "SM-G973U", "SM-A325U", "SM-G928F",
    "SM-A710F", "SM-G920F", "SM-G935W8", "SM-G977B", "SM-A520F", "SM-G950U",
    "SM-J530F", "SM-N950F", "SM-A703F", "SM-G965U", "SM-G965W", "SM-G800F",
    "SM-N976B", "SM-G780F", "SM-A707F", "SM-G570Y", "SM-A125F", "SM-N975F",
    "SM-S767V", "SM-A328B", "SM-N960U", "SM-G670F", "SM-A505F"
    ])
    google_model = random.choice([
    "GD1YQ", "G025I", "G020A", "G020B", "G020F", "G020J", "G020P", "G020X", "G020Q", "G020R",
    "G020U", "G020V", "G021A", "G021B", "G021C", "G021F", "G0220", "G0221", "G0222", "G0230",
    "G0231", "G0232", "G0240", "G0241", "G0242", "G0243", "G025A", "G025B", "G025C", "G026A",
    "G027A", "G028A", "G029A", "G030A", "G030B", "G030C", "G030D", "G031A", "G031B", "G031C",
    "G032A", "G032B", "G033A", "G033B", "G034A", "G034B", "G035A", "G036A", "G037A", "G038A"
    ])
    oneplus_model = random.choice([
"A6000", "A6010", "A6013", "A5010", "A5000", 
    "A7000", "A7001", "A7003", "A6013", "BE2013", 
    "BE2028", "BE2012", "GM1911", "GM1913", "GM1901", 
    "GM1903", "HD1901", "HD1903", "IN2010", "IN2020", 
    "IN2021", "LE2110", "LE2113", "LE2115", "LE2120", 
    "LE2127", "LE2123", "LA2001", "LA2003", "LA2020", 
    "LU2020", "LU2030", "LU2033", "LU2025", "LU2028", 
    "X9000", "X9003", "X9001", "X9010", "RMX1911", 
    "RMX1913", "RMX1921", "RMX1931", "RMX1993", "RMX2051", 
    "RMX2053", "RMX2063", "RMX2075", "RMX2101", "RMX2103"
    ])
    xiaomi_model = random.choice([
    "M2001J2G", "M2003J15SC", "M2004J19C", "M2005J5BC", "M2006C3LI", "M1902F1G", "M1901F7G", 
    "M1901F9G", "M1908C3JH", "M2101K6G", "M2102J20SG", "M2103K19AG", "M2103J20SI", "M2104J19PI", 
    "M2105K81AC", "M2105K81C", "M2010J19SC", "M2010J19SI", "M2104J19AG", "M2102J20IC", "M2012K11AG", 
    "M2013K19G", "M2003J6A1", "M1904F3GT", "M2007J3SG", "M2004J11G", "M1906J15SG", "M2006C3LG", 
    "M2101K7AG", "M2005J5AI", "M2010J19CG", "M1901F9G", "M2011K9G", "M2004J19IG", "M2105K81AG", 
    "M2006C3KG", "M2101K6G", "M2004J9G", "M2101K6AG", "M2005J5AI", "M2006J1AC", "M2003J7BC", 
    "M2004J10CG", "M2007J3AG", "M2008J3SG", "M1905F9G", "M2009J2SC", "M2101K7SG"
    ])

    oppo_model = random.choice([
    "CPH1923", "CPH1917", "CPH1909", "CPH1903", "CPH1819", "CPH1609", "CPH1591", "CPH1581",
    "CPH1571", "CPH1561", "CPH1541", "CPH1523", "CPH1511", "CPH1505", "CPH1491", "CPH1481",
    "CPH1461", "CPH1451", "CPH1441", "CPH1431", "CPH1419", "CPH1409", "CPH1393", "CPH1385",
    "CPH1373", "CPH1365", "CPH1355", "CPH1343", "CPH1339", "CPH1327", "CPH1311", "CPH1309",
    "CPH1303", "CPH1299", "CPH1297", "CPH1291", "CPH1289", "CPH1281", "CPH1277", "CPH1273",
    "CPH1265", "CPH1257", "CPH1249", "CPH1239", "CPH1223", "CPH1215", "CPH1205", "CPH1195",
    "CPH1185", "CPH1177", "CPH1169"
    ])
    vivo_model = random.choice([
    "V1936A", "V1820A", "V1911A", "V1932A", "V1928A", "V1822A", "V1838A", "V1818A", 
    "V1825A", "V1933A", "V1916A", "V1918A", "V1858A", "V1860A", "V1845A", "V1831A", 
    "V1875A", "V1865A", "V1922A", "V1819A", "V1852A", "V1826A", "V1859A", "V1871A", 
    "V1815A", "V1904A", "V1906A", "V1851A", "V1848A", "V1910A", "V1912A", "V1931A", 
    "V1823A", "V1839A", "V1854A", "V1814A", "V1846A", "V1886A", "V1868A", "V1902A", 
    "V1827A", "V1862A", "V1903A", "V1843A", "V1824A", "V1879A", "V1857A", "V1888A", 
    "V1874A", "V1890A", "V1901A"
    ])
    asus_model = random.choice([
    "ZS570KL", "ZS600KL", "ZC554KL", "ZB602KL", "ZB601KL", "ZC520TL", "ZC553KL", "ZC554KL", 
    "ZB602KL", "ZB601KL", "ZS600KL", "ZB570TL", "ZB552KL", "ZC520KL", "ZC553KL", "ZS660KL", 
    "ZS676KL", "ZB633KL", "ZB634KL", "ZC580KL", "ZC555KL", "ZS550KL", "ZB555KL", "ZC590KL", 
    "ZC580KL", "ZB631KL", "ZS670KL", "ZC551KL", "ZC570KL", "ZC650KL", "ZB550KL", "ZB560KL", 
    "ZS660KL", "ZB633KL", "ZB636KL", "ZC551KL", "ZC550KL", "ZS602KL", "ZB634KL", "ZC545KL", 
    "ZB640KL", "ZC600KL", "ZB637KL", "ZS680KL", "ZS620KL", "ZC510KL", "ZB643KL", "ZC560KL", 
    "ZC500KL", "ZS655KL", "ZS618KL"
    ])
    realme_model = random.choice([
    "RMX1801", "RMX1831", "RMX1921", "RMX1925", "RMX1931", "RMX1971", "RMX2040", "RMX2041", 
    "RMX2061", "RMX2075", "RMX2076", "RMX2081", "RMX2085", "RMX2095", "RMX2101", "RMX2103", 
    "RMX2201", "RMX2202", "RMX2233", "RMX2235", "RMX2242", "RMX2255", "RMX2256", "RMX2261", 
    "RMX2300", "RMX2301", "RMX2310", "RMX2312", "RMX2321", "RMX2333", "RMX2341", "RMX2345", 
    "RMX2355", "RMX2401", "RMX2403", "RMX2410", "RMX2412", "RMX2451", "RMX2500", "RMX2501", 
    "RMX2510", "RMX2520", "RMX2530", "RMX2550", "RMX2561", "RMX2600", "RMX2610", "RMX2620", 
    "RMX2700", "RMX2710", "RMX2720"
    ])
    device_model = {
    "samsung": samsung_model,
    "google": google_model,
    "oneplus": oneplus_model,
    "xiaomi": xiaomi_model,
    "oppo": oppo_model,
    "vivo": vivo_model,
    "asus": asus_model,
    "realme": realme_model
    }.get(device_makes)
    chrome_version = random.choice(["135.0.7049.38","134.0.6998.135","134.0.6998.108","134.0.6998.95","133.0.6943.137", "133.0.6943.121", "133.0.6943.49", "132.0.6834.163", "132.0.6834.122", "131.0.6778.260", "131.0.6778.200", "131.0.6778.135", "131.0.6778.104", "131.0.6778.81", "131.0.6778.39"])
    
    build_version = {"14": "U", "13": "T", "12": "S", "11": "R"}[os_version]+"P1A."+f"{random.randint(20, 25)}{random.randint(1, 12):02}{random.randint(1, 30):02}"+".007"
    build_name = " Build/"+build_version
    user_agent = "Mozilla/5.0 (Linux; Android "+os_version+"; "+device_model+build_name+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+chrome_version+" Mobile Safari/537.36"
    dalvik_agent = "Dalvik/2.1.0 (Linux; U; Android "+os_version+"; "+device_model+build_name+")"
    
    model_split = str(max(device_model.split('-'), key=len) if '-' in device_model else device_model)
    random_string = ''.join(random.choices(string.ascii_uppercase, k=7))
    finger_print = device_makes+"/"+model_split.lower()+"/"+model_split.lower()+":"+os_version+"/"+build_version+"/"+model_split+random_string+"1:user/release-keys"
    
    return [os_version,device_makes,device_model,dalvik_agent,user_agent,finger_print]

print(get_user_agent())
