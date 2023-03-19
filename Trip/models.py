from django.db import models

# Create your models here.
from django.db import models

class Trip(models.Model):
    #    ⅰ. id primary
    trip_id = models.IntegerField(primary_key=True, verbose_name="商品唯一id")
    # ⅱ. 商品名称
    trip_name = models.CharField(max_length=200)
    # ⅲ. 商品描述
    trip_description = models.CharField(max_length=200)
    # ⅳ. 商品的价格
    trip_price = models.IntegerField(default=0)
    # ⅴ. 商品图片相对目录链接  "/src/source/imgsource/213123.jpg"
    trip_url = models.CharField(max_length=200)
    # ⅵ. 被预订的次数
    trip_num_bookings = models.IntegerField(default=0)
    # ⅶ. 逻辑删除 is_delete = false   false代表没有删除
    trip_logic_delete = models.BooleanField(default=0)