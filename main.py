from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vupsen')
def vupsen_page():
    link = "https://steamuserimages-a.akamaihd.net/ugc/1857175307721688347/0C8A31156E25AB955C983EAF0176E65C8AAAEA18/?imw=512&amp;imh=512&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true"

    description = "Несмотря на свой характер, Вупсеню не чужды страхи. В серии «Трусишка Вупсень», он не может спрыгнуть с батута, потому что боится высоты. В серии «Обманщики», Вупсень по этой же причине не соглашается на шутку с обрывом."

    return render_template('actor.html', name="Вупсень", description=description, img=link)

@app.route('/pupsen')
def pupsen_page():
    link = "https://yt3.googleusercontent.com/lKjG4zl_ze1eVPV9YIjNeejSHJXv_Nf8Y-w_vJrj23QByjgeUAfTnJOhr0RkmQKwds0SnoSuSwc=s900-c-k-c0x00ffffff-no-rj"
    description = "Пупсень - брат Вупсеня. С начала он может показаться глупым(на самом деле это так и есть), но потом мы можем заметить его блистательный ум"

    return render_template('actor.html', name="Пупсень", description=description, img=link)

@app.route('/luntic')
def luntic_page():
    link = "https://yt3.googleusercontent.com/f80Gxwy6xsy8FCdAJOu60llemXJyAixvdTiIZiRvYQjJBy4QfREAgBEc1SXOHAkMozbufWa6=s900-c-k-c0x00ffffff-no-rj"
    description = "Лунтик - главный персонаж. Упал с луны. Очень добрый и позитивный"

    return render_template('actor.html', name="Лунтик", description=description, img=link)


@app.route('/kuzya')
def kuzya_page():
    link = "https://static.wikia.nocookie.net/ac2a2668-bab5-440d-95ef-8c8f79978650"
    description = "Кузя - лучший друг лунтика."

    return render_template('actor.html', name="Кузя", description=description, img=link)




# TODO: добавь страницы еще хотя бы двух персонажей

app.run(debug=True)