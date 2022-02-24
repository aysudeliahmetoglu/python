#listeler
liste=["python",234,"java",12367888]
print(len(liste)) # listenin uzunluğunu bulma
#indeksleme ve parçalama
print(liste[0])
print(liste[2:])
liste1=[1,2,3,4,5,6]
liste2=[7,8,9,10,11]
liste3=liste1+liste2
print(liste3*3)
#stringler değiştirilemez fakat listeler değiştirşilebilir
liste3[0]=45
print(liste3) #artık liste3 ün ilk elemanı 45
liste.append(7) #verdiğimiz değeri listeye ekler
print(liste)
liste.pop() #eğer içine indeks değeri vermezsek son elemanı çıkarır verirsek 
            #verdiğimiz indexteki elemanı listeden atar
print(liste)
liste=[9,23,45,12,1,234]
liste.sort() #listenin elemanlarını büyükten küçüğe sıralar
print(liste)
liste.sort(reverse=True) #büyükten küçüğe sıralama
print(liste)
#iç içe listeler
liste=[[1,2],[3,5]]
print(liste[1][0])
#Tuples(demetler) listelerden en temel farkı değiiştirelemez oluşudur.
demet=(1,2,2,2,2,2,2,3,4,5,6,7)
print(demet[3])
print(demet.count(2)) #değerin kaç defa tuple içinde geçtiğini gösterir.
print(demet.index(1)) #elemanın hangi indexte olduğunu gösterir.


