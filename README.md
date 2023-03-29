# Python-Selenium-Kamp-

DECORATORS
Fonksiyon ve metotlar çağrılabilirdir. __call__() özel metodu ile herhangi bir nesneye çağırma işlemi uygulanabilir. Bir decorator’de çağrılabilen bir nesnedir. Temel olarak bir decorator bir fonksiyonu alır, yeni fonksiyonellikler ekler ve döndürür. Dekoratörler, temelde alınan parametreyi iç fonksiyona (wrapper) gönderen ve geriye de bu fonksiyonu döndüren fonksiyonlardır. İç fonksiyonları dekoratör yazmadığınız durumlarda da kullanabilirsiniz.

-@pytest.mark.skip: Bu anotasyon ilgili test fonksiyonunu herhangi bir koşul belirtmek zorunda olmaksızın atlamayı sağlar. İstenirse ilgili testin neden atlandığına dair bir not (reason) belirtilebilir.

-@pytest.mark.skipif: pytest.mark.skip anotasyonuna benzer şekilde yine bir testi atlamak için kullanılır. Ancak bu sefer atlama işlemi verilen bir şarta bağlıdır. Bu anotasyon için koşul vermek zorunlu bir parametre iken, sebep belirtmek yine tercihen yapılabilir.

-@pytest.mark.usefixtures: Bu dekoratör daha önceden fixture olarak işaretlenmiş bir yapıyı (örneğin bir metodu) bir test koşulmadan önce çağırıp kullanmaya yarar.
-@pytest.mark.xfail: Bir test işleminden "başarısız sonuç beklediğimizi " belirtmek için bu anotasyon kullanılır.

-@pytest.mark.parametrize: Bu dekoratör, test işlevlerini farklı argüman kombinasyonları ile çalıştırmak için kullanılır.

-@pytest.mark.timeout: Bir test işlevinin belirli bir süre içinde tamamlanması gerektiğini belirtir

-@pytest.mark.usefixtures: Bir test işlevinin çalışması için gerekli olan bir veya daha fazla araç setini belirler.
