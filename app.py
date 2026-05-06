from flask import Flask, render_template
app = Flask(__name__)
oyuncular= [
    "Murat Akçakoç",
    "Enes Altundaş",
    "Servet Karabat",
    "Servet Tekdemir",
    "Bayram İlter",
    "Bayram Kartalmış",
    "Osman Işık",
    "Ali Işık",
    "Adem Alakaş",
    "Emin Ayhan",
    "Taha Yasin Karabat",
    "Okan Ayyıldız",
    "Ahmet Tilbaç",
    "Fırat Akbalık",
    "Fatih Kartalmış",
    "Güven Kocayiğit",
    "Mustafa Altundaş",
    "Samet Dalkılıç",
    "Burak Timurtaş",
    "Ercan Eşsiz",
    "Miraç Akçakoç",
    "Erol Tekdemir"
]

maclar = [
    "Nohutluspor 1 - 0 Arhalan",
    "Nohutluspor - Ulutaş Sorguçlu",
    "Nohutluspor - Gertan",
    "Nohutluspor - Maman",
    "Nohutluspor - Tatlıcak",
    "Nohutluspor - Kayadere",
    "Nohutluspor - Hüsükuşağı"
]
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/oyuncular")
def oyuncular_sayfa():
    return render_template("oyuncular.html", oyuncular=oyuncular)
@app.route("/maclar")
def maclar_sayfa():
    return render_template("maclar.html", maclar=maclar)
app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)