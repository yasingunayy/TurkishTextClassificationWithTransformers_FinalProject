# Turkish Text Classification With Transformers


![arayuz01](https://github.com/yasingunayy/TurkishTextClassificationWithTransformers_FinalProject/assets/121442500/44383ff5-9073-4a98-8941-2221198f308e)

![arayuz02](https://github.com/yasingunayy/TurkishTextClassificationWithTransformers_FinalProject/assets/121442500/f336d566-6be6-4bac-b9fd-3550840ab37d)

Bu metin sınıflandırma uygulaması, belediyelere gelen yazılı şikayetlerin ilgili birim ve konu bakımından
sınıflandırılmasını kapsamaktadır.

- Veri Seti Şikayetvar üzerinden gerçek kullanıcıların yazdığı şikayet metinlerinden oluşmaktadır.
- Veriler Manuel olarak toplanmıştır.
- Eğitim veri seti 2698 adet ve Doğrulama veri seti 289 adet etiketli metin verisinden oluşturulmuştur.
- Eğitimin ve Test işlemlerinin yapıldığı kodlar ve veri seti Train klasörü içerisinde paylaşılmıştır.
- Bu modelde https://github.com/stefan-it/turkish-bert modeli base model olarak kullanılmıştır.
- Model 8 farklı kategoride sınıflandırma işlemi gerçekleştirmektedir.
- Uygulama, Fırat Üniversitesi Bilgisayar Mühendisliği Bölümünde Bitirme Projesi olarak sunulmuştur.
- Uygulama, Python 3.11.7 sürümü üzerinde yapılandırılmıştır.Farklı sürümlerde, kullanılan kütüphanelerde kaynaklı olarak hatalar ile karşılaşılabilir.
- Modelde kullanılan sınıflar aşağıda görüldüğü gibi tanımlanmıştır.

code_to_label={
'LABEL_0': 'Su ve Kanalizasyon',
'LABEL_1': 'Ulaşım',
'LABEL_2': 'Park ve Bahçeler',
'LABEL_3': 'Zabıta',
'LABEL_4': 'Temizlik İşleri' ,
'LABEL_5': 'Veteriner İşleri',
'LABEL_6': 'Sosyal Hizmet ve Yardımlar',
'LABEL_7': 'Diğer' }
