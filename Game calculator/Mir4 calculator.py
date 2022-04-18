import time

pva = input ('Quantidade de poções de vida: ')
tpv = input ('Digite o tamanho da potion, P para pequena M para média e G para grande: ')

if tpv == 'p':
    vv = 10
elif tpv =='m':
    vv = 30
elif tpv == 'g':
    vv = '90'

pma = input ('Quantidade de poções de mana: ')
tpm = input ('Digite o tamanho da potion, P para pequena M para média e G para grande: ')

if tpm == 'p':
    vm = 10
elif tpm =='m':
    vm = 30
elif tpm == 'g':
    vm = '90'

xpa = input ('Digite a porcentagem de xp atual: ')

print ('Volte para preencher os dados após 15 Minutos!')

time.sleep(900)

pvd = input('Quantidade de poções de vida: ')
pmd = input('Quantidade de poções de mana: ')
xpd = input('Digite a porcentagem de xp atual: ')

pvf = int(pva) - int(pvd)
pmf = int(pma) - int(pmd)
xpf = int(xpd) - int(xpa)

print ("Foram consumidas {0} potions de vida {1} potions de mana e subiu {2} porcento de xp!".format(pvf,pmf,xpf))

vpv = int(pvf) * int(vv)
vpm = int(pmf) * int(vm)
tt = vpv + vpm

print ('Foram gastos um total de {} cobre'.format(tt))

#xpfut = int(xpd) - 100