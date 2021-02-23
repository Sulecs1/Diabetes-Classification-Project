# Diabetes-Classification-Project
Genel Bakış
Veriler, Pima Indians Diyabet Veritabanının bir parçası olarak "Ulusal Diyabet ve Sindirim ve Böbrek Hastalıkları Enstitüsü" tarafından toplanmış ve kullanıma sunulmuştur. Bu örneklerin daha büyük bir veritabanından seçilmesiyle ilgili çeşitli kısıtlamalar getirildi. Özellikle,
Buradaki tüm hastalar Pima Kızılderili mirasına (Yerli Amerikalıların alt grubu) aittir ve 21 yaş ve üstü kadınlardır.
Başlangıçta veri setimizin genel yapısı şu şekildedir
Observations: 768
Variables: 9
cat_cols: 1
num_cols: 8

Bir kişinin şeker hastası olup olmadığını tahmin etmemize yardımcı olmak için aşağıdaki özellikler sağlanmıştır:
Gebelikler(Pregnancies): Hamile kalma sayısı
Glikoz(Glucose): Oral glikoz tolerans testinde 2 saatin üzerinde plazma glikoz konsantrasyonu
Kan Basıncı(BloodPressure): Diyastolik kan basıncı (mm Hg)
85 :2 yılda bir kontrol edilmeli
85-89 : Senede bir
90-99 : 2 ay içinde
100-109 : 1 ay içinde
110  : 1 hafta içinde ya da hemen kontrol edilmelidir

SkinThickness(SkinThickness): Triceps cilt kıvrımı kalınlığı (mm)
İnsülin(Insulin): 2-Saat serum insülini (mu U / ml)
BMI: Vücut kitle indeksi (kg cinsinden ağırlık / (m cinsinden yükseklik) 2)
18.5 zayıf
19.18.5-24.9 sağlıklı
25-29.9 kilolu
30-40 şişman
40.1-60 aşırı şişman


Diyabet Pedigree Fonksiyonu(DiabetesPedigreeFunction): Diyabet soy ağacı fonksiyonu (aile geçmişine göre diyabet olasılığını puanlayan bir fonksiyon)
Yaş(Age): Yaş (yıl)
Sonuç(Outcome): Sınıf değişkeni (diyabetik değilse 0, diyabetikse 1)

Veri Setimizde eksik gözlem bulunmamaktadır
Pregnancies                 0
Glucose                     0
BloodPressure               0
SkinThickness               0
Insulin                     0
BMI                         0
DiabetesPedigreeFunction    0
Age                         0
Outcome                     0
dtype: int64

Isı haritasında, daha parlak renkler daha fazla korelasyonu gösterir. Tablodan ve ısı haritasından da görebileceğimiz gibi, glikoz seviyeleri, yaş, vücut kitle indeksi ve gebelik sayısı, sonuç değişkeni ile önemli bir korelasyona sahiptir. Ayrıca yaş ve gebelikler veya insülin ve cilt kalınlığı gibi özellik çiftleri arasındaki korelasyona dikkat ediniz.


