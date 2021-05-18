# Q-Learning ile Yol Planlaması

Pekiştirmeli öğrenme (reinforcement learning), öznelerin (agent) bir görevi en yüksek
kazançla tamamlayabilmek için hangi eylemleri gerçekleştirmeleri gerektigi ile
ilgilenen bir makine öğrenmesi tekniğidir. Bu tür öğrenme algoritmaların girdisi
öznelerin görev yapacakları farklı durumlardan oluşan bir ortam S, yapabilecekleri
eylemler A, ortamdaki durumuna göre yapabilecekleri eylemleri belirleyen prensipler, bir
durumdan diğer duruma geçtiklerinde elde edecekleri kazançtır.
Q-learning pekiştirmeli bir öğrenme algoritmasıdır. Ortam hakkında hiçbir şeyin
bilinmediği durumlarda, Q-learning algoritması ortamı brute-force şeklinde, her
ortam için olası tüm aksiyonları takip ederek, problem çözümü için en karlı yolu
bulmaya çalışır. Q-learning algoritmasının girdileri kazanç matrisi olarak adlandırılan R
matrisidir. Bu matrisin satır ve sütunları ortamları temsil etmekte, R[i][j] değeri ise i
durumundan j durumuna geçtiğinde elde edilen anlık kazanç değeridir. Eğer i
durumunda j durumuna bir geçiş yoksa R[i][j] değeri -1, geçis var ancak j durumu
hedef durum değilse değeri 0, j hedef durum ise değeri kullanıcı tarafından belirlenen bir
kazanç değeridir.
Q-learning algoritmasının çıktısı ise öğrenmenin kalitesini gösteren Q matrisidir.
Q-learning iteratif bir algoritmadır ve tüm değerleri başlangıçta 0 olan Q matrisi
optimal değerlere yakınsadığı da sona erer. Algoritma her iterasyonda rastgele bir
durumdan öğrenmeye baslar, A’ya göre durum değiştirir ve Q matrisini günceller.
A’ya göre hedef duruma ulaşıldığında iterasyon sona erer. A’ya göre bir durumdan
birden fazla duruma geçis olabilir. Boyle bir durumda, olası geçişler den biri rastgele
seçilir. Eğer seçilen durum hedef duruma ulaştırmıyorsa, durum rastgele olacak durum
olarak belirlenir. Hedef duruma ulaşılana
kadar iterasyon devam eder. Q matrisi aşağıdaki formüle göre güncellenir:
```
Q(durum, aksiyon) = R(durum, aksiyon)+γ×Max{Q(sonraki durumlar, tüm aksiyonlar)} γ
```
ogrenme katsayısıdır ve 0 ile 1 arasında bir değer alır.

Aşağıdaki örnek Q-learning algoritmasını çalışmasını kısaca açıklamaktadır. Figür
1’de 6 durumdan oluşan bir ortam verilmistir.Durumlar arası geçişler de oklar ile
göstermektedir.

<img src=https://github.com/rknyryn/Q-Learning/blob/main/images/figure1.png>

Buna göre R matrisi ve Q matrisinin ilk hali aşağıdaki gibi olur.

<img src=https://github.com/rknyryn/Q-Learning/blob/main/images/r-q-matrix.png>

## Kurulum
```
pip install pygame
pip install pygame-menu
pip install matplotlib
pip install texttable
pip install validators
```
