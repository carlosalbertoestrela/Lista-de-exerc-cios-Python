# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo_mb = float(input(f'tamanho do arquivo: Mb '))
link_vel = float(input('Velocidade do link: Mbps '))
converte_mbit = arquivo_mb / .125
tempo_min = (converte_mbit / link_vel) // 60
tempo_seg = (converte_mbit / link_vel) % 60
print(f'O tempo aproximado de download é {tempo_min:.0f}:{tempo_seg:.0f}min')
