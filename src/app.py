from flask import Flask
import re
app = Flask(__name__)

@app.route('/')
def get_distinct_words():
    text = """
    Bali (bahasa Bali: ᬩᬮᬶ) adalah sebuah provinsi di Indonesia yang ibu kota provinsinya bernama
    Denpasar. Bali juga merupakan salah satu pulau di Kepulauan Nusa Tenggara. Di awal kemerdekaan
    Indonesia, pulau ini termasuk dalam Provinsi Sunda Kecil yang beribu kota di Singaraja,
    dan kini terbagi menjadi 3 provinsi, yakni Bali, Nusa Tenggara Barat, dan Nusa Tenggara
    Timur.[9][10] Pada tahun 2020, penduduk provinsi Bali berjumlah 4.317.404 jiwa,
    dengan kepadatan 747 jiwa/km2.[4]

    Selain terdiri dari pulau Bali, wilayah provinsi Bali juga terdiri dari pulau-pulau yang
    lebih kecil di sekitarnya, yaitu pulau Nusa Penida, pulau Nusa Lembongan, pulau Nusa Ceningan,
    Pulau Serangan, dan Pulau Menjangan. Secara geografis, Bali terletak di antara Pulau Jawa dan
    Pulau Lombok. Mayoritas penduduk Bali adalah pemeluk agama Hindu.[5] Di dunia, Bali terkenal
    sebagai tujuan pariwisata dengan keunikan berbagai hasil seni-budayanya, khususnya bagi
    para wisatawan Jepang dan Australia. Bali juga dikenal dengan julukan Pulau Dewata dan
    Pulau Seribu Pura.
    """

    # Remove all non-alpha chars
    text = re.sub("[^a-zA-Z ]+", "", text)

    # Get distrinct words with a length of > 3
    words = set(text.split())
    words = [word.lower() for word in words if len(word) > 3]

    # @todo
    # 1. Check if words do not exist in db
    # 2. Translate words
    # 3. Store words in db

    distinct_text = " ".join(map(str, words))

    return distinct_text