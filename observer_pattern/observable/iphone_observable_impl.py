from observer_pattern.observable.stocks_observable import StocksObservable


class IphoneObservableImpl(StocksObservable):
    
    def __init__(self):
        self.observer_list = []
        self.stock_count = 0
    
    def add(self, observer_instance):
        self.observer_list.append(observer_instance)
    
    def remove(self, observer_instance):
        self.observer_list.remove(observer_instance)

    def notify_subscribers(self):
        for observer in self.observer_list:
            observer.update()
    
    def set_stock_count(self, stock_unit_changed):
        if self.stock_count == 0:
            self.notify_subscribers()
        
        self.stock_count += stock_unit_changed

        if stock_unit_changed == 0:
            self.stock_count = stock_unit_changed
            print("Item is stock-out.")

    def get_stock_count(self):
        return self.stock_count
    