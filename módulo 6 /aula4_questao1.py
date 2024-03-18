lista_par = [i for i in range(20,51, 2)]
print (lista_par)

lista_qua = [i**2 for i in range(1,10)]
print (lista_qua)

lista_7 = [i for i in range(1, 100)]
filt7 = [i for i in lista_7 if i % 7 == 0]
print (filt7)

lista_par_impar = [i for i in range(0,30,3)]
filt_pi = ['Par' if n % 2 == 0 else 'Impar' for n in lista_par_impar]
print (filt_pi)

