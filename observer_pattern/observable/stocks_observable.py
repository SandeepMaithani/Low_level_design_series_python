from abc import ABC, abstractmethod

class StocksObservable(ABC):

    @abstractmethod
    def add(observer_instance):
        pass

    @abstractmethod
    def remove(observer_instance):
        pass

    @abstractmethod
    def notify_subscribers():
        pass

    @abstractmethod
    def set_stock_count(stock_unit_changed):
        pass

    @abstractmethod
    def get_stock_count():
        pass