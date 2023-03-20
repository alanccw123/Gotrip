from django.test import TestCase

# Create your tests here.
import unittest


def test_view_my_order_button(self):
    # 发送 GET 请求到目标页面
    response = self.client.get('/orders/')
    # 检查响应状态码是否为 200 OK
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "login")
