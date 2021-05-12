# docker 排坑

## 安装 wsl2需要更新 -> 直接根据链接update

## 安装 error during connect: This error may indicate that the docker daemon is not running.

* 看官方文档是Hyper-V被其他服务禁用了 reset一下(估计是安装模拟器造成的)

```powershell
bcdedit /set hypervisorlaunchtype auto
```



## Failed to set version to docker-desktop: exit code: -1 

![image-20210512183323991](C:\Users\Kongxiangzhouye\AppData\Roaming\Typora\typora-user-images\image-20210512183323991.png)

```powershell
netsh winsock reset
```

# Swagger Editor

## 启动

* win10不能用pwd 替换为

    ```powershell
    docker run -d -p 80:8080 -v "C:/Users/Kongxiangzhouye/Desktop/git clone/whale-web:/tmp" -e SWAGGER_FILE=/tmp/openapi.yaml swaggerapi/swagger-editor
    ```

    

## schema -> ref

* 引用openapi.yml下面的格式

## 添加接口说明

* 主要是看后端代码和数据库加假数据造请求查看

```yml
openapi: 3.0.3
info:
  title: Bluewhale
  description: 'This is API specifications for bluewhale site'
  version: 1.0.0
servers:
  - url: http://127.0.0.1:8000
paths:
  # 省略重复
  "/api/v1/verify/{token}":
    get:
      parameters:  
        - name: token
          in: path
          description: token。
          required: true
          schema:
            type: string
      summary: verify verification token
      responses:
        '200':
          description: success verify
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/VerifySuccess"
          
  "/api/v1/register":
    post:
      summary: register
      requestBody:
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/RegisterForm"
      responses:
        '200':
          description: success register
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    $ref: "#/components/schemas/User"
                  code:
                    type: integer
                    
  "/api/v1/articles":
    get:
      summary: articles
      responses:
        '200':
          description: get all articles
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Articles"
  "/api/v1/articles/{pk}":
    get:
      summary: articles
      parameters:  
        - name: pk
          in: path
          description: primary key
          required: true
          schema:
            type: string
      responses:
        '200':
          description: get all articles
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Article"
  
components:
  schemas:
    # 省略重复
    VerifySuccess:
      type: object
      properties:
        data:
          type: string
        code:
          type: integer
    RegisterForm:
      type: object
      properties:
        email:
          type: string
          format: email
        password:
          type: string
    Article:
      type: object
      properties:
        id:
          type: string
        author:
          type: string
        title:
          type: string
        content:
          type: string
        created_at:
          type: string
        updated_at:
          type: string
        status:
          type: string
    Articles:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: "#/components/schemas/Article"
        code:
          type: integer
        
```

