from fcntl import ioctl
from typing import List

from mediactl.libmediactl import (
    struct_media_entity_desc,
    MEDIA_IOC_ENUM_ENTITIES,
    MEDIA_ENT_ID_FLAG_NEXT
)


def get_media_entities(device_path: str) -> List[struct_media_entity_desc]:
    entity_id = 0
    entities = []

    with open(device_path, 'r') as f:
        while True:
            info = struct_media_entity_desc()
            info.id = entity_id | MEDIA_ENT_ID_FLAG_NEXT

            try:
                ioctl(f.fileno(), MEDIA_IOC_ENUM_ENTITIES, info)
            except OSError:
                # ioctl raises error when we are reaching
                # boundary of existing entities
                break

            entity_id = info.id

            entities.append(info)

    return entities
