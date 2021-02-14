from database import db, ma

class Acutal(db.Model):
    __tablename__ = 'Model_test'
    __bind_key__ = 'mysql_db'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    parameter = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Parameter model: {self.parameter}, created at {self.date_created}"


class AcutalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Acutal
        load_instance = True



class Result(db.Model):
    __tablename__ = 'results'
    __bind_key__ = 'post_db'

    id = db.Column(db.String(), primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(db.String(20))
    result_no_stop_words = db.Column(db.String(20))

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)

class ResultSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Result
        load_instance = True
