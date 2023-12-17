from abc import ABC, abstractmethod


class RoomRepository(ABC):
    @abstractmethod
    def create_room(self, room):
        pass

    @abstractmethod
    def get_room(self, room_id):
        pass

    @abstractmethod
    def update_room(self, room):
        pass

    @abstractmethod
    def delete_room(self, room_id):
        pass
