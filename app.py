from flask import Flask, render_template, request, redirect, url_for
from models import db, StudyGroup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studyfinder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


@app.route('/')
def index():
    return redirect(url_for('list_groups'))


@app.route('/groups')
def list_groups():
    """
    Story: 'Student can create a new group with an exact schedule
    for other students to filter.'
    This route handles the filtering half of that story.
    """
    course_filter = request.args.get('course', '').strip()
    day_filter = request.args.get('day', '').strip()

    query = StudyGroup.query
    if course_filter:
        query = query.filter(StudyGroup.course_code.ilike(f"%{course_filter}%"))
    if day_filter:
        query = query.filter_by(day_of_week=day_filter)

    groups = query.order_by(StudyGroup.day_of_week, StudyGroup.start_time).all()

    return render_template(
        'groups.html',
        groups=groups,
        days=DAYS,
        course_filter=course_filter,
        day_filter=day_filter,
    )


@app.route('/groups/new', methods=['GET', 'POST'])
def create_group():
    """
    Story: 'Will... wants to create a new study group for his course,
    so that he can start one when no current group fits his schedule.'
    """
    if request.method == 'POST':
        new_group = StudyGroup(
            course_code=request.form['course_code'].strip().upper(),
            course_name=request.form['course_name'].strip(),
            creator_name=request.form['creator_name'].strip(),
            day_of_week=request.form['day_of_week'],
            start_time=request.form['start_time'],
            end_time=request.form['end_time'],
            location=request.form.get('location', '').strip(),
            description=request.form.get('description', '').strip(),
        )
        db.session.add(new_group)
        db.session.commit()
        return redirect(url_for('list_groups'))

    return render_template('create_group.html', days=DAYS)


if __name__ == '__main__':
    app.run(debug=True)
