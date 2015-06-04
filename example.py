#!/usr/bin/env python

from databox import Client, push

Client("adxg1kq5a4g04k0wk0s4wkssow8osw84")\
    .push("templj", 92.2)

push("templj", 102.3, token="adxg1kq5a4g04k0wk0s4wkssow8osw84")