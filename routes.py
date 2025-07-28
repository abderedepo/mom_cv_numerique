from flask import render_template, send_from_directory

def init_routes(app):

    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route('/a-propos')
    def about():
        return render_template("about.html")

    @app.route('/projets')
    def projects():
        return render_template("projets.html")

    @app.route('/competences')
    def skills():
        return render_template("skills.html")

    @app.route('/experience')
    def experience():
        return render_template("experience.html")

    @app.route('/formation')
    def education():
        return render_template("education.html")

    @app.route('/blog')
    def blog():
        return render_template("blog.html")

    @app.route('/temoignages')
    def testimonials():
        return render_template("testimonials.html")

    @app.route('/contact')
    def contact():
        return render_template("contacts.html")

    @app.route('/langues')
    def languages():
        return render_template("languages.html")

    @app.route('/interets')
    def interests():
        return render_template("interests.html")

    @app.route('/telechargement')
    def download_cv():
        return send_from_directory('static', 'cv_abderemne.pdf', as_attachment=True)
