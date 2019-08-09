


from rest_framework import serializers
from goods.models import SKUImage,SKU
from fdfs_client.client import Fdfs_client
from django.conf import settings

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKUImage
        fields = ['id', 'sku', 'image']

    def validate(self, attrs):
        # 1、获得浏览器传来的文件数据
        file = attrs.pop("image") # 文件对象 file = open("zelda1", "rb")
        file_content = file.read() # 文件数据，bytes字节数据对象

        # 2、通过fdfs客户端程序完成文件上传
        # 2.1 构建fdfs客户端对象
        conn = Fdfs_client(settings.FDFS_CONF_PATH)
        # 2.2 通过客户端对象，完成文件数据的上传
        res = conn.upload_by_buffer(file_content)

        if res.get("Status") != 'Upload successed.' or not res:
            # 如果上传失败
            raise serializers.ValidationError("文件上传fdfs失败！")

        file_id = res.get("Remote file_id")

        attrs['image'] = file_id
        return attrs

    # def create(self, validated_data):
    #     # 手动调用fdfs客户端程序上传图片到分布式fdfs存储中
    #     # 获得返回到file_id。mysql中存储到就是文件的id
    #
    #     # 1、获得浏览器传来的文件数据
    #     file = validated_data.pop("image") # 文件对象 file = open("zelda1", "rb")
    #     file_content = file.read() # 文件数据，bytes字节数据对象
    #
    #     # 2、通过fdfs客户端程序完成文件上传
    #     # 2.1 构建fdfs客户端对象
    #     conn = Fdfs_client(settings.FDFS_CONF_PATH)
    #     # 2.2 通过客户端对象，完成文件数据的上传
    #     res = conn.upload_by_buffer(file_content)
    #     # return dict
    #     # {
    #     #     'Group name': group_name,
    #     #     'Remote file_id': remote_file_id,
    #     #     'Status': 'Upload successed.',
    #     #     'Local file name': '',
    #     #     'Uploaded size': upload_size,
    #     #     'Storage IP': storage_ip
    #     # } if success else None
    #     if res.get("Status") != 'Upload successed.' or not res:
    #         # 如果上传失败
    #         raise serializers.ValidationError("文件上传fdfs失败！")
    #
    #     file_id = res.get("Remote file_id")
    #
    #     # 3、构建模型类对象保存mysql数据库
    #     validated_data['image'] = file_id
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     # 1、获得浏览器传来的图片数据
    #     file = validated_data.pop("image")  # 文件对象 file = open("zelda1", "rb")
    #     file_content = file.read()  # 文件数据，bytes字节数据对象
    #
    #     # 2、使用fdfs客户端完成数据上传
    #     conn = Fdfs_client(settings.FDFS_CONF_PATH)
    #     # 2.2 通过客户端对象，完成文件数据的上传
    #     res = conn.upload_by_buffer(file_content)
    #     if res.get("Status") != 'Upload successed.' or not res:
    #         # 如果上传失败
    #         raise serializers.ValidationError("文件上传fdfs失败！")
    #
    #     new_file_id = res.get("Remote file_id")
    #
    #     # 3、更新模型类
    #     validated_data['image'] = new_file_id
    #     return super().update(instance, validated_data)


class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['id', 'name']