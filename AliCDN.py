# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_cdn20180510.client import Client as Cdn20180510Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cdn20180510 import models as cdn_20180510_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Cdn20180510Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'cdn.aliyuncs.com'
        return Cdn20180510Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        refresh_object_caches_request = cdn_20180510_models.RefreshObjectCachesRequest(
            object_path='https://img.cdn.gaein.cn/Bing'
        )
        # 复制代码运行请自行打印 API 的返回值
        client.refresh_object_caches(refresh_object_caches_request)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        refresh_object_caches_request = cdn_20180510_models.RefreshObjectCachesRequest(
            object_path='https://img.cdn.gaein.cn/Bing'
        )
        # 复制代码运行请自行打印 API 的返回值
        await client.refresh_object_caches_async(refresh_object_caches_request)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
