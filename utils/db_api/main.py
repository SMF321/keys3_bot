import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
#DATABASE_NAME = 'database.sqlite'
engine = db.create_engine(f'sqlite:///utils\db_api\database.sqlite')
connection = engine.connect()
metadata = db.MetaData()


Users = db.Table('Users', metadata, autoload=True, autoload_with=engine)
User_Data = db.Table('User_Data', metadata,
                     autoload=True, autoload_with=engine)
Question = db.Table('Question', metadata, autoload=True, autoload_with=engine)
Suggest = db.Table('Current_Suggestion', metadata,
                   autoload=True, autoload_with=engine)


def POST_USER(id1, FIO1):
    query = db.insert(Users).values(Id=id1, Username='',
                                    FIO=FIO1, Phone='')
    ResultProxy = connection.execute(query)
    query = db.insert(Question).values(Id=id1, Question='',
                                       Class_question='', datetime='')
    ResultProxy = connection.execute(query)


def POST_NEW_SUGGESTIONS(id1, suggestion1, description):
    query = db.insert(Suggest).values(Id=id1, Suggestion=suggestion1,
                                      Description=description)
    ResultProxy = connection.execute(query)


def POST_USER_DATA(id1, fio1, username1):
    query = db.insert(User_Data).values(Id=id1, FIO=fio1,
                                        Username=username1)
    ResultProxy = connection.execute(query)


def POST_PHONE(id1, phone1):
    query = db.update(Users).values(Phone=phone1)
    query = query.where(Users.columns.Id == id1)
    results = connection.execute(query)


def POST_USERNAME(id1, username1):
    query = db.update(Users).values(Username=username1)
    query = query.where(Users.columns.Id == id1)
    results = connection.execute(query)


def POST_QUESTION(id1, question1, class_question1, datetime1):
    query = db.update(Question).values(Question=question1,
                                       Class_question=class_question1, datetime=datetime1)

    query = query.where(Question.columns.Id == id1)
    results = connection.execute(query)


def GET_QUESTION(class_question1):
    return db.select([Question.columns.Class_question, Question.columns.Question, Users.columns.Username, Users.columns.FIO, Question.columns.datetime]).where(
        Question.columns.Class_question == class_question1).where(Users.columns.Id == Question.columns.Id)


def GET_SUGGESTIONS():
    a = db.select([Suggest.columns.Suggestion])
    mass_suggestions = []
    for row in connection.execute(a).fetchall():
        mass_suggestions.append(row[0])
    return mass_suggestions


def GET_DESCRIPTION(suggestion1):
    a = db.select([Suggest.columns.Description]).where(
        Suggest.columns.Suggestion == suggestion1)
    mass_description = []
    for row in connection.execute(a).fetchall():
        mass_description.append(row[0])
    return mass_description[0]


def UPDATE__USER_DATA_USER(id1, fio1, username1):
    query = db.update(User_Data).values(FIO=fio1,
                                        Username=username1)

    query = query.where(User_Data.columns.Id == id1)
    ResultProxy = connection.execute(query)
    query = db.update(Users).values(Id=id1, Username=username1,
                                    FIO=fio1, Phone=''
                                    )
    query = query.where(Users.columns.Id == id1)
    ResultProxy = connection.execute(query)
