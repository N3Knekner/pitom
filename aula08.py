# Atividades:
# ● Criar rota para retornar os clientes dos mercados LATAM, US e Canada;
# ● Criar rota para retornar lista de pedidos e itens do mercado EU;
# ● Criar rota para retornar os pedidos do anos 2013 e 2014 da categoria Furniture no mercado EMEA;

from fastapi import FastAPI
import pandas as pd
import datetime as dt
import json
import sqlite3 as sql

app = FastAPI()

conexao = sql.connect('globalstore_normalizada.db')


@app.get('/')
async def hello():
    return "hello!"


@app.get('/v1/{target}')
async def version_1(target: str):
    return json.dumps({'teste': True, 'target': target})


@app.get('/products')
async def products():
    # conexao = sql.connect('globalstore_normalizada.db')
    prod = pd.read_sql(con=conexao, sql='select * from products')
    return prod.to_json(orient='records')


# REST: /tabela/id/subtabela/id...
# ex: /apis/v1/
# Plurals: /authors/ ; becouse the return will be a list of authors
#          /apis/ will return a list with all versions

# "{\"name\":{\"0\":\"category\",\"1\":\"subcategory\",\"2\":\"products\",\"3\":\"orders\",\"4\":\"items\",\"5\":\"customer\",\"6\":\"city\",\"7\":\"region\"}}"

# ● Criar rota para retornar os clientes dos mercados LATAM, US e Canada;
@app.get('/markets/l_u_c')
async def markets():
    markets_ = pd.read_sql(
        con=conexao, sql="SELECT customer.* from customer join city using(cty_sequence) join region using(reg_sequence) where market in ('LATAN', 'US', 'Canada')")
    return markets_.to_json(orient='records')

# ● Criar rota para retornar lista de pedidos e itens do mercado EU;


@app.get('/markets/{target}/orders')
async def orders(target: str):
    orders_ = pd.read_sql(
        con=conexao, sql=f"SELECT orders.*, market from orders join customer using(cst_sequence) join city using(cty_sequence) join region using(reg_sequence)")
    orders_ = orders_[orders_['market'] == target]
    return orders_.to_json(orient='records')


@app.get('/markets/{target}/orders/items')
async def orders(target: str):
    orders_ = pd.read_sql(
        con=conexao, sql=f"SELECT items.* from items join orders using(ord_sequence) join customer using(cst_sequence) join city using(cty_sequence) join region using(reg_sequence) where market like '{target}'")
    return orders_.to_json(orient='records')

# ● Criar rota para retornar os pedidos do anos 2013 e 2014 da categoria Furniture no mercado EMEA;


@app.get('/markets/{target}/orders/{year}/category/{category}')
async def orders_category(target: str, year: str, category: str):
    orders_ = pd.read_sql(con=conexao, sql="SELECT distinct orders.*, market, category from orders join customer using(cst_sequence) join items using(ord_sequence) join products using (pro_sequence) join subcategory using(sub_sequence) join category using (cat_sequence) join city using(cty_sequence) join region using(reg_sequence)")
    orders_ = orders_[orders_['market'] == target]
    orders_ = orders_[orders_['category'] == category]
    return orders_[orders_['order_date'].apply(lambda x: x[-2:] == year)].to_json(orient='records')
