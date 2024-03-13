"""
@Author                         : XiaoTao
@Email                          : 18773993654@163.com
@Lost modifid           : 2023/4/24 17:16
@Filename                       : config.py
@Description            : 
@Software           : PyCharm
"""
# DEBUG = False
# DB_NAME = "chatai_gray"
DB_NAME = "chatai"
ADMIN_DN = "chatai_admin"
# ADMIN_DN = "chatai_admin_gray"        # chat
# VHOST = "chat"
VHOST = "ai"
# VHOST = "develop"
# TODO MQ 配置
MQ_HOST = ""
MQ_SERVER = f"http://{MQ_HOST}:15672/"
DEBUG = True

# TODO HTTP 调用地址， 对应pay模块和 user模块服务地址
SERVER_IP = ""
CALLBACK = f"http://{SERVER_IP}:28083/"
SERVER_USER_URL = f"http://{SERVER_IP}:29090/"
SERVER_PAY_URL = f"http://{SERVER_IP}:28060/"
SERVER_COST_URL = f"http://{SERVER_IP}:28071/"

SERVER_OPENAI_URL = f"http://{SERVER_IP}:8080/"

# TODO Redis配置
REDIS_SERVER = ""
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_SERVER}/1',        # wc,um共用配置库

        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                # "decode_responses": True
                # "socket_timeout": 10
            },
        },
    },
    'cache': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_SERVER}/2',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                # "decode_responses": True
                # "socket_timeout": 10
            },
        },
    },
    'chat': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_SERVER}/10',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 500,

                "decode_responses": True
                # "socket_timeout": 10
            },
        },
    },
    'config': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_SERVER}/8',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                # "socket_timeout": 10
                "decode_responses": True
            },
        },
    },
    'model': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_SERVER}/30',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                # "socket_timeout": 10
                "decode_responses": True
            },
        },
    },
    #prompts
    'prompts': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_SERVER}/31',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                # "socket_timeout": 10
                "decode_responses": True
            },
        },
    },
}
# TODO DB配置
if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': DB_NAME,
            # 'NAME': "chatai",
            'USER': "root",
            'PASSWORD': "",
            'HOST': "",
            'PORT': 3306,
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
        },
        "admin": {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': ADMIN_DN,     # ai
            'USER': "root",
            'PASSWORD': "",
            'HOST': "",
            'PORT': 3306,
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'connect_timeout': 10
            },
        },
        "admin_video": {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "admin_video",  # ai
            'USER': "root",
            'PASSWORD': "",
            'HOST': "",
            'PORT': 3306,
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'connect_timeout': 10
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': DB_NAME,
            # 'NAME': "chatai",
            'USER': "root",
            'PASSWORD': "",
            'HOST': "",
            'PORT': 3306,
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
        },
        "admin": {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': ADMIN_DN,  # ai
            'USER': "root",
            'PASSWORD': "",
            'HOST': "",
            'PORT': 3306,
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'connect_timeout': 10
            },
        },
        "admin_video": {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "admin_video",  # ai
            'USER': "root",
            'PASSWORD': "",
            'HOST': "",
            'PORT': 3306,
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'connect_timeout': 10
            },
        }
    }


MQ = {
    "ty": {
        "USER": "admin",
        "PASSWORD": "",
        "HOST": MQ_HOST,
        "PORT": "5672",
        "vhost": VHOST,
        # "vhost": "ai",
    }
}

# channels_redis
# TODO
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["redis://:{redis地址}/3"],
        },
    },
}

REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'utils.exception.exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 设置以下为全局设置（除登录注册）需要带token才能访问接口
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'utils.auth_user.UserAuthentication',
    ),
    # 'UNAUTHENTICATED_USER': None,
    # 'UNAUTHENTICATED_TOKEN': None,  #将匿名用户设置为None
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     "utils.permissions.IsLoginUser", #设置路径，
    # ]
}

# AUTHENTICATION_BACKENDS = [
#     'utils.auth_user.CustomBackend',
#     # 'django.contrib.auth.backends.ModelBackend',
# ]



#TODO  baidu 绘画和语音 配置
B_APP_ID = ""
B_APP_KEY = ""
B_APP_SECRET = ""
# 百度语音
B_URI = "wss://vop.baidu.com/realtime_asr"


# TODO baidu 文心一言配置
ERNIE_APP_ID = ""       # 文心一言
ERNIE_APP_KEY = ""
ERNIE_APP_SECRET = ""
EB_HOST = "https://aip.baidubce.com/"


# TODO 阿里语音配置
A_URI = "wss://nls-gateway.cn-shanghai.aliyuncs.com"
A_APP_KEY = ""
ALI_APP_ID = ""     # 敏感词ai能力等
ALI_APP_SECRET = ""

# SD 服务地址
ADMIN_HOST = ""
SD_HOST = F"http://{ADMIN_HOST}:7860/"       # sd


#TODO 科大讯飞 配置
KD_APP_ID = ""
KD_API_SECRET = ""
KD_API_KEY = ""
KD_GPT_URL = ""

# TODO OSS 配置
ACCESS_KEY_ID = ""
ACCESS_KEY_SECRET = ""
BUCKET_NAME = ""
END_POINT = ""
NETWORK_STATION = ""


# TODO Claude Key
CLAUDE_KEY = """"""


# TODO 商汤 Key
ST_APP_ID = ""
ST_APP_SECRET = ""


# TODO 360 Key
QIHOO_URL = "https://api.360.cn/"


VG_TTS_APP_ID = ""
VG_TTS_TOKEN = ""

VG_AK = ""
VG_SK = ""