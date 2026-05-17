from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def get_hello():
    return {"message": "你好，fastapi"}


@app.get("/user/hello")
async def get_user():
    return {'msg': '我正在学习fastapi'}


# 路径参数
@app.get('/book/{id}')
async def get_book(id: int):
    return {'id': id, 'title': f'这是第{id}本书'}


@app.get('/books/{id}')
async def get_books(id: int = Path(gt=0, lt=100, description="书籍id，取值范围是0到100")):  # Path在路径参数做类型注解
    return {'id': id}


# 需求：查找书籍的作者，路径参数 name，长度范围2-10
@app.get('/author/{name}')  # 注意：要把路径区分开，不要用/book或者/books，因为相同的路径会先匹配第一个，
async def get_name(name: str = Path(..., min_length=2, max_length=10)):
    return {'msg': f'这是{name}的信息'}


# 查询参数
# 查询新闻，要有分页功能,skip:跳过的记录数，limit：返回的记录数10
@app.get('/news/news_list')
async def get_news_list(
        skip: int = Query(default=0, gt=0, lt=9, description="最大是0，最小是9"),
        limit: int = Query(10)
):  # Query在查询参数做类型注解
    return {'跳过的记录数是：': {skip}, '返回的记录数是': {limit}}


# 练习题：设计接口查询图书，要求携带两个查询参数：图书分类和价格
# 参数具体要求：图书分类：长度限制5-255
# 价格：限制大小:50-100
@app.get('/news/news_info')
async def get_news_info(
        type: str = Query(min_length=5, max_length=255),
        price: int = Query(gt=50, lt=100),
):
    return {'type': type, 'price': price}


# 请求体参数
# 需求：注册，用户名+密码，str
from pydantic import BaseModel, Field


class User(BaseModel):
    username: str
    password: str


@app.post('/register')
async def register(user: User):
    return user


# 练习：设计接口新增图书，图书信息包含：书名、作者、出版社、售价
class Book(BaseModel):
    name: str = Field(..., min_length=2, max_length=20)  # 请求体参数用Field
    author: str = Field(min_length=2, max_length=20)
    publishing_house: str = Field(default="花生出版社")
    price: int = Field(..., gt=0)


@app.post('/add_book')
async def add_book(book: Book):
    return book


# 相应类型：html格式
@app.get('/html', response_class=HTMLResponse)
async def get_html():
    return "<h1>这是一级标题</h1>"


# 相应类型：文件格式
@app.get('/file')
async def get_file():
    path = '../../test.txt'
    print(path)
    return FileResponse(path)


# 自定义相应数据格式
# 需求：定义一个新闻接口，包含id,title,content
from pydantic import BaseModel


class News(BaseModel):
    id: int
    title: str
    content: str


@app.get('/news/{id}', response_model=News)
async def get_news(id: int):
    return {
        'id': id,
        'title': f'这是第{id}本书',
        'content': '这是一本好书'
    }


from fastapi import HTTPException


# 异常处理
# 需求：按id查询新闻，id范围是1到6
@app.get('/_news/{id}')
async def _get_news(id: int):
    id_list = [1, 2, 3, 4, 5, 6]
    if id not in id_list:
        raise HTTPException(status_code=404, detail='您查找的新闻不存在')
    return {'id': id}


# 中间件：给每个请求前后添加统一的逻辑处理
@app.middleware("http")
async def middleware(request, call_next):
    print('中间件1 start')
    response = await call_next(request)
    print('中间件1 end')
    return response


# 如果有多个中间件，执行顺序是自底向上
@app.middleware("http")
async def middleware(request, call_next):
    print('中间件2 start')
    response = await call_next(request)
    print('中间件2 end')
    return response


# 依赖注入
from fastapi import Depends


# 分页参数逻辑共用：新闻列表和用户列表
# 1.依赖项
async def common_parameters(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, lt=20),
):
    return {'skip': skip, 'limit': limit}


@app.get("/user/hello2")
async def get_user(common=Depends(common_parameters)):
    return common


# 挂载路由
from routers import news

app.include_router(news.router)
