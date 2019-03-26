import os
from uuid import uuid4


def uuid_upload_to(instance, filename):
    uuid_name = uuid4().hex
    ext = os.path.splitext(filename)[-1].lower()

    return '/'.join([
        uuid_name[:2], # uuid는 16진수로 이뤄지므로 2자리의 조합만으로 256가지 조합이 생성됨
        uuid_name[2:4],
        uuid_name[4:] + ext
    ])
