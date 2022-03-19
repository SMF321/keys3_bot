import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
engine = db.create_engine(f'sqlite:///utils\db_api\database.sqlite')
connection = engine.connect()
metadata = db.MetaData()


User_Data = db.Table('User_Data', metadata,
                     autoload=True, autoload_with=engine)
Question = db.Table('Question', metadata, autoload=True, autoload_with=engine)
Suggest = db.Table('Current_Suggestion', metadata,
                   autoload=True, autoload_with=engine)
Secret = db.Table('Secret_Table', metadata,
                  autoload=True, autoload_with=engine)


def POST_TEST(id1):
    query = db.insert(Question).values(Id=id1, Question='',
                                       Class_question='', DONE=0)
    ResultProxy = connection.execute(query)


def POST_NEW_SUGGESTIONS(id1, suggestion1, description):
    query = db.insert(Suggest).values(Id=id1, Suggestion=suggestion1,
                                      Description=description)
    ResultProxy = connection.execute(query)


def POST_NEW_SUGGESTIONS1(suggestion1):
    query = db.insert(Suggest).values(Suggestion=suggestion1,
                                      Description='')
    ResultProxy = connection.execute(query)


def POST_NEW_SUGGESTION_DESCRIPTION(description1):
    query = db.update(Suggest).values(Description=description1)
    query = query.where(
        Suggest.columns.Description == '')
    ResultProxy = connection.execute(query)


def POST_USER_DATA(id1, username1,):
    query = db.insert(User_Data).values(Id=id1, Username=username1, BAN=0)
    ResultProxy = connection.execute(query)


def POST_QUESTION(id1, question1):
    query = db.update(Question).values(Question=question1)
    query = query.where(Question.columns.Id == id1).where(
        Question.columns.Question == '')
    results = connection.execute(query)


def POST_QUESTION_DELETE():
    query = db.delete(Question)
    query = query.where(Question.columns.Class_question == '')
    results = connection.execute(query)


def POST_CLASS_QUESTION(id1, class_question1):
    query = db.insert(Question).values(Id=id1, Question='',
                                       Class_question=class_question1)
    ResultProxy = connection.execute(query)


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


def UPDATE__USER_DATA_USER(id1,  username1):
    query = db.update(User_Data).values(
        Username=username1)

    query = query.where(User_Data.columns.Id == id1)
    ResultProxy = connection.execute(query)


def GET_QUESTION(id1):
    a = db.select([Question.columns.Question, Question.columns.Class_question]).where(
        Question.columns.Id == id1)
    mass_description = []
    mass_description1 = []
    mass_description2 = []
    for row in connection.execute(a).fetchall():
        mass_description1.append(row[0])
        mass_description2.append(row[1])
    mass_description.append(mass_description1)
    mass_description.append(mass_description2)
    return mass_description


def DELETE_SUGGESTION(suggestion1):
    query = db.delete(
        Suggest)
    query = query.where(Suggest.columns.Suggestion == suggestion1)
    results = connection.execute(query)


def GET_VIEW(class_question1):
    a = db.select([Question.columns.Question, Question.columns.Class_question]).where(
        Question.columns.Class_question == class_question1).where(Question.columns.DONE == 0)
    mass_description = []
    for row in connection.execute(a).fetchall():
        mass_description.append(row[0])
    if len(mass_description) == 0:

        return 'Все записи по данной теме просмотрены'
    return mass_description[0], GET_VIEW1(mass_description[0], class_question1)


def GET_IS_NULL(class_question1):
    query = db.update(Question).values(DONE=0)
    query = query.where(Question.columns.Class_question == class_question1)
    ResultProxy = connection.execute(query)
    return 'Все записи по данной теме просмотрены'


def GET_VIEW1(question, class_question1):
    if (question == ''):
        print(GET_IS_NULL(class_question1))
        return -1
    a = db.select([Question.columns.Id]).where(
        Question.columns.Question == question).where(
        Question.columns.Class_question == class_question1)
    mass_description1 = []
    for row in connection.execute(a).fetchall():
        mass_description1.append(row[0])
    return GET_VIEW2(mass_description1[0], class_question1, question)


def GET_VIEW2(id1, class_question1, question):
    query = db.update(Question).values(DONE=1)
    query = query.where(Question.columns.Class_question == class_question1).where(
        Question.columns.Question == question)
    ResultProxy = connection.execute(query)
    if (id1 == -1):
        return 'Все записи по данной теме просмотрены'
    a = db.select([User_Data.columns.Username]).where(
        User_Data.columns.Id == id1)
    mass_description2 = []
    for row in connection.execute(a).fetchall():
        mass_description2.append(row[0])
    return mass_description2[0]


def GET_COUNT_MESSAGE(class_question1):
    a = db.select([db.func.count(Question.columns.DONE)]).where(
        Question.columns.DONE == 0).where(Question.columns.Class_question == class_question1)
    mass_description = []
    for row in connection.execute(a).fetchall():
        mass_description.append(row[0])
    return mass_description[0]


def GET_ALL_NULL():
    a = db.select([db.func.count(Question.columns.DONE)]).where(
        Question.columns.DONE == 0)
    mass_description = []
    for row in connection.execute(a).fetchall():
        mass_description.append(row[0])
    return mass_description[0]


def BAN(username1):
    username1 = username1[1:-1]
    query = db.update(User_Data).values(BAN=1)
    query = query.where(User_Data.columns.Username == username1)
    ResultProxy = connection.execute(query)
    return'Пользователь '+username1+' добавлен в бан-список'


def GET_BAN():
    a = db.select([User_Data.columns.Id]).where(
        User_Data.columns.BAN == 1)
    mass_description = []
    for row in connection.execute(a).fetchall():
        mass_description.append(row[0])
    return mass_description


def GET_SECRET_KEY():
    a = db.select([Secret.columns.Secret_key])
    mass_description = []
    for row in connection.execute(a).fetchall():
        mass_description.append(row[0])
    return mass_description


def GET_SECRET_SUGGESTION(secret_key1):
    a = db.select([Secret.columns.Secret_suggestion]).where(
        Secret.columns.Secret_key == secret_key1)
    mass_description = []
    for row in connection.execute(a).fetchall():
        mass_description.append(row[0])
    return mass_description
