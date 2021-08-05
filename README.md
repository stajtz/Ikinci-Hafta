# Tracking

OpenCVde birkaç tane farklı takip (tracker) algoritmaları vardır. Bunlardan bazıları are BOOSTING, MIL, KCF, TLD, MEDIANFLOW, GOTURN, MOSSE ve CSRT’dır.

BOOSTING:
Bu izleyici, yaklaşık on yıllık, eski , yavaş ve daha az verimli. Yalnızca eski nedenlerle ve diğer algoritmaların karşılaştırılması için hala kullanılmaktadır.

MIL:
Bu izleyici, BOOSTING izleyicisine kıyasla daha iyi doğruluk sağlar. Ancak MIL izleyicinin ana dezavantajı, raporlama hatasından muzdarip olmasıdır.

KCF:
Kernelized Correlation Filters izleyici, BOOSTING ve MIL ile karşılaştırıldığında daha hızlıdır. Aynı şekilde MIL KCF, kişinin boyutu ve pozisyonunda değişiklik olduğunda fazla verim vermez.

TLD :
OpenCV ile TLD Tracker'ın uygulanmasında sorun olma olasılığı yüksektir. Çünkü; TLD izleyici aşırı derecede yanlış pozitiflerden muzdaripti. Bu OpenCV nesne izleyicisi, anormal davranışı nedeniyle önerilmez.

MEDIANFLOW:
Bu model, harekette büyük bir sıçrama, hızlı hareket ve ani görünüm değişikliği ile karşılaştığında başarısız olacaktır. 

MOSSE:
MOSSE çok hızlıdır ancak CSRT veya KCF'den nispeten daha az doğrudur. Bu izleyici, saf hıza ihtiyacınız olduğunda iyi bir seçimdir.

CSRT:
Ayrımcı Korelasyon Filtresi (Kanal ve Mekansal Güvenilirlik ile). Bu izleyici, KCF'den nispeten daha doğru ancak biraz daha yavaştır.

Benim gözlemlerim
MOSSE, BOOSTING, MIL, TLD, MEDIANFLOW, CSRT: Araç görüntüden çıktıktan sonra takip için oluşturulan bounding box başka nesneler için ekranda kaldı.
MOSSE, KCF: Araç gözden kaybolunca bounding box da ekrandan kayboldu.

Bu bilgiler ve gözlerimlerim sonucunda projenin şuanki aşamasında KCF kullanmaya karar verdim

Kaynak

https://learnopencv.com/object-tracking-using-opencv-cpp-python/
https://www.youtube.com/watch?v=1FJWXOO1SRI
https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8877025&casa_token=IGHmjeNY2loAAAAA:8O42EVirND8wD5ev8qunovoWS8EICsgfwvQPerh5HoOGPE2cTJMxR5jqUbSEd2fSOZqqyOL16Q&tag=1
