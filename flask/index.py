from flask import Flask,render_template

my_app =Flask(__name__)

my_skills =[('html',59), ('css',90), ('js',80), ('python', 40), ('mySql', 98)]
@my_app.route("/")
def homePage():
    return render_template('homepage.html', pagetitle="HomePage", custom_css="homestyle.css")

@my_app.route("/about")
def about():
    return render_template('aboutpage.html', pagetitle="AboutUsPage")

@my_app.route('/add')
def add():
    return render_template('add.html', pagetitle="add page", custom_css="addstyle.css")

@my_app.route('/skills')
def skills():
    return render_template('skills.html',
                            pagetitle="My Skills",
                            page_head="My Skills",
                            description=" This Is My Skills Page",
                            skills= my_skills,
                            custom_css="skillsstyle.css"
                            )



if __name__ == "__main__":
    my_app.run(debug=True, port=9000)