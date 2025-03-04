# SQLite_DB 基础课程攻略 🌟🌟🌟

以下内容将每个教学板块进行细化，并在相应位置提供示例代码，方便快速上手 SQLite 的基础操作与代码实现。 🌟🌟🌟

---

## 一、课程简介 🌟🌟🌟

1. **课程背景**：SQLite 作为一种轻量级的关系型数据库，不需要专门的服务器进程，适合移动端应用、桌面应用或小型项目的快速开发。
2. **课程特点**：
   - 理论与实践并重：边学边练。
   - 项目为导向：通过小任务、真实案例加深理解。
   - 大模型辅助：使用大模型进行搜索、编写示例、解决疑难问题。
3. **课程目标**：
   - 掌握 SQLite 数据库的基础概念与操作：创建、修改、删除数据库和表格等。
   - 能够根据需求进行数据库设计，并使用 ER 图进行逻辑结构规划。
   - 掌握 ORM（Object Relational Mapping）基础用法，将 Python 类与 SQLite 表结构映射。
   - 学会大模型提问技巧，快速查找答案并进行思路梳理。

> **AI 提示示例**：
> - “SQLite 数据库适用于哪些应用场景？能举几个常见的实际案例吗？”
> - “我需要轻量级的数据库为原型项目提供支撑，有哪些需要注意的地方？”

---

## 二、课程大纲与教学设计 🌟🌟🌟

### 1. 数据库的创建 🌟🌟🌟

- **教学内容**：
  - 熟悉 SQLite 数据库的基本概念及使用场景。
  - 学会使用 Python 自带的 `sqlite3` 模块或 SQLAlchemy 进行数据库连接与初始化。

- **实践操作**：
  - 直接使用 `sqlite3` 模块在本地创建数据库文件。
  - 在 Python 脚本中完成连接、建表、插入与查询等简易操作。

- **代码示例：使用 `sqlite3` 连接并初始化数据库**

```python
import sqlite3

# 1. 连接（如果文件不存在则自动创建）
connection = sqlite3.connect('example.db')

# 2. 创建游标
cursor = connection.cursor()

# 3. 创建一个简单的表
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
'''
cursor.execute(create_table_query)

# 4. 插入示例数据
insert_user_query = 'INSERT INTO users (username, email) VALUES (?, ?)'
users_data = [
    ('alice', 'alice@example.com'),
    ('bob', 'bob@example.com')
]
cursor.executemany(insert_user_query, users_data)

# 5. 查询并显示结果
select_query = 'SELECT id, username, email FROM users'
cursor.execute(select_query)
results = cursor.fetchall()

print("Users in database:")
for row in results:
    print(row)

# 提交事务并关闭连接
connection.commit()
connection.close()
```

> **AI 提示示例**：
> - “我想知道如何在 Python 环境中连接并初始化一个 SQLite 数据库文件，请给我代码示例和最佳实践。”
> - “如果使用 SQLAlchemy 进行连接和配置，需要注意哪些关键参数？”

---

### 2. 表格的创建 🌟🌟🌟

- **教学内容**：
  - 了解 SQLite 表结构的组成：字段类型、主键、外键等。
  - SQLAlchemy ORM 中如何定义对应的 Python 类（Model）。

- **实践操作**：
  - 直接编写 SQL 语句：`CREATE TABLE`。
  - 借助 SQLAlchemy：通过继承 `Base` 并定义类属性。

- **SQLAlchemy 代码示例：创建数据库表**

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. 创建引擎和基类
engine = create_engine('sqlite:///example_orm.db', echo=True)
Base = declarative_base()

# 2. 定义 User 类与数据库映射
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# 3. 创建表
Base.metadata.create_all(engine)

# 4. 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 5. 插入示例数据
user1 = User(username='charlie', email='charlie@example.com')
user2 = User(username='diana', email='diana@example.com')
session.add(user1)
session.add(user2)
session.commit()

# 6. 查询数据
all_users = session.query(User).all()
for user in all_users:
    print(user.id, user.username, user.email)

session.close()
```

> **AI 提示示例**：
> - “我想创建一个包含用户信息的数据表，结构包括 id、用户名、邮箱和注册时间，请问 SQL 语句怎么写？”
> - “如果使用 SQLAlchemy ORM 来建表，需要如何定义类和字段？”

---

### 3. 需求设计 🌟🌟🌟

- **教学内容**：
  - 需求分析思路：如何从业务需求中提炼数据库需求。
  - 介绍使用 diagrams.net（原 draw.io）绘制思维导图、流程图或用例图以辅助需求分析。

- **实践操作**：
  - 使用可视化工具将需求进行模块化拆分，列举实体、属性及相互之间的关系。
  - 与数据库表进行映射，思考如何落地到实际的表设计。

- **AI 提示示例**：
> - “请帮我整理一个应用场景的需求列表，并根据需求设计数据库结构。”
> - “如何根据业务流程图判断要创建多少张表？”

---

### 4. ER 图设计 🌟🌟🌟

- **教学内容**：
  - 实体(Entity)、属性(Attribute)、关系(Relationship)的区别与联系。
  - 通过 ER 图实现对业务逻辑的可视化梳理，进而映射到实际表结构。

- **实践操作**：
  - 根据给定的业务场景或想法，先绘制 ER 图（实体、关系、属性等）。
  - 将 ER 图转化为相应的建表语句或 ORM 定义。

> **AI 提示示例**：
> - “根据以下业务描述生成相应的 ER 图，请给出详细的实体与关系定义。”
> - “当实体之间存在多对多关系时，如何在 ER 图中表示并在实际数据库中实现？”

---

### 5. 案例与小任务 🌟🌟🌟

#### 案例1：在 SQLite + ORM 中创建自定义编码类型 🌟🌟🌟

- **教学内容**：
  - 如何在 SQLite 中存储自定义类型，如枚举或带编码转换的字段。
  - 在 SQLAlchemy 中实现自定义类型映射。

- **自定义类型映射示例**：
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import TypeDecorator

engine = create_engine('sqlite:///custom_type.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class ColorType(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        # 假设我们的颜色用整数字符串表示，类似 '255,0,0'
        if isinstance(value, tuple):
            return ','.join(map(str, value))
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return tuple(map(int, value.split(',')))
        return value

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(ColorType)

Base.metadata.create_all(engine)
session = Session()

# 插入示例
product = Product(name='T-Shirt', color=(255,0,0))
session.add(product)
session.commit()

# 查询示例
result = session.query(Product).first()
print(f"Product: {result.name}, Color: {result.color}")  # 输出: (255, 0, 0)

session.close()
```

> **AI 提示示例**：
> - “我想在 SQLite 中存储一个自定义编码类型（例如颜色、状态枚举）该如何实现？”
> - “如何在 ORM 中编写自定义类型并注册给 SQLAlchemy？”

#### 案例2：远程数据库应用（以 MySQL 为例） 🌟🌟🌟

- **教学内容**：
  - 了解远程数据库部署与本地 SQLite 的区别及应用场景。
  - SQLAlchemy 连接远程 MySQL 的实际操作和注意点。

- **代码示例**：
```python
from sqlalchemy import create_engine

# 使用 PyMySQL 驱动连接远程 MySQL
# 假设远程服务器 IP 是 192.168.1.100，端口3306
# 数据库名 testdb，用户名 root，密码 mypassword

engine = create_engine('mysql+pymysql://root:mypassword@192.168.1.100:3306/testdb')

# 后续操作与 SQLite 类似，例如
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
# ...
```

> **AI 提示示例**：
> - “如何配置远程数据库连接？需要注意哪些安全问题？”
> - “在 MySQL 上建立表格和在 SQLite 有哪些区别？”

---

## 三、实施方案 🌟🌟🌟

1. **理论+实践相结合**：通过紧凑的知识讲解和上手实验，增强对数据库的理解。
2. **小组讨论与分工**：学生之间相互交流与配合，完成小型项目式的任务。
3. **大模型辅助**：
   - 学会提问：带上下文地向大模型描述问题，获取更准确的解答。
   - 学会迭代：对不满意的回答或复杂问题，多次询问、补充细节。
4. **学习反馈与总结**：
   - 及时展示与答疑，复盘学习效果。
   - 探索更多高级用法，或融合更多技术（如数据可视化等）。

---

## 四、资源与参考 🌟🌟🌟

- **官方文档**：
  - [SQLite 官方文档](https://sqlite.org/docs.html)
  - [SQLAlchemy 官方文档](https://docs.sqlalchemy.org/)
- **工具**：
  - diagrams.net (前身是 draw.io)
    用它来创建我们所需的一切图表链接：https://app.diagrams.net/
  - ![img.png](drawio绘制需求图的示例.png)
  - Python + SQLAlchemy + SQLite
- **大模型使用建议**：
  - **清晰描述需求**：描述问题场景、代码上下文、报错信息，以便大模型快速定位重点。
  - **善用上下文**：多轮对话时，随时补充之前的结果或新的需求。
  - **反复迭代**：如果回答不理想或不完整，可不断追加提问或更改要点。

---



