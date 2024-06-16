from observer_pattern.observable.iphone_observable_impl import IphoneObservableImpl
from observer_pattern.observer.email_alert_observer_impl import EmailAlertObserverImpl
from observer_pattern.observer.mobile_alert_observer_impl import MobileAlertObserverImpl

iphone_stock_observable = IphoneObservableImpl()
email_observer_1 = EmailAlertObserverImpl(email_id='abc1@gmail.com', observable_instance=iphone_stock_observable)
email_observer_2 = EmailAlertObserverImpl(email_id='xyz1@hotmail.com', observable_instance=iphone_stock_observable)
mobile_observer_1 = MobileAlertObserverImpl(user_name='123@outlook.com', observable_instance=iphone_stock_observable)

iphone_stock_observable.add(observer_instance=email_observer_1)
iphone_stock_observable.add(observer_instance=email_observer_2)
iphone_stock_observable.add(observer_instance=mobile_observer_1)

# this will notify user
print("Adding 5 units to stock.\n")
iphone_stock_observable.set_stock_count(stock_unit_changed=5)

# this will not notify user
print("\nAdding 2 units to stock.")
iphone_stock_observable.set_stock_count(stock_unit_changed=2)

# this will not notify user
print("\nSetting units to 0.")
iphone_stock_observable.set_stock_count(stock_unit_changed=0)

# this will notify user
print("\nAdding 2 more units.")
iphone_stock_observable.set_stock_count(stock_unit_changed=5)

