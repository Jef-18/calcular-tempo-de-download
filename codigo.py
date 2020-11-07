#download
v_download = float(input("Digite o tamanho do arquivo para download(MB): "))

# internet 
v_link_internet =  float(input("Digite o tamanho do seu link de internet (Mbps): "))
v_link_internet = v_link_internet/8

#tempo aproximado
v_minutos = (v_download / v_link_internet) / 60

#resultado
print("")
print("O tempo aproximado para download é: ", round(v_minutos,2),"s")

