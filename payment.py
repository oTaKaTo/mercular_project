class Payment:
  def __init__(self, transaction_id, status, create_date):
    self.__transaction_id = transaction_id
    self.__status = status
    self.__create_date = create_date
  
  def get_status(self):
    return self.__status


class CreditCardTransaction(Payment):
  def __init__(self, transaction_id, status, create_date, name_on_card, card_id, CVC, due_date):
    Payment.__init__(self, transaction_id, status, create_date)
    self.__name_on_card = name_on_card
    self.__card_id = card_id
    self.__CVC = CVC
    self.__due_date = due_date

  def process(self):
    return True


class CashOnDeliveryTransaction(Payment):
  def __init__(self, transaction_id, status, create_date):
    Payment.__init__(self, transaction_id, status, create_date)

  def process(self):
    return True

class QRCodeTransaction(Payment):
  def __init__(self, transaction_id, status, create_date):
    Payment.__init__(self, transaction_id, status, create_date)

  def get_QRcode():
    pass