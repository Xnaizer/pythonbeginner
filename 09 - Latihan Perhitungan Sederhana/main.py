#latihan konversi satuan temperatur

# Program konversi celcius ke satuan lain

print("\nProgram Konversi Temperature\n")

celcius = float(input("Masukkan suhu dalam Celcius : "))
print("suhu adalah " , celcius, "Celcius")

# Reamur
reamur = ( 4 / 5 ) * celcius
print("suhu reamur adalah " , reamur, "Reamur")



# Fahrenheit
fahrenheit = (( 9 / 5 ) * celcius ) + 32
print("suhu fahrenheit adalah " , fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu kelvin adalah " , kelvin, "kelvin")

fahrenheitkelvin = ( 5 / 9 * ( fahrenheit - 32 ))
fk = fahrenheitkelvin + 273
print("suhu fahrenheit : ", fahrenheit, " ke kelvin  adalah " , fk, "K")

kelvinfahrenheit = kelvin - 273
kf = (( 9 / 5 ) * kelvinfahrenheit) + 32
print("suhu kelvin : ", kelvin, " ke fahrenheit adalah " , kf, "f")

