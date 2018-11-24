import psycopg2
import psycopg2.extras
import json

conn = psycopg2.connect("dbname='db' user='username' host='localhost' password='password'")
cur = conn.cursor()

def get_users():

    query = """SELECT * from users"""
    cur.execute(query)
    columns = ( 'username', 'password', 'cuisine')
    results = []
    rows = cur.fetchall()
    for row in rows:
        results.append(dict(zip(columns, row)))


def get_restaurant_details(keyword, filter):

    if filter == "Cuisine":

        query = """ SELECT * from restaurants where cuisine = """ + "'" +keyword + "'"
        print(query)
        cur.execute(query)
        columns = ( 'res_id', 'res_name', 'locality', 'address', 'cuisine', 'avg_cft', 'price_range', 'avg_rating', 'img_link' )
        results = []
        rows = cur.fetchall()
        for row in rows:
            results.append(dict(zip(columns, row)))

        return results

    elif filter == "location":

        query = """ SELECT * from restaurants where locality = """ + "'" +keyword + "'"
        print(query)
        cur.execute(query)
        columns = ( 'res_id', 'res_name', 'locality', 'address', 'cuisine', 'avg_cft', 'price_range', 'avg_rating', 'img_link' )
        results = []
        rows = cur.fetchall()
        for row in rows:
            results.append(dict(zip(columns, row)))

        return results

    elif filter == "id":

        query0 = """ SELECT * from restaurants where res_id = """ + "'" +keyword + "'"
        print(query0)
        cur.execute(query0)
        columns = ( 'res_id', 'res_name', 'locality', 'address', 'cuisine', 'avg_cft', 'price_range', 'avg_rating', 'img_link' )
        results = []
        rows = cur.fetchall()
        for row in rows:
            results.append(dict(zip(columns, row)))

        return results


        

def get_restaurant_reviews(id):

    results = get_restaurant_details(id, "id")
    

    query = """ SELECT * from reviews where res_id = """ + id 
    print(query)
    cur.execute(query)
    columns = (  'res_id', 'username', 'review_text', 'sentiment' )
    datas = []
    rows = cur.fetchall()
    for row in rows:
        datas.append(dict(zip(columns, row)))

    resp = []
    resp.append(results)
    resp.append(datas)

    return resp    


def set_restaurant_review(id, username, review, sentiment):

    

    cur.execute("INSERT INTO reviews (res_id, username, review_text, sentiment) VALUES (%s, %s, %s, %s)", (id, username, review, sentiment))
    print("######################WXECUTED####################")
    return 0







if __name__ == "__main__":

    print(get_restaurant_details("Thai", "Cuisine"))




