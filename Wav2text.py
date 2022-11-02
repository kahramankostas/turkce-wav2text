
# coding: utf-8

# ### Bu kısa kod vereceğiniz klasör içersindeki wav dosyalarını aynı klasör içerinde ve aynı isimde txt dosyalarına çevirir. google API kullanıldığı için çalışma sırasında internet bağlantınızın olması gerekir

# ## Gerekli modüllerin alınması.
# ### SpeechRecognition modülü yoksa kurulumu yapar.

# In[6]:


#get_ipython().system('pip3 install SpeechRecognition')
import speech_recognition as sr
import os


# ### wav dosyalarını içeren klasörünüzün ismini yazın - python/jupyter dosyası ile aynı klasör içerisinde olmalı



klasor="sesler"


# ### Bu fonksiyon klasör içersindeki wav dosyalarını bulur ve listeler

# In[9]:


def dosya_bul(yol,dosya_uzantisi):
    dosya_listesi = []
    for r, d, f in os.walk(yol):
        for dosya in f:
            if dosya_uzantisi in dosya:
                dosya_listesi.append(os.path.join(r, dosya))  
    return dosya_listesi
dosya_listesi=dosya_bul("./"+klasor,'.wav')
dosya_listesi


# ## Tüm wav dosyalarını txt dosyasına çevirerek kaydeder.

# In[10]:


for dosya in dosya_listesi:
    r = sr.Recognizer()
    islem_goren=sr.AudioFile(dosya)
    with islem_goren as kaynak:
        ses_kaydi = r.record(kaynak)
    try:
        metin = r.recognize_google(ses_kaydi, language='tr-tr')#,enable_word_time_offsets=True)#,"enableWordTimeOffsets": true)
        print(dosya,":",metin)
        ths = open(str(dosya[:-4])+".txt", "w", encoding="utf-8")
        ths.write(metin)
        ths.close()
        
    except Exception as e:
        print("HATA!!!: "+str(e))

