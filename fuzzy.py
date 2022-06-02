#mendefinisikan variabel pada fungsi turun
#variabel mini sebagai nilai minimum
#variabel maxi sebagai nilai maxsimum
def turun(maxi,mini,x):
    if(x<=mini): 
        nilai = 1
    elif(x>mini and x<maxi):
        nilai = (maxi-x)/(maxi-mini)
    elif(x>=maxi): 
        nilai = 0
    return nilai

#mendefinisikan variabel pada fungsi naik
def naik(maxi,mini,x):
    if(x<=mini):
        nilai = 0
    elif(x>mini and x<maxi):
        nilai = (x-mini)/(maxi-mini)
    elif(x>=maxi):
        nilai = 1
    return nilai
#mendefinisikan variabel pada fungsi inferensi Turun
def inferensiTurun(maxi,mini,alfa):
    nilai = maxi - (alfa*(maxi-mini))
    return nilai
#mendefinisikan variabel pada fungsi agregasi Naik
def inferensiNaik(maxi,mini,alfa):
    nilai = alfa*(maxi-mini) + mini
    return nilai

var = int(input("Jumlah variabel: "))
nama_var = []
for i in range(var):
    nama = input("Sebutkan nama variabel: ")
    nama_var.append(nama)
print("+--------------------------------+")
    
variabel = dict()
for i in nama_var:
    print()
    print(i)
    up = int(input("Naik  : "))
    down = int(input("Turun : "))
    variabel.update({i+"_naik":up})
    variabel.update({i+"_turun":down})

soal = { } #merupakan dictionary soal
print("\n+--------------------------------+")
jml = int(input("Jumlah variabel yang diketahui : "))
for i in range(jml):
    ver = input("Nama variabel : ")
    val = int(input("Nilai : "))   
    soal.update({ver:val})  

produksi = input("Variabel yang ditanyakan : ")
nk = dict()
for i in soal:
    up = naik(variabel[i+"_naik"],variabel[i+"_turun"],soal[i])
    down = turun(variabel[i+"_naik"],variabel[i+"_turun"],soal[i])
    nk.update({i+"_naik":up})
    nk.update({i+"_turun":down})
print()
print(nk)

#inferensi
alfa = []
z = []
r = int(input("\nMasukkan jumlah peraturan : "))
for i in range(r):
    print("Rule",i+1)
    k1 = input("Kondisi : ")
    k2 = input("Kondisi : ")
    kesimpulan = input("Kesimpulan(naik/turun): ")
    
    #Fire Strength INTERSEKSI (AND)
    mini = min(nk[k1],nk[k2]) 
    alfa.append(mini)
    if(kesimpulan == "turun"):
        R = inferensiTurun(variabel[produksi+"_naik"],variabel[produksi+"_turun"],mini)
    elif(kesimpulan == "naik"):
        R = inferensiNaik(variabel[produksi+"_naik"],variabel[produksi+"_turun"],mini)        
    z.append(R)
print()   
print("alfa =",alfa)
print("Z = ",z)

#DEFUZIFIKASI
df = 0
for i in range(len(alfa)):
    df += alfa[i]*z[i] #rumus mencari perkalian alfa dengan z
produk = int(df/sum(alfa)) #hasil perklaian alfa[i] dan z[i] kemudian di bagi dengan jumlah alfa
print("\nJadi, nilai produksi adalah ",produk)